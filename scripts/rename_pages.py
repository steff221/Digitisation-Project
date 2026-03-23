import os
import glob

input_folder = "images"

images = sorted(glob.glob(f"{input_folder}/*.png"))

if not images:
    print("No images found in the images/ folder!")
else:
    for i, old_path in enumerate(images, start=1):
        new_name = f"page_{i:03d}.png"
        new_path = os.path.join(input_folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {os.path.basename(old_path)} → {new_name}")

    print(f"\nDone! Renamed {len(images)} images.")