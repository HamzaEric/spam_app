import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
def main():
    st.set_page_config(layout="wide")
    st.title('Implementation Of CountVectorizer')
    st.markdown('---')
    st.write('''
    CountVectorizer converts text into a matrix of token counts
    it simply counts how often each word appears in a document.
    ''')
    st.markdown('---')
    st.header('Using PortStemmer')
    st.write('''
    PorterStemmer ensures similar words are treated as one 
    but it does truncation so i word might not be in the dictionary
    ''')
    html_file=Path('ps.html')
    components.html(html_file.read_text(encoding='utf-8',errors='replace'),height=1000,scrolling=True)
    st.markdown('---')
    st.header('Using WordNetLemmatizer')
    st.write('''
    A Lemmatizer reduces words to their root form but not in truncation 
    but to develop a real dictionary word
    ''')
    html_file=Path('wnl.html')
    components.html(html_file.read_text(encoding='utf-8',errors='replace'),height=1000,scrolling=True)
if __name__ == '__main__':
    main()