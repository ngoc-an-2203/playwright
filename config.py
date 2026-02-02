import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
# You can set these environment variables in a .env file or in your system environment
# Example .env file content:
"""
TIMEOUT=120000
HANBAI_BASE_URL=https://demo.hanbai.vn
"""

TIMEOUT = int(os.getenv("TIMEOUT", 120000))
"""Default load page timeout: 120 seconds"""

HANBAI_BASE_URL = os.getenv("HANBAI_BASE_URL", "https://demo.hanbai.vn")
"""Default base URL for Hanbai application"""

HANBAI_AUTH_FILE = "hanbai_auth.json"
"""Default file path for storing Hanbai authentication state"""

PORTAL_BASE_URL = os.getenv("PORTAL_BASE_URL", "https://demo.sorimachi.vn")

PORTAL_AUTH_FILE = "portal_auth.json"
"""Default file path for storing Portal authentication state"""

PORTAL_USERNAME = os.getenv("PORTAL_USERNAME", "trangnguyen")
"""Default username for Portal login"""

PORTAL_PASSWORD = os.getenv("PORTAL_PASSWORD", "123456")
"""Default password for Portal login"""


