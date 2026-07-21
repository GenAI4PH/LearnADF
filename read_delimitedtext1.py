from pathlib import Path
import json

# Read dataset/DelimitedText1.json from the workspace root
file_path = Path(__file__).resolve().parent / "dataset" / "DelimitedText1.json"

with file_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

print(json.dumps(data, indent=2))
