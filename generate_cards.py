import json
import re
from pathlib import Path

# Configuration
ROOT = Path(__file__).parent
IMAGES_DIR = ROOT / "reference_images" / "mega-evolution" / "fr-fr"
OUTPUT_JSON = ROOT / "reference_images" / "mega-evolution" / "fr-fr" / "cards.json"
SET_NAME = "MEG"
LANG = "fr"

FILENAME_PATTERN = re.compile(r"JL2G_FR_(\d+)\.png", re.IGNORECASE)

# Minimal base template for new cards
BASE_TEMPLATE = {
    "set": SET_NAME,
    "language": LANG,
    "category": "Pokemon",  # Placeholder; adjust if needed
    "rarity": "À définir",   # Placeholder
}

def load_existing():
    if OUTPUT_JSON.exists():
        try:
            with OUTPUT_JSON.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
        except Exception:
            pass
    return []


def index_existing(existing):
    by_number = {}
    for card in existing:
        num = card.get("number") or card.get("id")
        if isinstance(num, int):
            by_number[num] = card
    return by_number


def build_card_entry(number: int, image_filename: str):
    # French placeholder name; you can later replace with the real card name.
    name = f"Carte {number}"
    entry = {
        **BASE_TEMPLATE,
        "number": number,
        "name": name,
        "image": f"reference_images/mega-evolution/fr-fr/{image_filename}",
    }
    return entry


def main():
    existing = load_existing()
    existing_index = index_existing(existing)

    new_cards = []
    for file in sorted(IMAGES_DIR.glob("*.png")):
        m = FILENAME_PATTERN.match(file.name)
        if not m:
            continue
        number = int(m.group(1))
        if number in existing_index:
            # Optionally enrich existing card with image if missing
            card = existing_index[number]
            if "image" not in card:
                card["image"] = f"reference_images/mega-evolution/fr-fr/{file.name}"
            continue  # Keep original metadata
        new_cards.append(build_card_entry(number, file.name))

    # Merge: keep existing at front, append new ones sorted by number
    merged = existing + sorted(new_cards, key=lambda c: c["number"])

    # Write pretty JSON
    with OUTPUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=4)

    print(f"Generated {len(new_cards)} new card entries. Total now: {len(merged)}")


if __name__ == "__main__":
    main()
