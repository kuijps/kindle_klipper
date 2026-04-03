from kindle_klipper import parser, database, email
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
DB_PATH = os.getenv("DB_PATH")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT")


def main():
    print("starting kindle_klipper!")
    
    root = Path(__file__).resolve().parent.parents[1]
    clippings_path = root / "My Clippings.txt"
    if not clippings_path.exists():
        print(f"Error: {clippings_path} not found. Please ensure the file is in the correct location.")
        return
    parser.parse_clippings(clippings_path)
    database.update_database("kindle_highlights.csv", "kindle_clippings.db", "highlights")
    email.send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT)