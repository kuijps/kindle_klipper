import random

from kindle_klipper.database import get_all_highlights

def pick_random_highlight(conn):
    highlights = get_all_highlights(conn)
    return random.choice(highlights)