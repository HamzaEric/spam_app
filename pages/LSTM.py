import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

def main():
    st.set_page_config(layout="wide")
    st.title('Implementation Of Long Short-Term Memory (LSTM)')
    st.markdown('---')
    st.header('How It Works')
    st.write('''
    LSTM (Long Short-Term Memory) is used to detect spam 
    by analyzing the sequence of words in SMS messages. 
    LSTM can remember context across the message, which helps it understand patterns 
    like "free prize" or "click here" that often indicate spam.
    ''')
    st.write('''
    The model processes each message word by word, learning which words (and their order)
    are important. It uses memory cells and gates to decide what to remember 
    and what to ignore. After training on labeled messages, 
    the LSTM can then predict whether a new SMS is spam or not based on learned patterns.
    ''')
    st.markdown('---')
    st.subheader('Building Of The Neural Network')

    html_file = Path('Deep_Learning_in_NLP_LSTM_for_Sequence_Classification.html')
    components.html(html_file.read_text(encoding='utf-8', errors='replace'), height=1000, scrolling=True)
if __name__ == '__main__':
    main()