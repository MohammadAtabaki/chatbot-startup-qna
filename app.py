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

    query = st.text_input("Ask a question about a startup:")

    if query:
        response = "Sorry, I don't have an answer for that."

        if "what does" in query.lower():
            startup = query.split(" ")[2]
            result = df[df["Startup name"].str.lower() == startup.lower()]
            if not result.empty:
                response = result.iloc[0]["What is your company going to make? Please describe your product and what it does or will do."]

        elif "founders of" in query.lower():
            startup = query.split(" ")[-1]
            result = df[df["Startup name"].str.lower() == startup.lower()]
            if not result.empty:
                response = result.iloc[0]["Founder Names"]

        elif "chart of founders" in query.lower():
            st.write("### Founders per Startup")
            plt.figure(figsize=(10, 5))
            sns.histplot(df["Founders #"], bins=10)
            st.pyplot(plt)
            response = "Here is a visualization of the number of founders per startup."

        st.write(response)
else:
    st.write("Please upload the dataset to start using the chatbot.")
