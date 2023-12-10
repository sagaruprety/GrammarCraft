from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.text_splitter import CharacterTextSplitter

# Function to generate a response focusing on grammar improvement only
def generate_response_grammar_only(text: str, openai_api_key: str) -> str:
    sample_text = "I goed to the store yesterday and buyed some apples. Then, me and my friend eated them at the park. It was a funner day!"
    template = """The following text is written by a non-native English speaker. Your task as a helpful assistant
    is to correct the grammar of the text and return only the corrected text. The meaning of the text should never be changed.
    Text: {text}
    """
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    chain = prompt | model | StrOutputParser()
    output = chain.invoke({"text": text})
    return output

# Function to generate a response focusing on grammar and style improvement
def generate_response_grammar_style(text: str, openai_api_key: str) -> str:
    sample_text = "I goed to the store yesterday and buyed some apples. Then, me and my friend eated them at the park. It was a funner day!"
    template = """The following text is written by a non-native English speaker. Your task as a helpful assistant
    is to correct the grammar of the text and also help improve the style of written English, if possible. The meaning of the text should never be changed.
    Text: {text}
    """
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    chain = prompt | model | StrOutputParser()
    output = chain.invoke({"text": text})
    return output

# Function to generate a summarized response
def generate_response_summarise(text: str, openai_api_key: str) -> str:
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    text_splitter = CharacterTextSplitter(
        separator=" ",
        chunk_size=1000,
        chunk_overlap=100
    )
    texts = text_splitter.create_documents([text])

    prompt_template = """The following text is written by a non-native English speaker. Your task as a helpful assistant
    is to summarize the text in less than 100 words. Remember that since it is written by a non-native English speaker, there might be some
    inconsistency in the language. Keep that in mind. The summary should cover all the key facts mentioned in the text.
    Text: {text}

    CONCISE SUMMARY:"""

    base_prompt = PromptTemplate(template=prompt_template, 
                        input_variables=["text"])

    if len(text.split()) < 500:
        print('stuff')
        chain = StuffDocumentsChain(llm_chain=LLMChain(llm=model, prompt=base_prompt),
                                    document_variable_name="text")
    else:
        # only for longer texts
        refine_template = (
            "Your job is to produce a final summary\n"
            "We have provided an existing summary up to a certain point: {existing_answer}\n"
            "We have the opportunity to refine the existing summary"
            "(only if needed) with some more context below.\n"
            "------------\n"
            "{text}\n"
            "------------\n"
            "Given the new context, refine the original summary"
            "If the context isn't useful, return the original summary."
        )
        refine_prompt = PromptTemplate(
            input_variables=["existing_answer", "text"],
            template=refine_template,
        )
        chain = load_summarize_chain(model, 
                                chain_type="refine", 
                                return_intermediate_steps=False, 
                                question_prompt=base_prompt, 
                                refine_prompt=refine_prompt)

        print('refine')

    output = chain.run(texts)

    return output
