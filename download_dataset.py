import os
import gdown
import zipfile

# Google Drive file ID extracted from the link
dataset_id = "16taCsZOmOJ22qw0LVTQmMcKlMTP3DTUY"

# Output directory and filename
os.makedirs("Dataset", exist_ok=True)
dataset_zip_path = "Dataset/spectrograms.zip"

# Download the dataset
print(f"⬇ Downloading dataset to: {dataset_zip_path}")
gdown.download(id=dataset_id, output=dataset_zip_path, quiet=False)

# Extract the ZIP file
print(" Extracting dataset...")
with zipfile.ZipFile(dataset_zip_path, 'r') as zip_ref:
    zip_ref.extractall("Dataset/")
    print(" Dataset extracted to 'Dataset/'")

print("Dataset download and extraction complete.")
