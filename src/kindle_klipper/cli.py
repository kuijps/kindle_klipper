from kindle_klipper import parser, database, email, selector
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
    clippings_path = root / "data" / "My Clippings.txt"
    if not clippings_path.exists():
        print(f"Error: {clippings_path} not found. Please ensure the file is in the correct location.")
        return
    parser.parse_clippings(clippings_path)
    database.create_database("kindle_highlights.csv", "kindle_clippings.db", "highlights")
    
    email.send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT)
    #email.send_email("ckuijpe@gmail.com", "testing", "im using a new email client library")
    

def random_highlight():
    conn = database.connect_db(DB_PATH)
    highlight = selector.pick_random_highlight(conn)
    print(highlight)
    email_subject = f"Random Kindle Highlight: {highlight[0]} by {highlight[1]}"
    email_content = f"{highlight[0]} by {highlight[1]}\n\n{highlight[4]}\n\nAdded on: {highlight[3]}"
    email.send_email(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO, email_subject, email_content)