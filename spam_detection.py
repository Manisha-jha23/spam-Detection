# 📧 Spam Detection Project

# Step 1: Import libraries
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load dataset
# Make sure you have the file 'spam.csv' in your working directory
# You can rename your downloaded dataset to spam.csv
data = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
data.columns = ['label', 'message']

# Step 3: Convert labels to numeric (ham=0, spam=1)
data['label_num'] = data['label'].map({'ham': 0, 'spam': 1})

# Step 4: Text preprocessing
def clean_text(text):
    text = text.lower()  # lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    return text

data['message'] = data['message'].apply(clean_text)

# Step 5: Split data
X_train, X_test, y_train, y_test = train_test_split(
    data['message'], data['label_num'], test_size=0.2, random_state=42
)

# Step 6: Convert text to numerical form (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Step 7: Train model (Naive Bayes)
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Step 8: Predict and evaluate
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
print("✅ Model Trained Successfully!")
print("📊 Accuracy:", accuracy)
print("\n" + "="*60)

# Step 9: Interactive user input
print("\n🔍 SPAM DETECTION - Enter your message to check")
print("="*60)
print("Type 'quit' or 'exit' to stop\n")

while True:
    user_message = input("\n💬 Enter your message: ")
    
    if user_message.lower() in ['quit', 'exit']:
        print("\n👋 Thanks for using Spam Detection!")
        break
    
    if not user_message.strip():
        print("⚠️  Please enter a message!")
        continue
    
    # Predict
    test_msg = [user_message]
    test_msg_tfidf = vectorizer.transform(test_msg)
    pred = model.predict(test_msg_tfidf)
    
    # Get probability
    prob = model.predict_proba(test_msg_tfidf)[0]
    
    # Display result
    result = "🔴 SPAM" if pred[0] == 1 else "🟢 NOT SPAM"
    confidence = prob[pred[0]] * 100
    
    print(f"\n{result}")
    print(f"📈 Confidence: {confidence:.2f}%")
    
    if pred[0] == 0:
        print(f"   Spam probability: {prob[1]*100:.2f}%")
    else:
        print(f"   Ham probability: {prob[0]*100:.2f}%")
