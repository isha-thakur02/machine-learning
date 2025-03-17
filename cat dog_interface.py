
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("model.h5")  # Make sure this file is in the correct path

# Define class labels
classes = ["Cat", "Dog"]  # Adjust labels if needed

# Function to open and classify image
def classify_image():
    global img_label, result_label

    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    
    if not file_path:
        return  # If no file is selected, do nothing

    # Load the image
    img = Image.open(file_path)
    img = img.convert("RGB")  # Ensure it's in RGB format
    img = img.resize((64, 64))  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict the class
    prediction = model.predict(img_array)
    result = classes[np.argmax(prediction)]

    # Display the image in the GUI
    img = img.resize((200, 200))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)

    img_label.config(image=img_tk)
    img_label.image = img_tk

    # Display prediction result
    result_label.config(text=f"Prediction: {result}", font=("Arial", 14, "bold"))

# Create GUI window
root = tk.Tk()
root.title("Cat vs Dog Classifier")
root.geometry("400x500")

# Heading label
heading = tk.Label(root, text="Image Classification", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Button to select an image
btn_select = tk.Button(root, text="Choose Image", command=classify_image, font=("Arial", 12))
btn_select.pack(pady=10)

# Label to display the selected image
img_label = tk.Label(root)
img_label.pack()

# Label to display the prediction result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
