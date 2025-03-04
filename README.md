# Color Detection in Images using K-Means Clustering

## Overview
This project implements a color detection system using K-Means clustering to extract dominant colors from an image. 
The program allows users to select an image, preprocess it, apply clustering, and visualize the extracted colors in a palette.

## Features
- Load and preprocess images
- Apply K-Means clustering to detect dominant colors
- Display the original image
- Visualize detected colors in a color palette

## Dependencies
Ensure you have the following Python libraries installed before running the script:

```sh
pip install numpy matplotlib scikit-learn pillow opencv-python tkinter
```

## How to Run
1. Clone or download this repository.
2. Run the script using:

```sh
python color_detection.py
```
3. A file dialog will prompt you to select an image file (JPG, PNG, JPEG).
4. The program will process the image and display:
   - The original image
   - A bar chart representing the extracted colors

## File Structure
```
├── color_detection.py  # Main script
├── utils.py            # Contains helper functions
├── README.md           # Project documentation
```

## Functions Explained
### `load_image(image_path, max_size=(400, 400))`
Loads an image, converts it to RGB format, resizes it, and converts it into a NumPy array.

### `preprocess_image(img)`
Reshapes the image into a 2D array where each row represents a pixel’s RGB values.

### `extract_colors(img, k=5)`
Applies K-Means clustering to extract `k` dominant colors from the image.

### `plot_palette(colors, labels)`
Displays a bar chart of the extracted colors with their respective proportions.

## Example Output
After selecting an image, the script will generate an output similar to the following:
- **Original Image Display**
- **Color Palette Bar Chart**

## Customization
- Modify the `k` value in `extract_colors(img, k=5)` to change the number of detected colors.
- Adjust `max_size` in `load_image` to set a different image resize limit.

## License
This project is open-source and available under the MIT License.

## Author
Rajya-V

