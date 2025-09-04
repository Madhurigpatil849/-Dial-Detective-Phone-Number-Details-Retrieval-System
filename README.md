# Dial-Detective-Phone-Number-Details-Retrieval-System
AI-powered system for phone number validation, location &amp; carrier identification, and spam detection. Built with Python, Flask, and ML (KNN).

# 📱 Dial Detective: Phone Number Details Retrieval System

**Domain:** Cybersecurity / Fraud Detection | **Type:** Mini Project  
**Institute:** Usha Mittal Institute of Technology, SNDT Women’s University, Mumbai  

---

## 📖 Overview
**Dial Detective** is an intelligent phone number analysis system designed to:  
- Validate phone numbers 📞  
- Extract details like **location, carrier, and time zone** 🌍  
- Detect spam or fraudulent numbers 🤖  

Built using **Python (Phonenumbers library + ML KNN Classifier)** with a **Flask backend** and **web UI**, this project enhances fraud prevention, telecom security, and user verification.  

---

## 🚀 Project Highlights
🔍 Validates phone number authenticity  
🌍 Fetches location, carrier, and timezone info  
🤖 Classifies numbers as **spam or safe** using KNN  
⚡ Real-time analysis through web interface  
🔐 Useful for businesses, individuals & law enforcement  

---

## 🎯 Problem Statement
Fraudulent calls, phishing scams, and spoofed numbers are rising 📈.  
Existing solutions (e.g., **Truecaller**) face issues like **privacy risks, false spam reports, and dependency on internet databases**.  

✅ **Dial Detective** overcomes these by providing **AI-based detection + reliable validation** with higher transparency.  

---

## 🛠️ Technologies Used
- **Language:** Python  
- **Libraries:** Phonenumbers, Pandas, NumPy, Scikit-learn, Joblib  
- **Backend:** Flask  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Tools:** Jupyter Notebook, VS Code  

---

## 🧠 Implementation Details  
- **Dataset:** Self-created dataset (`spam_dataset.csv`) with labeled phone numbers (spam / not spam) and extracted features.  
- **Feature Engineering:** Extracted attributes like sum of digits, unique digit count, first digit frequency, country, and carrier info.  
- **Model Training:** Used **K-Nearest Neighbors (KNN)** with scikit-learn. Model trained on dataset, evaluated, and saved using Joblib for deployment.  
- **Backend & UI:** Flask backend processes numbers and returns results (validity, location, carrier, spam status) to a simple web interface.  

---

## 🖥️ User Interface
- **Input:** Enter phone number in international format (+91, +1, etc.)  
- **Output:** Location, Carrier, Timezone, Spam Status  

---

## 📊 Applications
- Spam/Fraud call detection 🚨  
- Customer phone validation for businesses 🏢  
- Caller location & network identification 🌍  
- Police & forensic investigations 👮‍♂️  
- Prevention of spoofed numbers & fake registrations 🔐  

---

## 🔮 Future Scope
- Deep learning models (LSTM, CNN) for spam detection  
- Real-time caller ID with live alerts  
- Global telecom database integration 🌍  
- Offline mode with local dataset  
- Mobile app development 📱  
- Voice/call pattern analysis for scam detection  

---

## 👩‍💻 Team Members
- Madhuri Patil (45)  
- Durva Patkar (47)  
- Vaishnavi Rawate (53)  

**Guided by:** Prof. Sumedh Pundkar  

---

## 📚 References
- IRJMETS – *Phone Number Tracking Using Python*, 2022  
- Quest Journals – *Phone Number Tracking System Using Python*, 2022  
- ACM CHI – *Phonenumbers: Parsing, Formatting, and Validating International Phone Numbers*, 2021  
- Scribd – *Phone Tracking Using Python*, 2022  

---

✨ *A mini-project submitted at **Usha Mittal Institute of Technology, SNDT Women’s University (2024-2025)** in partial fulfillment for the B.Tech in Computer Science & Technology.*  
