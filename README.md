 SMS Spam Detection Classifier

A machine learning project to classify SMS messages as 'ham'or spam' 

***

## ✨ Features

Data Analysis & Training:Full data cleaning, Exploratory Data Analysis (EDA), and model training pipeline in a Jupyter Notebook (`sms-spam-detection.ipynb`).
Text Preprocessing:Implements a custom text transformation pipeline including lowercasing, tokenization, punctuation/stopword removal, and **Porter Stemming**.
Model Deployment: A user-friendly web application for instant classification, built with **Streamlit**.
Vectorization:** Uses a **TF-IDF Vectorizer** for converting text data into numerical features.

***

## ⚙️ Technology Stack

The project is built entirely in Python and relies on the following key libraries:

* **Programming Language:** Python
* **Data Handling:** `pandas`, `numpy`
* **NLP/Preprocessing:** `nltk` (for tokenization, stopwords, and stemming)
* **Machine Learning:** `scikit-learn` (`sklearn`) (for model training, `LabelEncoder`, and TF-IDF)
* **Web Application:** `streamlit`
* **Serialization:** `pickle` (to save and load the model and vectorizer)

***

## 📁 Repository Structure

The core files of this repository should include:
├── sms-spam-detection.ipynb   # Jupyter notebook containing the full ML pipeline
├── app.py                     # Streamlit web application script
├── spam.csv                   # The raw dataset used for training
├── vectorizer.pkl             # Pickled TF-IDF vectorizer object
└── model.pkl                  # Pickled trained classification model object (e.g., Naive Bayes, SVM, etc. - inferred from NLP task)

***

## Installation and Setup

## 1. Clone the Repository

bash
git clone <your-repo-link>
cd sms-spam-detection-repo

2. Install Dependencies
It is highly recommended to use a virtual environment.

Create a requirements.txt file (you will need to create this file) with the following content:
streamlit>=1.37.1
pandas>=2.2.2
numpy>=1.26.4
scikit-learn>=1.5.1
nltk>=3.9.1

Then, install the required packages:

Bash
pip install -r requirements.txt

3. Download NLTK Resources
The app.py script requires specific NLTK data resources for preprocessing. You can install them by running these commands in a Python interpreter or ensuring they are run before deployment:

Python

import nltk
nltk.download('punkt')
nltk.download('stopwords')
💻 Usage
Running the Web Application
Start the Streamlit application from your terminal:

Bash

streamlit run app.py
