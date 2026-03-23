import os
import glob
import pytesseract
from PIL import Image

book_name = "Чуварот"

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images_folder = os.path.join(base_dir, "images")
output_folder = os.path.join(base_dir, "ocr_output")
output_file = os.path.join(output_folder, f"{book_name}_ocr_raw.txt")

os.makedirs(output_folder, exist_ok=True)

image_paths = sorted(glob.glob(os.path.join(images_folder, "page_*.png")))

if not image_paths:
    print("Ne se najdeni sliki vo images/ folderot.")
    print("Proveren folder:", images_folder)
    exit()

all_text = []

for path in image_paths:
    print(f"Processing {path}...")
    img = Image.open(path)

    text = pytesseract.image_to_string(
        img,
        lang="mkd",
        config="--oem 1 --psm 6"
    )

    all_text.append(f"===== {os.path.basename(path)} =====\n{text}\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))

print(f"\nGotovo! OCR output zachuvan vo {output_file}.")