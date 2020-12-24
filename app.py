# Core packages
# NLP packages
import nltk
import streamlit as st

from src.tf_idf import run_summarization_tf_idf
from src.word_frequency import run_summarization_wf

if __name__ == '__main__':
    nltk.download('punkt')
    nltk.download('stopwords')

    st.header("Text Summarization using TF-IDF")
    st.subheader("This app will summarize the long piece of input text in a few sentences")

    st.subheader("Paste your long text below:")
    text = st.text_area(label="Input text")
    if st.button("Summarize"):
        if text:
            summary_result = run_summarization_tf_idf(text)
            st.subheader("Using TF-IDF Algorithm:")
            st.success(summary_result)

            summary_result = run_summarization_wf(text)
            st.subheader("Using WordFrequency Algorithm:")
            st.success(summary_result)
        else:
            st.error("Please paste or write(!) some text")

