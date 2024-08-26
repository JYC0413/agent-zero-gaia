
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

3. **Run the Project**:
    ```bash
    python main.py
    ```

## Notes

- The project runs without requiring any environment variables to be set.
- The performance and output should be nearly identical to the original version using OpenAI.