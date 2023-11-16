import streamlit as st
from PIL import Image
import os
import time

def resize_images_in_folder(input_folder, output_folder, new_size=(1024, 533)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Record start time
    start_time = time.time()

    # Initialize spinner
    progress_bar = st.progress(0.0)
    with st.spinner("Resizing images..."):
        # Process each file in the input folder
        for i, file_name in enumerate(os.listdir(input_folder)):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Open the image
                file_path = os.path.join(input_folder, file_name)
                with Image.open(file_path) as img:
                    # Resize the image
                    resized_img = img.resize(new_size)

                    # Save the resized image to the output folder
                    resized_file_path = os.path.join(output_folder, file_name)
                    resized_img.save(resized_file_path)

                # Update progress bar
                progress = (i + 1) / len(os.listdir(input_folder))
                progress_bar.progress(progress)

    # Calculate and display the time taken for resizing
    end_time = time.time()
    elapsed_time = end_time - start_time
    st.success(f"Images resized successfully in {elapsed_time:.2f} seconds!")

# Streamlit app
st.title("Image Resizer App")

# Sidebar for input and output folders
st.sidebar.header("Settings")

# Get the directory of the current script
current_script_directory = os.path.dirname(__file__)

# Combine with relative paths for input and output folders
input_folder = st.sidebar.text_input("Input Folder Path", os.path.join(current_script_directory, "path/to/input/folder"))
output_folder = st.sidebar.text_input("Output Folder Path", os.path.join(current_script_directory, "path/to/output/folder"))

# Slider for selecting image size
new_width = st.sidebar.slider("Select Width for Resized Images", 100, 2000, 1024)
new_height = st.sidebar.slider("Select Height for Resized Images", 100, 2000, 533)

# Button to trigger image resizing
if st.sidebar.button("Resize Images"):
    new_size = (new_width, new_height)
    resize_images_in_folder(input_folder, output_folder, new_size)