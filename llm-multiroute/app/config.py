import os


class Settings:
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", "8080"))
    APP_NAME: str = os.getenv("APP_NAME", "llm-multiroute")
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "https://ollama.com")
    OLLAMA_TEMPERATURE: float = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
    OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "")

    # Per-route model assignments (must be available on Ollama cloud).
    # All 4 routes are temporarily pinned to gemma4:31b-cloud - it's the only
    # model confirmed to work on the free tier (glm-5.2/mistral-large-3/minimax-m3
    # return 402 Payment Required without purchased credits). Restore per-task
    # diversity once credits/a paid plan are added.
    OLLAMA_MODEL_CLASSIFY: str = os.getenv("OLLAMA_MODEL_CLASSIFY", "gemma4:31b-cloud")
    OLLAMA_MODEL_SENTIMENT: str = os.getenv("OLLAMA_MODEL_SENTIMENT", "gemma4:31b-cloud")
    OLLAMA_MODEL_SUMMARIZE: str = os.getenv("OLLAMA_MODEL_SUMMARIZE", "gemma4:31b-cloud")
    OLLAMA_MODEL_INTENT: str = os.getenv("OLLAMA_MODEL_INTENT", "gemma4:31b-cloud")


settings = Settings()
