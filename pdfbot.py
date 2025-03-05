import os
import faiss
import dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load API key from .env file or ask user
dotenv.load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    API_KEY = input("🔑 Enter your OpenAI API Key: ").strip()
    os.environ["OPENAI_API_KEY"] = API_KEY  # Store temporarily for runtime

class QueryAgent:
    """Retrieves relevant legal information from PDFs."""
    
    def __init__(self, pdf_path, name):
        self.pdf_path = pdf_path
        self.name = name
        self.embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
        self.vectorstore = self._create_vectorstore()
        self.retriever = self.vectorstore.as_retriever()

    def _create_vectorstore(self):
        """Loads the PDF, splits text, and stores it in FAISS vector database."""
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = text_splitter.split_documents(documents)

        vectorstore = FAISS.from_documents(texts, self.embeddings)
        return vectorstore

    def get_relevant_text(self, query):
        """Retrieves the most relevant legal information for a query."""
        docs = self.retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs]) if docs else None

class SummarizationAgent:
    """Summarizes complex legal information into simpler terms."""
    
    def __init__(self):
        self.llm = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

    def summarize(self, text):
        """Summarizes lengthy legal text into an easy-to-understand format."""
        if not text:
            return "❌ No relevant legal information found in the provided documents."
        
        prompt = f"Summarize the following legal text in simple terms:\n\n{text}"
        return self.llm.invoke(prompt)

class LegalChatbot:
    """Main chatbot handling legal queries across multiple PDFs."""
    
    def __init__(self, pdf_paths):
        self.query_agents = {name: QueryAgent(path, name) for name, path in pdf_paths.items()}
        self.summarizer = SummarizationAgent()

    def answer_question(self, query):
        """Finds the best legal answer by searching each PDF separately."""
        best_answer = None
        best_source = None
        best_score = 0

        for name, agent in self.query_agents.items():
            print(f"\n🔍 Searching in '{name}'...")
            retrieved_text = agent.get_relevant_text(query)
            if retrieved_text:
                summary = self.summarizer.summarize(retrieved_text)
                score = len(retrieved_text)  # More retrieved text = more relevance
                if score > best_score:
                    best_score = score
                    best_answer = summary
                    best_source = name

        if best_answer:
            return f"\n📖 **Source:** {best_source}\n\n💡 **Answer:**\n{best_answer}\n"
        else:
            return "❌ No relevant legal information found."

if __name__ == "__main__":
    pdf_paths = {
        "Guide to Litigation in India": "Guide-to-Litigation-in-India.pdf",
        "Legal Compliance & Corporate Laws": "Legal-Compliance-Corporate-Laws.pdf"
    }

    bot = LegalChatbot(pdf_paths)

    print("\n⚖️ **Welcome to the Legal Chatbot!** ⚖️")
    print("Ask legal questions based on Indian litigation & corporate laws.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("📝 Enter your question: ").strip()
        if query.lower() == "exit":
            print("\n👋 Goodbye! Stay legally informed.\n")
            break
        print(bot.answer_question(query))