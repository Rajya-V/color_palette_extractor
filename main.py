from utils import load_image, preprocess_image, extract_colors, plot_palette
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    return file_path

# Select and process image
image_path = select_image()

if not image_path:
    print("No file selected. Exiting...")
    exit()

image = load_image(image_path)
processed_image = preprocess_image(image)

# Apply K-Means clustering
k = 5
colors, labels = extract_colors(processed_image, k)

# Display results
plt.imshow(image)
plt.axis("off")
plt.show()
plot_palette(colors, labels)
