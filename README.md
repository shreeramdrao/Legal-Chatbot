# 📚 Legal Chatbot

## 🔄 Overview
**Legal Chatbot** is an AI-powered multi-agent chatbot designed to retrieve and summarize legal information from Indian litigation and corporate law documents. It helps users get clear and concise answers by fetching data from legal PDFs and simplifying complex legal language.

## 🌐 Live Demo
[Click here to use the chatbot](https://legal-chatbott.streamlit.app/)

## ⚖️ Features
- ✅ **Multi-Agent System**: Uses a **Query Agent** to retrieve legal text and a **Summarization Agent** to simplify responses.
- ✅ **Legal Document Search**: Fetches information from:
  - *Guide to Litigation in India*
  - *Legal Compliance & Corporate Laws*
- ✅ **Web Interface**: Built using **Streamlit** for easy interaction.
- ✅ **Accurate Responses**: Uses **FAISS for retrieval** and **GPT-based summarization**.
- ✅ **Secure API Handling**: OpenAI API key is securely stored in Streamlit secrets.

## 🔧 Tech Stack
- **Python** – Core programming language
- **LangChain & OpenAI API** – Query & Summarization Agents
- **FAISS** – Fast retrieval of legal text
- **PyPDF** – PDF text extraction
- **Streamlit** – Web UI framework

## 📁 Folder Structure
```
legal-chatbot/
│── app.py                 # 🌟 Main Streamlit App
│── requirements.txt        # 📀 Dependencies
│── data/                   📂 Store PDFs here
│   ├── Guide-to-Litigation-in-India.pdf
│   ├── Legal-Compliance-Corporate-Laws.pdf
│── utils/                  📂 Helper functions (Query & Summarization)
│   ├── query_agent.py
│   ├── summarization.py
│── README.md               # 📚 Project documentation
```

## ✨ Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/shreeramdrao/Legal-Chatbot.git
   cd Legal-Chatbot
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the chatbot locally**:
   ```bash
   streamlit run app.py
   ```

## 🚀 Deployment
The chatbot is deployed using **Streamlit Cloud**. To deploy your own version:
1. Push your repository to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and select your repo.
3. Set the main file as `app.py` and deploy.
4. Add the OpenAI API key under **Streamlit secrets**.

## ⚡ Future Enhancements
- 📉 **Improve Legal Accuracy**: Fine-tune a **custom LLM** trained on Indian legal texts.
- 📉 **Enhance UI**: Add **dropdown menus** for predefined legal topics.
- 📉 **Expand Data Sources**: Integrate **more legal PDFs** for better coverage.
- 📉 **Voice Support**: Allow **speech-to-text input** for accessibility.
- 📉 **Authentication System**: Restrict access to legal professionals (if required).

## 📊 Contributing
Feel free to submit **issues** or **pull requests** to improve the chatbot!

## 👤 Author
Developed by **Shreerama D S**

