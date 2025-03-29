import os
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.telegram_token = os.getenv("TELEGRAM_TOKEN")
        self.db_path = os.getenv("DB_PATH", "data/chat_history.db")
        self.config_file = os.getenv("CONFIG_FILE", "config.yaml")
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                config_data = yaml.safe_load(file)
                self.api_key = config_data.get("API_KEY", self.api_key)
                self.telegram_token = config_data.get("TELEGRAM_TOKEN", self.telegram_token)
                self.db_path = config_data.get("DB_PATH", self.db_path)
        else:
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")