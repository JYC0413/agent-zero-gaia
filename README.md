
# Agent Zero - Gaia Integration

This fork of the Agent Zero project integrates the Gaia node for model inference, replacing the original OpenAI API. Additionally, it includes a minor adjustment for Docker SSH connection to enhance reliability under proxy conditions.

## Adjustments

1. **Gaia Node Integration**:
    - The entire process now uses Gaia's node for model inference: `https://llama.us.gaianet.network/v1`.
    - This replaces the previous OpenAI integration.

2. **Docker SSH Address**:
    - The SSH address for connecting to Docker has been changed from `localhost` to `127.0.0.1`.
    - This adjustment prevents connection timeouts when running under certain proxy conditions.

## Installation and Usage

### Prerequisites

- Python 3.x
- Docker installed and running on your system

### Steps

1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Start Docker**:
    - **Windows**:
        - If Docker Desktop is installed, simply open Docker Desktop, and it will start automatically.
    - **macOS**:
        - If Docker Desktop is installed, open it from the Applications folder or use Spotlight Search.
    - **Linux**:
        - Ensure Docker is installed, and start the service with the following command:
            ```bash
            sudo systemctl start docker
            ```

3. **Project Environment Variables Configuration Guide**:

This project allows you to customize certain environment variables to connect your AI models and choose your preferred search engine. If you don't configure these variables, the program will run with default values.

① Configuring Environment Variables

First, you need to create a `.env` file in the root directory of the project. You can do this by copying the `example.env` file and renaming it to `.env`:

#### For Linux or macOS:
```bash
cp example.env .env
```
#### For Windows (Command Prompt):
```cmd
copy example.env .env
```
#### For Windows (PowerShell):
```powershell
Copy-Item -Path example.env -Destination .env
```
② Editing the .env File 
Open the .env file in your preferred text editor and fill in the following variables if you want to use your own models:
`CHAT_MODEL_BASE_URL`
`CHAT_MODEL_NAME`
`CHAT_API_KEY`
`EMBEDDING_MODEL_BASE_URL`
`EMBEDDING_MODEL_NAME`
`EMBEDDING_API_KEY`

#### Optional Configuration for PERPLEXITY Search
If you want to use PERPLEXITY search, add your API key by filling in the API_KEY_PERPLEXITY variable
If this variable is not set, the program will default to using DuckDuckGo combined with the chat model you configured.

3. **Run the Project**:
    ```bash
    python main.py
    ```

## Notes

- The project runs without requiring any environment variables to be set.
- The performance and output should be nearly identical to the original version using OpenAI.