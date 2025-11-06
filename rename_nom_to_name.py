import json
from pathlib import Path

# Path to the mega_evolution.json file
INPUT_FILE = Path(__file__).parent / "reference_images" / "mega-evolution" / "fr-fr" / "mega_evolution.json"

def main():
    # Load the JSON file
    with INPUT_FILE.open("r", encoding="utf-8") as f:
        cards = json.load(f)
    
    # Replace "nom" with "name" in each card entry
    for card in cards:
        if "nom" in card:
            card["name"] = card["nom"]
            del card["nom"]
    
    # Write back with proper formatting
    with INPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Fixed {len(cards)} card entries")
    print("All 'nom' fields renamed to 'name'")

if __name__ == "__main__":
    main()
