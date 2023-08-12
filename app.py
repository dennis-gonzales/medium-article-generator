import os

import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

# Your API KEY must be saved securely!!
api_key: str | None = os.getenv(key="OPENAI_API_KEY")

# A prompt with defined template
title_template = PromptTemplate(
    input_variables=["topic", "language"],
    template="Give me a medium article title on {topic} in {language} language",
)

# OpenAI llm instance
# Temperature (0 = precision, 1 = creativity)
openai_llm = OpenAI(temperature=0.9)
# example usage:
# response: str = openai_llm(title_template.format(topic=topic, language="English"))

# Chgin instance
title_chain = LLMChain(llm=openai_llm, prompt=title_template, verbose=True)


st.title("Medium Article Generator")

topic: str = st.text_input(label="What's on your mind?")
language: str = st.text_input(label="What should be the language?")

if topic and language:
    response = title_chain.run({"topic": topic, "language": language})
    st.write(response)
