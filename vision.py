

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the API key
genai.configure(api_key=os.getenv("google_api_key"))

# Load the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # Recommended for object detection

# Function to get Gemini response
def get_gemini_response(input, image):
    if input.strip():  # Fixed condition for empty input
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit page configuration
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

# Input for text prompt
input = st.text_input("Input Prompt:", key="input")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Fixed typo
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
if st.button("Tell me about the image"):
    if image is not None:
        response = get_gemini_response(input, image)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.error("Please upload an image before submitting.")
