from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import streamlit as st
from PIL import Image


load_dotenv(find_dotenv())   

def img2text(image):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(image)[0]["generated_text"]
    return text

def main():
    st.title("Image to Text Generator")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Read the content of the uploaded file and convert it to a PIL image
        pil_image = Image.open(uploaded_file)
        
        st.image(pil_image, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Use the img2text function to get the generated text
        result_text = img2text(pil_image)

        st.success(f"Generated Text: {result_text}")

if __name__ == "__main__":
    main() 
