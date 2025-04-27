import streamlit as st


def main():
    st.title('🛠️📖 Documentation')
    st.markdown('---')
    st.subheader('The Purpose Of The Project')
    st.markdown('---')
    st.write('''
   The purpose of this project is to build a deep learning model using 
   Long Short-Term Memory (LSTM) networks to automatically 
   detect and classify SMS messages as spam or not spam
    ''')
    st.markdown('---')
    st.subheader('''📊 Dataset ''')
    st.write('''

    Source: Kaggle

    Total samples: 5000 Legitimate domains and 5000 Phising domains

    Features:(e.g.Text,Label)

    Each sample is labeled as:

    -ham-Normal text
    -spam-spam text

    



    ''')
    st.markdown('---')
    st.subheader('🏗️Tech Stack')
    st.markdown('---')
    st.write('''

    1.Language: Python

    2.ML Libraries: Scikit-learn,TensorFlow/Keras

    Data Handling: Pandas, NumPy

    Visualization: Matplotlib, Seaborn

    Notebook: Jupyter
    ''')

    st.markdown('---')
    st.subheader('✅ Conclusion')
    st.markdown('---')
    st.write('''

    This project demonstrates that machine learning is highly effective for Spam detection. It provides strong accuracy and interpretability, and can be further extended into:

    Future improvements/works:

    1.Use Pretrained Embeddings
    
    2.Bidirectional LSTM
    
    ''')
    st.markdown('---')
    st.subheader('📚 References')
    st.markdown('---')

    st.markdown("""
    - [Youtube Tutorial](https://www.youtube.com/watch?v=YCzL96nL7j0)
""")
    st.markdown('---')

    st.subheader('👨‍💻 Developer Information')
    st.markdown('---')
    st.code('''
    st.write('Name:Eric Hamza Maina')
    ''')
    st.write('Access Me')
    st.markdown('''
    [instagram](https://www.instagram.com/hamza.aaah_k1/)

    [Github](https://github.com/HamzaEric)

    ''')


if __name__ == '__main__':
    st.set_page_config(
        layout="wide",
    )
    main()