import streamlit as st
import spacy
from spacy import displacy
import en_core_web_sm
from newspaper import Article

# Load English language model
nlp = en_core_web_sm.load()

# Set the title of the Streamlit app
st.title("Named Entity Recognizer")

# Display an informational message to the user
st.info("This app extracts named entities from the input provided by the user.")

# Text area for entering a paragraph
text1 = st.text_area("Enter a paragraph")

# Text area for entering a URL
text2 = st.text_area("Enter the URL of an article")

# Check if the "Submit" button is clicked
if st.button("Submit"):
    # If the user input text directly
    if text1:  
        doc = nlp(text1)
    # If the user input a URL
    else:
        # Download and parse the article
        article = Article(text2)
        article.download()
        article.parse()
        
        # Process the text using the NLP pipeline
        doc = nlp(article.text)
    
    # Render named entities and display the visualization
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)
