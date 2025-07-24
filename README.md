# 🧠 Chattrix – Streamlit Chatbot App

Chattrix is a simple and elegant AI chatbot interface built using **Streamlit** and powered by **Together.ai's MoonshotAI Kimi-K2-Instruct** model.
Want to visit the app click on --   https://app-chatbot-wkhvbvqyamdqmmjqmxzteb.streamlit.app/

---

## 🚀 Features

- 🤖 Conversational AI with natural responses
- 💬 Chat-style interface (You on the right, AI on the left)
- 📦 Lightweight and easy to deploy
- 🔐 API key-based access
- 🖼️ Clean and modern UI

---

## 📂 Project Structure

Streamlit-Chatbot/
│
├── app.py # Main Streamlit application
├── .gitignore # Git ignore rules
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🛠️ Setup Instructions (Local Development)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/chandu3678/Streamlit-Chatbot.git
cd Streamlit-Chatbot
2️⃣ Create a virtual environment
bash
Copy
Edit
python -m venv .hfapp
3️⃣ Activate the virtual environment
On Windows:

bash
Copy
Edit
.hfapp\Scripts\activate
On Mac/Linux:

bash
Copy
Edit
source .hfapp/bin/activate
4️⃣ Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 API Key Setup
This app uses Together.ai’s API to generate responses.

Get your free API key from: https://www.together.ai

Replace the API key in your app.py file:

python
Copy
Edit
API_KEY = "Bearer YOUR_API_KEY_HERE"
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
Then visit http://localhost:8501 in your browser.

📄 .gitignore
Make sure your .gitignore includes virtual environments and system files:

bash
Copy
Edit
# Python
__pycache__/
*.py[cod]
*.sqlite3
.env
*.env

# Streamlit
.streamlit/

# Virtual Environment
.hfapp/
.venv/

# OS
.DS_Store
Thumbs.db
🗃️ Git Commands (First Time Push)
If you're pushing to GitHub for the first time:

bash
Copy
Edit
git init
git remote add origin https://github.com/your-username/Streamlit-Chatbot.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
If you get a conflict or rejected push:

bash
Copy
Edit
git pull --rebase origin main
# Resolve conflicts if any
git add .
git rebase --continue
git push
👨‍💻 Author
Made with ❤️ by Chandra Shekhar
