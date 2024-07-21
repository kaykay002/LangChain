#libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
from dotenv import load_dotenv
import os


#Environment variables loaded
load_dotenv()

#LangSmith Tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template -- Tells how chatbot behaves!
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"), #msg to system
        ("user","Question:{question}") #how user should input
    ]
)

# Streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("How should I assist you today ?")

# Ollama LLAMA2 LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser #chat prompt --> goes to llm --> output

if input_text:
    st.write(chain.invoke({"question":input_text}))