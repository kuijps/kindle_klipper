import re
import pandas as pd

def parse_clippings(path):
    # Read the content of the file
    with open(path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    # Split the content into individual entries
    entries = content.split("==========")

    data = []

    # Process each entry
    for entry in entries:
        lines = [l.strip() for l in entry.strip().split("\n") if l.strip()]
        # Ensure lines has enough elements before accessing
        if len(lines) < 3:
            continue

        title_author = lines[0]
        meta = lines[1]
        text = " ".join(lines[2:])

        # Extract title and author
        title, author = re.match(r"(.*) \((.*)\)", title_author).groups()

        # Extract location and date
        location = re.search(r"Location ([\d-]+)", meta)
        date = re.search(r"Added on (.*)", meta)

        # Append the extracted data
        data.append({
            "title": title,
            "author": author,
            "location": location.group(1) if location else None,
            "date": date.group(1) if date else None,
            "text": text
        })
    
  
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv("kindle_highlights.csv", index=False)
    