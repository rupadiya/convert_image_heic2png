from PIL import Image
import pillow_heif
import os

# Directories
input_dir = 'img'
output_dir = 'output'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".heic"):
        # Read the HEIC file
        heif_file = pillow_heif.read_heif(os.path.join(input_dir, filename))
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )

        # Save the image as PNG in the output directory
        output_filename = os.path.splitext(filename)[0] + ".png"
        image.save(os.path.join(output_dir, output_filename), "png")

print("Conversion complete!")
