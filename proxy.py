from mitmproxy import http
import json

def request(flow: http.HTTPFlow) -> None:
    # Target URL to intercept
    if flow.request.pretty_url == "https://demo.playwright.dev/api-mocking/api/v1/fruits":
        # Mock response data, only including the "Strawberry" entry
        mock_data = [
            {
                "name": "Banana",
                "id": 1
            }
        ]
        
        # Prepare the mock response
        mock_response = json.dumps(mock_data).encode("utf-8")
        
        # Set custom response
        flow.response = http.Response.make(
            200,  # status code
            mock_response,  # response body
            {"Content-Type": "application/json"}  # headers
        )
