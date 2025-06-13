import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
import os

# Set API key directly (optional if already in env variable)
os.environ["GOOGLE_API_KEY"] = "AIzaSyADh8pKp_qFmoJxh53JHU7MfiFkBDwwiRU"  # Replace with your actual key

# Streamlit UI setup
st.set_page_config(page_title="English to French Translator", layout="centered")
st.title("🌍 English to French Translator")

# Input field
input_text = st.text_input("Enter an English sentence:", "")

# Button to trigger translation
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        try:
            # Initialize Gemini model via LangChain
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

            # Define prompt template
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant that translates English to French."),
                ("user", "Translate this sentence to French: {sentence}")
            ])

            # Chain prompt with LLM
            chain: Runnable = prompt | llm

            # Run the chain
            result = chain.invoke({"sentence": input_text})

            # Extract and display the result
            translation = result.content if hasattr(result, 'content') else str(result)
            st.success("Translation complete! 🇫🇷")
            st.write("**French Translation:**")
            st.write(translation)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
