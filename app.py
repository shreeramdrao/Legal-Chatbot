import os
import streamlit as st
from utils.query_agent import QueryAgent
from utils.summarization import SummarizationAgent

# 🔑 Hardcoded OpenAI API Key (Replace with your actual key)
API_KEY = st.secrets["OPENAI_API_KEY"]  # Store it for other modules

#If You want to run In Local then enter your API here
#API_KEY = "your-api-key-here"
#os.environ["OPENAI_API_KEY"] = API_KEY

# Streamlit UI Setup
st.set_page_config(page_title="Legal Chatbot", layout="wide")
st.title("⚖️ Legal AI Chatbot")
st.write("Ask legal questions related to **Indian Litigation & Corporate Laws**.")

# Load PDFs
pdf_paths = {
    "Guide to Litigation in India": "data/Guide-to-Litigation-in-India.pdf",
    "Legal Compliance & Corporate Laws": "data/Legal-Compliance-Corporate-Laws.pdf"
}

class LegalChatbot:
    """Multi-agent chatbot for answering legal queries."""
    
    def __init__(self, pdf_paths):
        self.query_agents = {name: QueryAgent(path, name) for name, path in pdf_paths.items()}
        self.summarizer = SummarizationAgent()

    def answer_query(self, query):
        """Finds the best legal answer by searching each PDF separately."""
        best_answer = None
        best_source = None
        best_score = 0

        for name, agent in self.query_agents.items():
            retrieved_text = agent.get_relevant_text(query)
            if retrieved_text:
                summary = self.summarizer.summarize(retrieved_text)
                score = len(retrieved_text)  # More retrieved text = more relevance
                if score > best_score:
                    best_score = score
                    best_answer = summary
                    best_source = name

        if best_answer:
            return f"""
            📖 **Source:** {best_source}

            💡 **Answer:**
            {best_answer}
            """
        else:
            return "❌ No relevant legal information found."

# Initialize chatbot
bot = LegalChatbot(pdf_paths)

# Streamlit UI Interaction
query = st.text_input("📝 Enter your legal question:")
if st.button("Ask"):
    if query:
        with st.spinner("🔍 Searching..."):
            response = bot.answer_query(query)
            st.write(response)
    else:
        st.warning("⚠️ Please enter a question!")