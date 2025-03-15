import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Startup Q&A Chatbot")

# File uploader for the dataset
uploaded_file = st.file_uploader("Upload Application Database.xlsx", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="Applications")
    st.write("Dataset successfully loaded!")


    query = st.text_input("Ask a question about a startup:")

    if uploaded_file is not None and query:
        response = "Sorry, I don't have an answer for that."

    # Convert input to lowercase for better matching
        query = query.lower()

    # Extracting startup name if it exists in dataset
        startup_names = df["Startup name"].str.lower().tolist()
        matched_startup = None

        for name in startup_names:
            if name in query:
                matched_startup = name
                break

        if matched_startup:
            startup_data = df[df["Startup name"].str.lower() == matched_startup]

            if "what does" in query:
                response = startup_data.iloc[0]["What is your company going to make? Please describe your product and what it does or will do."]

            elif "founders of" in query:
                response = startup_data.iloc[0]["Founder Names"]

            elif "demo link" in query:
                response = startup_data.iloc[0]["If\n you have a demo, what's the url? Demo can be anything that shows us how\n the product works. Usually that's a video or screen recording."]

            elif "pitch deck" in query:
                response = startup_data.iloc[0]["Any pitch deck? Please share"]

        st.write(response)

else:
    st.write("Please upload the dataset to start using the chatbot.")
