from flask import Flask, request, jsonify, render_template
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Ensure NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y = [ps.stem(i) for i in y]
    return " ".join(y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form.get('message', '')
    if not message:
        return jsonify({'result': 'error', 'message': 'No input provided'})
    
    transformed = transform_text(message)
    vector = tfidf.transform([transformed])
    prediction = model.predict(vector)[0]
    result = "spam" if prediction == 1 else "not spam"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
