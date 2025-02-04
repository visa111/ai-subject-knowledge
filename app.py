import openai
import streamlit as st
import os
from dotenv import load_dotenv

# โหลด API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ตรวจสอบว่า API Key ถูกต้อง
if not api_key:
    st.error("❌ OpenAI API Key ไม่ถูกต้อง กรุณาตั้งค่าใน environment variables!")
    st.stop()

# กำหนดค่า API Key ให้ OpenAI
client = openai.Client(api_key=api_key)  

# สร้าง Streamlit App
st.title("AI Subject Knowledge Generator")

program_name = st.text_input("Enter the undergraduate program name (e.g., B.Sc. in Computer Science):")

if program_name:
    prompt = (
        f"Define subject-specific knowledge for {program_name}. "
        "Classify it into: Factual, Conceptual, and Procedural Knowledge."
    )

    if st.button("Generate Knowledge"):
        with st.spinner("Generating..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "system", "content": "You are an expert academic advisor."},
                              {"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"🚨 Error: {e}")
