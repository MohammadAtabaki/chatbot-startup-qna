import streamlit as st
import pandas as pd
import spacy
from fuzzywuzzy import process
import seaborn as sns
import matplotlib.pyplot as plt

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

# File uploader
st.title("Smart Startup Chatbot")
uploaded_file = st.file_uploader("Upload Application Database.xlsx", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="Applications")
    st.write("✅ Dataset successfully loaded!")
    
    query = st.text_input("Ask a question:")

    if query:
        response = "Sorry, I don't have an answer for that."
        query = query.lower()

        # Extract keywords using NLP
        doc = nlp(query)
        keywords = [token.text for token in doc if token.is_alpha]  # Extract meaningful words

        # Match startup names
        matched_startup = process.extractOne(" ".join(keywords), df["Startup name"].str.lower().tolist())
        if matched_startup and matched_startup[1] > 80:  # Confidence threshold
            startup_data = df[df["Startup name"].str.lower() == matched_startup[0]]

            # Match closest column
            possible_questions = df.columns.tolist()
            matched_column = process.extractOne(query, possible_questions)

            if matched_column and matched_column[1] > 70:
                response = startup_data.iloc[0][matched_column[0]]

        st.write(response)
