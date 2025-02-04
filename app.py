import openai
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check API key
if not api_key:
    st.error("❌ OpenAI API Key is missing! Please set it in environment variables.")
    st.stop()

# Initialize OpenAI Client
client = openai.Client(api_key=api_key)

# 🎨 Set Page Config
st.set_page_config(page_title="AI Knowledge Generator", page_icon="📚", layout="wide")

# 🌟 Sidebar for App Info
st.sidebar.header("📌 About this App")
st.sidebar.write(
    "Enter an undergraduate program name, and this app will generate "
    "essential subject-specific knowledge categorized into:\n"
    "🔹 **Factual Knowledge**\n"
    "🔹 **Conceptual Knowledge**\n"
    "🔹 **Procedural Knowledge**"
)
st.sidebar.write("⚡ Powered by OpenAI GPT-4 🚀")

# 🎓 Main App
st.title("🎓 AI-Powered Subject Knowledge Generator")
st.write("**Get structured subject-specific knowledge instantly!**")

# 📌 User Input
program_name = st.text_input("Enter the undergraduate program name (e.g., B.Sc. in Computer Science):")

if program_name:
    prompt = (
        f"Define subject-specific knowledge for {program_name}. "
        "Classify it into:\n"
        "1️⃣ **Factual Knowledge** (Basic facts, terminology, and data)\n"
        "2️⃣ **Conceptual Knowledge** (Key theories and principles)\n"
        "3️⃣ **Procedural Knowledge** (Skills, processes, and methodologies)\n\n"
        "Provide structured insights for each category."
    )

    if st.button("🚀 Generate Knowledge Categories", help="Click to generate AI response"):
        with st.spinner("Generating response... ⏳"):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert academic advisor."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                
                ai_output = response.choices[0].message.content
                
                # 📝 Display Structured Output
                st.markdown("## 📚 **Generated Subject Knowledge**")
                
                # Formatting AI Response
                st.markdown("---")
                st.markdown("### **🔹 Factual Knowledge**")
                st.write(ai_output)  # You can split responses if structured
                
                st.markdown("### **🔹 Conceptual Knowledge**")
                st.write(ai_output)

                st.markdown("### **🔹 Procedural Knowledge**")
                st.write(ai_output)

            except Exception as e:
                st.error(f"🚨 Error: {e}")
