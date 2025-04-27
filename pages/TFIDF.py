import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
def main():
    st.set_page_config(layout="wide")
    st.title('Implementation Of Text Frequency-Inverse Document Frequency(TFIDF)')
    st.markdown('---')
    st.write('''
    TF-IDF is a technique that scores words based on how important they are in a 
    document by balancing word frequency and uniqueness across documents.
    ''')
    st.markdown('---')
    st.header('Using PortStemmer')
    st.write('''
    In spam detection, TF-IDF helps identify important words in messages, and PorterStemmer simplifies words to their root form (e.g., “running” → “run”).
    TF-IDF gives weight to unique, spam-indicative words (like “free”, “win”),
    PorterStemmer ensures similar words are treated the same, improving accuracy.
    ''')
    html_file=Path('portstemmer.html')
    components.html(html_file.read_text(encoding='utf-8',errors='replace'),height=1000,scrolling=True)
    st.markdown('---')
    st.header('Using WordNetLemmatizer')
    st.write('''
    WordNet Lemmatizer reduces words to their dictionary form
    based on meaning.
    Then, TF-IDF scores these lemmatized words by their importance—highlighting 
    key spam indicators while ignoring common terms.
    ''')
    html_file=Path('wordnetlemmatizer.html')
    components.html(html_file.read_text(encoding='utf-8',errors='replace'),height=1000,scrolling=True)
if __name__ == '__main__':
    main()