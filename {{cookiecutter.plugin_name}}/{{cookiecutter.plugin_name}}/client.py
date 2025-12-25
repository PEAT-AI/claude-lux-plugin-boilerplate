"""API client for {{cookiecutter.plugin_display_name}}.

This module provides HTTP client functionality for external API calls.
Customize this for your specific API integration.
"""
{%- if cookiecutter.include_api_client %}

import httpx

# Default timeout for API requests (seconds)
DEFAULT_TIMEOUT = 30.0


class APIClient:
    """HTTP client for external API calls."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.example.com",
        timeout: float = DEFAULT_TIMEOUT,
    ):
        """Initialize the API client.

        Args:
            api_key: API authentication key
            base_url: Base URL for API endpoints
            timeout: Request timeout in seconds
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._client: httpx.Client | None = None

    @property
    def client(self) -> httpx.Client:
        """Get or create the HTTP client."""
        if self._client is None:
            self._client = httpx.Client(
                base_url=self.base_url,
                timeout=self.timeout,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
            )
        return self._client

    def get(self, endpoint: str, **kwargs) -> httpx.Response:
        """Make a GET request.

        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments passed to httpx.get

        Returns:
            HTTP response
        """
        return self.client.get(endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> httpx.Response:
        """Make a POST request.

        Args:
            endpoint: API endpoint path
            **kwargs: Additional arguments passed to httpx.post

        Returns:
            HTTP response
        """
        return self.client.post(endpoint, **kwargs)

    def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            self._client.close()
            self._client = None

    def __enter__(self) -> "APIClient":
        return self

    def __exit__(self, *args) -> None:
        self.close()


def test_api_connection(api_key: str) -> bool:
    """Test API connectivity.

    Args:
        api_key: API key to test

    Returns:
        True if connection successful, False otherwise
    """
    try:
        with APIClient(api_key) as client:
            # Customize this endpoint for your API
            response = client.get("/health")
            return response.status_code == 200
    except Exception:
        return False
{%- else %}
# API client not included in this plugin.
# Set include_api_client=true in cookiecutter to enable.
{%- endif %}
