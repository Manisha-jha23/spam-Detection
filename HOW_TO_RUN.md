# 🚀 How to Run This Project in VS Code

## Quick Start Guide

### Method 1: Run in VS Code Terminal (Recommended)

1. **Open VS Code** in your project folder
2. **Open Terminal**:
   - Press `Ctrl + ~` (backtick)
   - Or go to `Terminal → New Terminal`
3. **Make sure you're in the right directory**:
   ```powershell
   cd "C:\Users\Manisha\OneDrive\Attachments\Desktop\coding1\spam detection"
   ```
4. **Install dependencies** (if not already installed):
   ```powershell
   pip install -r requirements.txt
   ```
5. **Run the script**:
   ```powershell
   python spam_detection.py
   ```

### Method 2: Run Using Play Button in VS Code

1. **Open** `spam_detection.py` in VS Code
2. **Click the Play Button** (▶️) in the top-right corner
3. If you see a Python interpreter selection, choose your Python installation
4. The script will run automatically!

### Method 3: Using Run Configuration

1. Press `F5` or go to `Run → Start Debugging`
2. Select "Python File" when prompted
3. The debugger will start and run your file

### Method 4: Right-Click Menu

1. **Right-click** on `spam_detection.py` in the file explorer
2. Select **"Run Python File in Terminal"**
3. Watch the magic happen! ✨

## 🎨 Run the WEB VERSION (Interactive UI)

### Run Streamlit Web App

1. **Install Streamlit** (if not installed):
   ```powershell
   pip install streamlit
   ```

2. **Run the web app**:
   ```powershell
   streamlit run spam_detection_web.py
   ```

3. **Your browser will automatically open** with the web interface!

4. **Type messages** in the text box and click "Check Message"

5. **To stop**: Press `Ctrl + C` in the terminal

### What's Different?

**Terminal Version** (`spam_detection.py`):
- Runs in command line
- Type messages directly
- Good for quick testing
- Type 'quit' to exit

**Web Version** (`spam_detection_web.py`):
- Beautiful web interface
- Visual feedback
- Progress bars
- Example messages included
- Better for demos!

## ✅ Expected Output

### Terminal Version:
```
✅ Model Trained Successfully!
📊 Accuracy: 0.98XX

==========================================================

🔍 SPAM DETECTION - Enter your message to check
==========================================================
Type 'quit' or 'exit' to stop

💬 Enter your message: Win a free iPhone!
🟢 NOT SPAM
📈 Confidence: 98.45%
```

### Web Version:
Opens in browser with:
- Text input box
- Check button
- Color-coded results
- Confidence percentages
- Progress bars

## 🔧 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'pandas'"
**Solution**: Install dependencies
```powershell
pip install -r requirements.txt
```

### Error: "No such file: spam.csv"
**Solution**: Make sure `spam.csv` is in the same folder as the Python files

### Error: Python not recognized
**Solution**: Install Python from [python.org](https://www.python.org/downloads/)

### Error: "streamlit: command not found"
**Solution**: 
```powershell
pip install streamlit
```

### Web app shows "FileNotFoundError: spam.csv"
**Solution**: Make sure you run the command from the project folder

## 🎯 Quick Tips

- **First time?** Try the web version - it's more user-friendly!
- **Want to see code execution?** Use the terminal version
- **Want to share with others?** Deploy the web version to Streamlit Cloud
- **Port already in use?** Streamlit will ask to use a different port

## 📚 What the Scripts Do

1. Loads your spam dataset
2. Cleans and preprocesses the text
3. Trains a Naive Bayes classifier
4. Shows model accuracy
5. **Waits for YOUR input** to predict spam!

## 🌐 Deploy to Web (Optional)

Want to share your app online? Deploy to Streamlit Cloud:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy!
5. Share your live website URL!

Enjoy running your spam detection project! 🎉
