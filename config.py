# config.py
# Shared configuration variables for the project.

import os

API_BASE_URL = os.getenv("MONEYPENNY_API_BASE_URL", "https://api.agenthack.uk/api")
DEFAULT_LLM_MODEL = "gemini-2.5-flash-preview-05-20"
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "ADDS")
