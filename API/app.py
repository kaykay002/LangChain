from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from  langchain_community.llms import Ollama
from  dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"

)

##ollama llama2
llm=Ollama(model="llama2")

prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 year old child with 100 words")


add_routes(
    app,
    prompt2|llm,
    path="/poem")


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
