# 📧 Spam Detection Web App with Streamlit

import streamlit as st
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Page configuration
st.set_page_config(
    page_title="Spam Detection App",
    page_icon="📧",
    layout="centered"
)

# Title and description
st.title("📧 Spam Detection App")
st.markdown("**Detect spam messages using Machine Learning!**")
st.markdown("---")

# Load and train model (cache it so it doesn't retrain every time)
@st.cache_resource
def train_model():
    # Load dataset
    data = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
    data.columns = ['label', 'message']
    
    # Convert labels to numeric
    data['label_num'] = data['label'].map({'ham': 0, 'spam': 1})
    
    # Clean text
    def clean_text(text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text
    
    data['message'] = data['message'].apply(clean_text)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        data['message'], data['label_num'], test_size=0.2, random_state=42
    )
    
    # Vectorize
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train model
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    
    # Get accuracy
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, vectorizer, accuracy

# Train model
model, vectorizer, accuracy = train_model()

# Display accuracy in sidebar
with st.sidebar:
    st.header("📊 Model Info")
    st.metric("Accuracy", f"{accuracy:.1%}")
    st.markdown("---")
    st.markdown("**How to use:**")
    st.markdown("1. Type your message")
    st.markdown("2. Click 'Check Message'")
    st.markdown("3. View the result!")

# Main input area
st.subheader("🔍 Enter Your Message")

# Text input
user_message = st.text_area(
    "Type the message you want to check:",
    height=100,
    placeholder="e.g., Free! Click here to win a million dollars!!!"
)

# Check button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    check_button = st.button("🔍 Check Message", type="primary", use_container_width=True)

# Process when button is clicked
if check_button:
    if not user_message.strip():
        st.warning("⚠️ Please enter a message to check!")
    else:
        # Preprocess
        cleaned_msg = user_message.lower()
        cleaned_msg = cleaned_msg.translate(str.maketrans('', '', string.punctuation))
        
        # Predict
        test_msg_tfidf = vectorizer.transform([cleaned_msg])
        pred = model.predict(test_msg_tfidf)
        prob = model.predict_proba(test_msg_tfidf)[0]
        
        # Display result
        st.markdown("---")
        
        if pred[0] == 1:
            st.error("🔴 **SPAM DETECTED!**")
            st.markdown(f"**Confidence:** {prob[1]*100:.2f}%")
            st.markdown("⚠️ This message appears to be spam!")
        else:
            st.success("🟢 **NOT SPAM**")
            st.markdown(f"**Confidence:** {prob[0]*100:.2f}%")
            st.markdown("✅ This message looks legitimate!")
        
        # Progress bars
        st.markdown("**Probability Breakdown:**")
        col1, col2 = st.columns(2)
        
        with col1:
            st.progress(prob[0])
            st.caption(f"Not Spam: {prob[0]*100:.1f}%")
        
        with col2:
            st.progress(prob[1])
            st.caption(f"Spam: {prob[1]*100:.1f}%")

# Example messages
with st.expander("💡 Example Messages to Try"):
    st.markdown("**Spam Examples:**")
    st.code("""
    - "Win a free iPhone! Click here now!!!"
    - "Congratulations! You've won $1000. Claim your prize!"
    - "URGENT: Your account will be closed. Verify now."
    """)
    
    st.markdown("**Not Spam Examples:**")
    st.code("""
    - "Hey, are we meeting tomorrow?"
    - "Thanks for your help today!"
    - "Can we reschedule to next week?"
    """)

# Footer
st.markdown("---")
st.markdown("**Made with ❤️ using Streamlit and Machine Learning**")

