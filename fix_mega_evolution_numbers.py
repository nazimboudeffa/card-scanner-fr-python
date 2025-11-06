import json
from pathlib import Path

# Path to the mega_evolution.json file
INPUT_FILE = Path(__file__).parent / "reference_images" / "mega-evolution" / "fr-fr" / "mega_evolution.json"

def main():
    # Load the JSON file
    with INPUT_FILE.open("r", encoding="utf-8") as f:
        cards = json.load(f)
    
    # Fix each card entry
    for card in cards:
        # Get the number (either from "numero" or "number")
        if "numero" in card:
            num = card["numero"]
            del card["numero"]
        elif "number" in card:
            num = card["number"]
            # If it's already a string, convert to int first
            if isinstance(num, str):
                num = int(num)
        else:
            print(f"Warning: Card has no number field: {card}")
            continue
        
        # Format as 3-digit string with leading zeros
        card["number"] = f"{num:03d}"
    
    # Write back with proper formatting
    with INPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Fixed {len(cards)} card entries")
    print("All 'numero' fields converted to 'number' with 3-digit format")

if __name__ == "__main__":
    main()
