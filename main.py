from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


template = """Summarise the following text based on the context:

Text: {text}

Context: {context}

"""

prompt = ChatPromptTemplate.from_template(template)

model =  ChatOpenAI(model = "gpt-3.5-turbo")

chain = prompt| model| StrOutputParser

chain.invoke(
    "text": 
)