import streamlit as st
import pickle


import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

tfidf = pickle.load(open('vectorizer','rb'))
model = pickle.load(open('model','rb'))

st.title("SMS/ Email spam classifier")

input_sms = st.text_imput("Enter the message")

nltk.download('punkt')
nltk.download('stopwords')


ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

#1)PREPROCESS
transformed_sms= transform_text(input_sms) 
#2)VECTORIZE
vector_input = tfidf.transform([transformed_sms])
#3)PREDICT
result = model.predict(vector_input)(0)
#4) DISPLAY

if result ==1:
    st.header('spam')

else:
    st.header('not spam')     