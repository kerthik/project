import streamlit as st
import os

# Folder to save uploaded images
UPLOAD_FOLDER = "students/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

st.title("Student Image Uploader")

name = st.text_input("Enter Student Name:")
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if st.button("Upload"):
    if not name.strip():
        st.error("Error: Name cannot be empty")
    elif uploaded_file and allowed_file(uploaded_file.name):
        name = name.strip().replace(" ", "_")  # Replace spaces with underscores
        ext = uploaded_file.name.rsplit(".", 1)[1].lower()
        filename = f"{name}.{ext}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File '{filename}' uploaded successfully!")
    else:
        st.error("Error: Invalid file format")

