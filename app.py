import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

load_dotenv()

# Your API KEY must be saved securely!!
api_key: str | None = os.getenv(key="OPENAI_API_KEY")

# A prompt with defined template
title_template = PromptTemplate(
    input_variables=["topic"],
    template="Give me a medium article title on {topic}",
)

article_template = PromptTemplate(
    input_variables=[
        "article_title"
    ],  # article title is the output of `title_template`
    template="Give me a medium article for title {article_title}",
)

# OpenAI llm instance
# Temperature (0 = precision, 1 = creativity)
davinci_llm = OpenAI(model="text-davinci-003", temperature=0.9)  # type: ignore
gpt35_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
# example usage:
# response: str = openai_llm(title_template.format(topic=topic, language="English"))

# Chgin instance
title_chain = LLMChain(
    llm=davinci_llm, prompt=title_template, output_key="article_title", verbose=True
)
article_chain = LLMChain(llm=gpt35_turbo_llm, prompt=article_template, verbose=True)


st.title("Medium Article Generator")

topic: str = st.text_input(
    label="What's on your mind?", placeholder="Video games addiction"
)
language: str = st.text_input(label="What should be the language?", value="English")

if topic and language:
    overall_chain = SimpleSequentialChain(
        chains=[title_chain, article_chain], verbose=True
    )

    response = overall_chain.run(topic)
    st.write(response)
else:
    st.write(
        "Medium Article AI leverages ChatGPT language models (LLMs) to creatively craft and generate engaging articles, transforming the way content is produced and personalized."
    )
    st.write("Get started by typing in what's on your mind!")
