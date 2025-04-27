import pickle
import streamlit as st

# Load the TF-IDF vectorizer and SVM model separately
tfidf_loaded = pickle.load(open("tfidf_vectorizer.pickle", "rb"))
svm_loaded_model = pickle.load(open("SVC.pickle.dat", "rb"))

# Function to predict if the input message is spam or not
def predict_spam(message):
    # Transform the message using the TF-IDF vectorizer
    message_tfidf = tfidf_loaded.transform([message])

    # Convert the sparse matrix to a dense format
    message_tfidf_dense = message_tfidf.toarray()

    # Predict using the loaded SVM model
    prediction = svm_loaded_model.predict(message_tfidf_dense)
    return st.warning("# Spam(Warning: This message is flagged as spam. Exercise caution.)") if prediction == 1 else st.info("# Not Spam(This message seems legitimate.)")

st.title('Machine Learning Mastery')
st.markdown('---')
col1, col2 = st.columns(2)
with col1:
    st.image('logo.jpg')
with col2:
    st.title('SMS Spam Detection')

st.markdown("---")
st.subheader('Introduction')
st.write(''' 
This Spam Detection App uses a Support Vector Machine (SVM) to classify SMS messages 
as spam or non-spam. The model is trained on a dataset of labeled messages, 
and after preprocessing (using TF-IDF), it learns to distinguish spam from 
non-spam based on patterns in the text.
When a user submits a message, the app predicts whether it's spam or not.
''')
st.markdown("---")
st.header('How The Support Vector Machines(SVM) Algorithm Works In Spam Detection')
st.write('''
In spam detection, SVM works by converting SMSs into feature vectors 
(e.g., word frequency, links). The algorithm then finds a decision boundary 
(hyperplane) that best separates spam from non-spam SMS. 
The support vectors are the data points closest to this boundary and help define it.
 Once trained, 
the model classifies new SMS messages based on which side of the boundary they fall.
''')
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.image('spamimg.jpg')
with col2:
    st.header('SMS Spam Detection using Support Vector Machines(SVM)')

# User input for the message to check
user_message = st.text_area('Enter the message to check:')

# Button to trigger prediction
if st.button('Submit'):
    if user_message:
        result = predict_spam(user_message)
        st.info(f'The message was analysed by SVM machine learning model and classification is based on past Data.So prediction made should also be reconsidered incase of misclassification')
    else:
        st.write('Please enter a message to check.')
