# Azure Content Filter

A serverless content filtering microservice built with Azure Functions (Python v2 model).

## Features

-   **HTTP Trigger**: `filter_comment` endpoint.
-   **Content Filtering**: Detects and masks bad words (e.g., "bad", "terrible", "worst").
-   **JSON Output**: Returns original text, filtered text, and safety status.

## Prerequisities

-   Python 3.8+
-   Azure Functions Core Tools
-   Azure CLI

## Local Development

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/raksit/azure-content-filter.git
    cd azure-content-filter
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the function locally:**

    ```bash
    func start
    ```

5.  **Test the endpoint:**

    Use `curl` or Postman to send a POST request to `http://localhost:7071/api/filter_comment`:

    ```bash
    curl -X POST http://localhost:7071/api/filter_comment \
         -H "Content-Type: application/json" \
         -d '{"comment": "This is a really bad example."}'
    ```

    **Expected Response:**

    ```json
    {
        "original": "This is a really bad example.",
        "filtered": "This is a really **** example.",
        "is_safe": false
    }
    ```

## Deploy to Azure

1.  **Login to Azure:**

    ```bash
    az login
    ```

2.  **Deploy using Azure Functions Core Tools:**

    ```bash
    func azure functionapp publish <APP_NAME>
    ```

    *Alternatively, use the VS Code Azure Functions extension for easier deployment.*
