import json
from pathlib import Path

# Paths
ROOT = Path(__file__).parent
INPUT_FILE = ROOT / "reference_images" / "mega-evolution" / "fr-fr" / "mega_evolution.json"
IMAGES_DIR = ROOT / "reference_images" / "mega-evolution" / "fr-fr"

def main():
    # Load the JSON file
    with INPUT_FILE.open("r", encoding="utf-8") as f:
        cards = json.load(f)
    
    # Get all image files in the directory
    image_files = {f.name: f.name for f in IMAGES_DIR.glob("JL2G_FR_*.png")}
    
    # Add image field to each card based on its number
    for card in cards:
        number = card.get("number")
        if number:
            # Convert "001" to 1 for filename matching
            num_int = int(number)
            # Construct expected filename
            image_filename = f"JL2G_FR_{num_int}.png"
            
            # Check if file exists
            if image_filename in image_files:
                card["image"] = f"reference_images/mega-evolution/fr-fr/{image_filename}"
            else:
                print(f"Warning: Image not found for card {number}: {image_filename}")
    
    # Write back with proper formatting
    with INPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Added image paths to {len(cards)} card entries")

if __name__ == "__main__":
    main()
