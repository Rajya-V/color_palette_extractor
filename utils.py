import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

def load_image(image_path, max_size=(400, 400)):
    img = Image.open(image_path)
    img = img.convert("RGB")
    img.thumbnail(max_size)  
    img = np.array(img)
    return img

def preprocess_image(img):
    return img.reshape((-1, 3))

def extract_colors(img, k=5):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_.astype(int)
    labels = np.unique(kmeans.labels_, return_counts=True)[1]
    return colors, labels

def plot_palette(colors, labels):
    sorted_indices = np.argsort(-labels)
    colors = colors[sorted_indices]
    labels = labels[sorted_indices]
    
    plt.figure(figsize=(8, 2))
    plt.bar(range(len(colors)), labels, color=[c/255 for c in colors], width=1)
    plt.xticks([])
    plt.yticks([])
    plt.show()
