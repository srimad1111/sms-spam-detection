# 📩 SMS Spam Detection Web App

A simple **Flask-based web app** that classifies SMS messages as **Spam** or **Not Spam** using NLP and machine learning.

---

## ⚙️ Features

* 🧠 **ML Model:** Trained with Multinomial Naive Bayes + TF-IDF
* 🔤 **Text Preprocessing:** Tokenization, stopword removal, stemming
* 💻 **Frontend:** HTML, CSS, JS (modern dark orb grid design)
* ⚡ **Instant Predictions:** Real-time classification via Flask API

---

## 🧱 Project Structure

```
sms-spam-detection/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── requirements.txt
```

---

## 🚀 How to Run

1️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

2️⃣ **Download NLTK data**

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

3️⃣ **Start the app**

```bash
python app.py
```

Then open 👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧰 Tech Stack

* **Backend:** Flask
* **ML/NLP:** scikit-learn, NLTK
* **Frontend:** HTML, CSS, JavaScript

---

## 🖼️ Example

| Message                              | Result     |
| ------------------------------------ | ---------- |
| “Congrats! You’ve won a free prize!” | 🚫 Spam    |
| “See you at 6pm!”                    | ✅ Not Spam |

---

## 🪪 Credits

Made with ❤️ by Srimad Snehasis 