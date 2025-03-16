# Chatbot for Startup Data Querying and Visualization

## 1. Introduction
This report outlines the development of a chatbot that allows users to query startup-related information from a dataset and generate visualizations. The chatbot was built using **Streamlit** and **spaCy**, with additional support from **fuzzy matching** and **data visualization techniques**.

The goal of this project was to create a chatbot that can:
- Answer questions about startups (e.g., founders, product descriptions, competitors, and business models).
- Retrieve relevant links (e.g., demo links and pitch decks).
- Generate visualizations based on startup-related data (e.g., number of founders per startup).

You can test the chatbot here: [Chatbot Demo](https://chatbot-startup-qna-5cdds5ovfceybhzkj6mim2.streamlit.app/). **Please upload the Excel file inside the app to start querying the data.**

---

## 2. Technologies & Libraries Used
To develop the chatbot, I utilized the following technologies and libraries:

- **Streamlit**: Used to build an interactive web-based chatbot interface.
- **Pandas**: For handling and processing tabular data.
- **spaCy**: A Natural Language Processing (NLP) library used to extract keywords from user queries.
- **FuzzyWuzzy**: For fuzzy string matching, helping to improve query accuracy.
- **Matplotlib & Seaborn**: For generating visualizations such as histograms.
- **OpenPyXL**: To read `.xlsx` files uploaded by users.

---

## 3. Methods Used

### 3.1 Data Preprocessing
The dataset provided contained startup information, including founder names, product descriptions, and business models. Before using it, I:
- **Loaded the dataset** using `pandas.read_excel()`.
- **Standardized column names** to ensure consistency in querying.

### 3.2 Query Processing
To correctly interpret user questions, I used **Natural Language Processing (NLP)** with **spaCy**. The process involved:
- Tokenizing user input.
- Extracting key terms.
- Matching extracted terms with **startup names** and **dataset columns**.

For improved query flexibility, I also applied **fuzzy matching** with **FuzzyWuzzy**, which allows the chatbot to find the most relevant startup or field even if the user's input is not perfectly accurate.

### 3.3 Answering User Questions
To ensure accuracy, I implemented **explicit column mapping**, where:
- If the query is about a startup’s product, the chatbot retrieves information from the **Product Description** column.
- If the query is about founders, it extracts data from the **Founder Names** column.
- If the query asks for competitors, it retrieves information from the **Competitors** column.
- If the query involves demo links or pitch decks, it extracts URLs from the relevant columns.

### 3.4 Data Visualization
To allow users to request data visualizations, the chatbot detects keywords such as **"visualize"** and **"chart"**. 
- If a user asks for a visualization of founders, the chatbot generates a histogram using **Matplotlib** and **Seaborn** to show the distribution of founders across startups.

### 3.5 Deployment on Streamlit Cloud
The chatbot was deployed using **Streamlit Cloud**, requiring:
- A `requirements.txt` file to specify dependencies.
- Pre-installation of the `en_core_web_sm` model for **spaCy**.
- Modifications to ensure the chatbot runs smoothly in a cloud environment without local installations.

---

## 4. Challenges & Solutions

| **Challenge** | **Solution Implemented** |
|--------------|-------------------------|
| Incorrect answers due to fuzzy matching | Implemented explicit column mapping for specific queries |
| Missing `spaCy` model on deployment | Pre-installed `en_core_web_sm` via `requirements.txt` |
| Streamlit not supporting file access | Used Streamlit’s `file_uploader` to manually upload datasets |
| Visualization requests not recognized | Added logic to detect "visualize" or "chart" in user queries |

---

## 5. Sample Questions for Testing
Here are some example queries to test the chatbot:

### Basic Information Retrieval
- *What is Dropbox’s product?*
- *What does GitLab do?*
- *Describe Buffer’s business model.*

### Founder & Team Queries
- *Who are the founders of Mixpanel?*
- *How many founders does Cruise have?*

### Links & Pitch Decks
- *What is the demo link for GitLab?*
- *Does Dropbox have a pitch deck?*

### Competitors & Market
- *Who are the competitors of Cruise?*
- *What makes Mixpanel different from its competitors?*

### Revenue & Business Model
- *How does Dropbox make money?*
- *What is GitLab’s revenue model?*

### Visualization Requests
- *Visualize number of founders.*
- *Show a chart of founders per startup.*
