import cv2
import glob
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_folder = os.path.join(base_dir, "images")

images = sorted(glob.glob(os.path.join(input_folder, "page_*.png")))

if not images:
    print("Neam page_*.png sliki najdeno vo images/ folderot.")
else:
    for path in images:
        img = cv2.imread(path)

        if img is None:
            print(f"Ne se cita: {path}, prodolzhuvam.")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray, h=10)
        _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imwrite(path, binary)
        print(f"Preprocesirano: {path}")

    print(f"\nDone! Preprocesirani {len(images)} sliki.")