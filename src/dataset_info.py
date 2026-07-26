from pathlib import Path

# Path to dataset
dataset_path = Path("data/PlantVillage")

# Find all class folders
class_folders = sorted([folder for folder in dataset_path.iterdir() if folder.is_dir()])

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print(f"\nNumber of Classes: {len(class_folders)}\n")

total_images = 0

for folder in class_folders:
    image_count = len(list(folder.glob("*.jpg")))
    total_images += image_count
    print(f"{folder.name:<35} {image_count} images")

print("\n" + "=" * 50)
print(f"Total Images: {total_images}")
print("=" * 50)