import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO

# Set Streamlit page configuration
st.set_page_config(page_title="Gemini Health App")

# Load environment variables (cached to avoid reloading)
@st.cache_resource
def load_environment():
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
@st.cache_data
def get_gemini_pro_response(image_data, prompt):
    try:
        # Set up the model once
        model = genai.GenerativeModel(model_name="gemini-pro-vision")
        response = model.generate_content([image_data, prompt])
        return response.text
    except Exception as e:
        st.error(f"Error in generating prediction: {e}")
        return None

# Function to setup image for API
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()  # Get file as bytes

        # Prepare the image parts for the API call
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Main app interface
def main():
    load_environment()  # Load environment once

    st.header("Gemini Health App")
    
    # Prompt (fixed, no user input needed)
    input_prompt = """
    You are an expert nutritionist. Analyze the food items from the image and calculate the total calories. 
    Provide details of every food item with calorie intake in the following format:

    1. Item 1 - number of calories
    2. Item 2 - number of calories
    ----
    """

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        try:
            # Load and display the image
            image = Image.open(BytesIO(uploaded_file.getvalue()))
            st.image(image, caption="Uploaded Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image: {e}")

    # Submit button for generating predictions
    if st.button("Tell me the total calories") and uploaded_file is not None:
        with st.spinner("Processing..."):
            try:
                # Prepare image data and call API
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_pro_response(image_data, input_prompt)
                
                # Display response or warn if no response
                if response:
                    st.subheader("The Response is:")
                    st.write(response)
                else:
                    st.warning("No response received from the model.")
            except Exception as e:
                st.error(f"Error in processing request: {e}")
    elif st.button("Tell me the total calories"):
        st.warning("Please upload an image first.")

# Run the app
if __name__ == "__main__":
    main()