from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


def generate_response(text):


    sample_text = "I goed to the store yesterday and buyed some apples. Then, me and my friend eated them at the park. It was a funner day!"
    template = """The following text is written by a non-native english speaker. Your task as a helpful assistant
    is to correct the grammar of the text and return only the corrected text. The meaning of the text should never be changed.
    Text: {text}
    """

    prompt = ChatPromptTemplate.from_template(template)

    model =  ChatOpenAI(model = "gpt-3.5-turbo")

    chain = prompt| model| StrOutputParser()

    output = chain.invoke(
        {
        "text": text
        },
    )

    print(output)
    return output