import openai
import streamlit as st
import os
from dotenv import load_dotenv

# โหลดตัวแปรจาก .env (ถ้ามี)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  

st.title("AI Knowledge Generator")

program_name = st.text_input("Enter the undergraduate program name (e.g., B.Sc. in Computer Science):")

if program_name:
    prompt = f"Define subject-specific knowledge for {program_name}. Classify it into: Factual, Conceptual, and Procedural Knowledge."
    
    if st.button("Generate"):
        with st.spinner("Generating..."):
            client = openai.OpenAI()  
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are an expert academic advisor."},
                          {"role": "user", "content": prompt}],
                temperature=0.7
            )
            st.markdown(response.choices[0].message.content)
