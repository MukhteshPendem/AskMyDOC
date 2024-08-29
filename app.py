import streamlit as st
import time
from src.helper import get_pdf_text


def process_pdf(pdf_docs):
    if pdf_docs:
        with st.spinner('Processing...'):
            
            output = get_pdf_text(pdf_docs)
           
            st.write("Extracted Text Preview:")
            st.write(output[:500])  
            st.success('File processed successfully!')
    else:
        st.warning('Please upload a PDF file before submitting.')

def main():
    st.set_page_config(page_title='Information Retrieval', layout='wide')

    
    st.sidebar.title('Navigation')
    option = st.sidebar.selectbox("Choose a page:", ["Home", "Upload", "About"])

    if option == "Home":
        st.header('Welcome to AskMyDOC!')
        st.write("""
            **Welcome to AskMyDOC!**  
            Here you can upload your PDF documents to extract information. Use the sidebar to navigate through different sections of the app.
        """)
    
    elif option == "Upload":
        st.header('Upload Your PDF')
        pdf_docs = st.file_uploader("Upload your PDF file here", accept_multiple_files=True)
        if st.button('Submit'):
            process_pdf(pdf_docs)
    
    elif option == "About":
        st.header('About Us')
        st.write("""
            **About AskMyDOC**  
            AskMyDOC is a tool designed to help you extract information from PDF documents easily. Simply upload your PDF files and let the tool process them for you.
        """)

if __name__ == "__main__":
    main()
