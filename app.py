import streamlit as st
from agents.api_agent import get_asia_tech_exposure
from agents.language_agent import generate_market_brief
from agents.retriever_agent import retrieve_relevant_docs
from agents.scraping_agent import scrape_earnings_news
from agents.voice_agent import speak_text
import os

ASIA_TECH_TICKERS = ["TSM", "005930.KS"]  # TSMC, Samsung


def handle_query_custom(question):
    exposure = get_asia_tech_exposure(ASIA_TECH_TICKERS)
    earnings = scrape_earnings_news()
    related_docs = retrieve_relevant_docs(question)

    # Combine all relevant data into a prompt
    brief = generate_market_brief({
        "question": question,
        "exposure": exposure,
        "retrieved_docs": related_docs
    }, earnings)

    speak_text(brief)
    return brief

st.title("📈 Morning Market Brief Assistant")

# New user input box
user_input = st.text_input("Ask a financial question:", value="What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?")

st.title("Finance Assistant")
if st.button("Ask Agent"):
    with st.spinner("Thinking..."):
        result = handle_query_custom(user_input)  # result = Gemini's full response
        st.success("Here's your market brief:")
        st.speak_text("assistant").write(result)


