import streamlit as st
import time



def main():
    st.set_page_config('Information retrieval')
    st.header('AskMyDOC !!')

    with st.sidebar:
        st.title('Menu:')
        pdf_doc = st.file_uploader("upload your pdf file here and click on submit", accept_multiple_files=True)
        
        if st.button('submit'):
            
            with st.spinner('Processing'):
                time.sleep(5)

                st.success('Done')



if __name__ == "__main__":
    main()
