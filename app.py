import streamlit as st
import os
from utils.file_utils import detect_file_type
from utils.text_extraction import extract_text
from utils.language_detection import detect_languages

def main():
    st.title("File Type and Language Detector")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "xlsx", "csv", "pptx", "txt"])

    if uploaded_file is not None:
        temp_file = "temp_file"

        with open(temp_file, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            file_type = detect_file_type(temp_file)
            text = extract_text(temp_file, file_type)
            languages = detect_languages(text)

            st.success("File processed successfully!")
            st.write("File Type:", file_type)
            st.write("Detected Languages:", ", ".join(languages))

            # Display a sample of the extracted text
            st.subheader("Sample of Extracted Text")
            st.text(text[:500] + "..." if len(text) > 500 else text)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

        finally:
            os.remove(temp_file)

if __name__ == "__main__":
    main()
