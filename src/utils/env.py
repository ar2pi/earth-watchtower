import dotenv
import os

dotenv.load_dotenv()

def env_value(key: str):
    return os.environ.get(key)
