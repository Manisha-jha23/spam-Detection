# 📚 GitHub Setup Guide

## Step-by-Step Guide to Add Your Project to GitHub with Website URL

### 1️⃣ Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit: Spam Detection Project"
```

### 2️⃣ Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name it: `spam-detection` (or your preferred name)
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### 3️⃣ Connect Local Repository to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/spam-detection.git
git branch -M main
git push -u origin main
```

### 4️⃣ Adding Website URL (Multiple Options)

#### Option A: In Repository Settings (Settings → Pages)
1. Go to your GitHub repository
2. Click "Settings" tab
3. Scroll down to "Pages" section
4. Select branch (usually `main`) and folder (usually `/root`)
5. Click "Save"
6. Your site will be available at: `https://YOUR_USERNAME.github.io/spam-detection`

#### Option B: In Repository About Section
1. Go to your repository main page
2. Click the gear icon (⚙️) next to "About"
3. Check "Website" checkbox
4. Enter your website URL (e.g., `https://your-deployed-app.herokuapp.com`)
5. Click "Save"

#### Option C: Add to README.md (Already Done!)
I've already added a placeholder in your README.md file. Update it with your actual URL.

### 5️⃣ Deploy Your Project as a Website

#### Using Heroku:
```bash
pip install streamlit
# Create a streamlit web app
heroku create your-app-name
git push heroku main
```

#### Using Streamlit Cloud:
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub repository
3. Auto-deploy

#### Using PythonAnywhere:
1. Upload your files via web interface
2. Configure web app
3. Get your URL

#### Using Netlify/Vercel:
For Python projects, you'll need to:
1. Create a web framework (Flask/Streamlit)
2. Build static files or use Docker
3. Deploy

### 6️⃣ Update README.md
Replace these placeholders in `README.md`:
- `YOUR_USERNAME` → Your actual GitHub username
- `https://your-website-url.com` → Your deployed website URL
- `Your Name` → Your actual name

### 7️⃣ Optional: Add License
```bash
# Create MIT License file
echo "" > LICENSE
# Add license text from: https://choosealicense.com/licenses/mit/
```

## 🎯 Quick Checklist
- [x] Git repository initialized ✅
- [x] Files committed locally ✅
- [ ] GitHub repository created (Next step!)
- [ ] Remote origin added and pushed
- [ ] Website deployed and URL obtained
- [ ] README.md updated with actual URLs
- [ ] Website link added in GitHub Pages or About section
- [ ] License file added (optional)

## 📝 Next Steps
1. Deploy your spam detection model as a web app
2. Add the deployment URL to your repository
3. Consider adding badges, screenshots, and more documentation

## 🆘 Need Help?
- [GitHub Documentation](https://docs.github.com)
- [GitHub Pages Guide](https://docs.github.com/en/pages)
- [Python Deployment Guide](https://realpython.com/python-web-applications/)

