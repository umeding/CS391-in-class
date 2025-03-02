import load_dotenv
import os

load_dotenv.load_dotenv()

DB_URI = os.getenv("DB_URI", "sqlite:///:memory:")
JWT_SECRET = os.getenv("JWT_SECRET", "defaultsecretvalue")
