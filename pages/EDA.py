import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
def main():
    st.set_page_config(layout="wide")
    st.title('Exploratory Data Analysis')
    st.markdown('---')
    st.write('''
    In this section, we explore the dataset to understand its structure, identify patterns, and detect any anomalies or imbalances.
    This helps in gaining insights and preparing the data for effective model training.
    ''')
    st.markdown('---')

    html_file = Path('Spam_sms_classifier_EDA.html')
    components.html(html_file.read_text(encoding='utf-8', errors='replace'), height=1000, scrolling=True)
if __name__ == '__main__':
    main()