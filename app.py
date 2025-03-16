import streamlit as st
import pandas as pd
import spacy
from fuzzywuzzy import process
import seaborn as sns
import matplotlib.pyplot as plt

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Streamlit UI
st.title("Smart Startup Chatbot")

# File uploader
uploaded_file = st.file_uploader("Upload Application Database.xlsx", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="Applications")
    st.write("✅ Dataset successfully loaded!")

    query = st.text_input("Ask a question:")

    if query:
        response = "Sorry, I don't have an answer for that."
        query = query.lower()

        # Extract startup names
        matched_startup = process.extractOne(query, df["Startup name"].str.lower().tolist())

        if matched_startup and matched_startup[1] > 80:  # Confidence threshold
            startup_data = df[df["Startup name"].str.lower() == matched_startup[0]]

            # **Better Column Mapping**
            if "product" in query or "what does" in query:
                response = startup_data.iloc[0]["What is your company going to make? Please describe your product and what it does or will do."]
            elif "founders" in query:
                response = startup_data.iloc[0]["Founder Names"]
            elif "demo" in query:
                response = startup_data.iloc[0]["If\n you have a demo, what's the url? Demo can be anything that shows us how\n the product works. Usually that's a video or screen recording."]
            elif "pitch deck" in query:
                response = startup_data.iloc[0]["Any pitch deck? Please share"]
            elif "competitors" in query:
                response = startup_data.iloc[0]["Who are your competitors, and who might become competitors? Who do you fear most?"]
            elif "business model" in query or "money" in query:
                response = startup_data.iloc[0]["How do or will you make money? How much could you make?"]

        # **Handle Visualization Requests**
        elif "visualize" in query or "chart" in query:
            if "founders" in query:
                st.write("### Founders per Startup")
                plt.figure(figsize=(10, 5))
                sns.histplot(df["Founders #"], bins=10)
                st.pyplot(plt)
                response = "Here is a visualization of the number of founders per startup."

        st.write(response)
