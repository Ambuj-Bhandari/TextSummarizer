import streamlit as st
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

st.title("Text Summarizer App")

st.set_page_config(layout="wide")

col1, col2  = st.columns(2)

with col1:
    st.header("Input Text")
    input_text = st.text_area(
        "Paste or Enter your Text here...",
        #width= 800,
        height=300,
        key = "input_text"
    )

with col2:
    st.header("Summary")
    summarized_text = st.empty()

if st.button("Summarize"):
    if input_text:
        obj = PredictionPipeline()
        summary = obj.predict(input_text)
        summarized_text.text_area(
            "Summarized Text will appear here...",
            value = summary,
            height = 300,
            key = "output_text"
        )
    else:
        summarized_text.text_area(
            "Summarized Text will appear here...",
            value = "Input Text is Empty...",
            height = 300,
            key = "output_text"
        )