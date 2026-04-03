from kindle_klipper import parser, database
from pathlib import Path

def main():
    print("starting kindle_klipper!")
    
    root = Path(__file__).resolve().parent.parents[1]
    clippings_path = root / "My Clippings.txt"
    if not clippings_path.exists():
        print(f"Error: {clippings_path} not found. Please ensure the file is in the correct location.")
        return
    parser.parse_clippings(clippings_path)
    database.update_database("kindle_highlights.csv", "kindle_clippings.db", "highlights")
