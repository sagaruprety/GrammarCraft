import streamlit as st
from agent import generate_response_grammar_only, generate_response_grammar_style, generate_response_summarise
from evaluation import evaluate_output

# Function to improve grammar using the LLM English Improvement Agent
def improve_grammar(text: str, open_api_key: str) -> str:
    return generate_response_grammar_only(text, open_api_key)

# Function to improve grammar and style using the LLM English Improvement Agent
def improve_grammar_and_style(text: str, open_api_key: str) -> str:
    return generate_response_grammar_style(text, open_api_key)

# Function to summarize text using the LLM English Improvement Agent
def summarise(text: str, open_api_key: str) -> str:
    return generate_response_summarise(text, open_api_key)

# Main function to run the Streamlit app
def main():
    st.title("LLM English Improvement Agent")

    # User inputs OpenAI API Key in the sidebar
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

    # User selects an option
    option = st.radio("Select an option:", ["Only improve grammar", "Improve grammar and style", "Only summarise text"])

    # User inputs text
    user_input = st.text_input("Enter your text:")

    # User clicks the "Submit" button
    if st.button("Submit"):
        if option == "Only improve grammar":
            st.write("You selected Option 1: Only improve grammar")
            response = improve_grammar(user_input, openai_api_key)
            st.markdown("Grammar improvement by English Agent: " + response)

        elif option == "Improve grammar and style":
            st.write("You selected Option 2: Improve grammar and style")
            response = improve_grammar_and_style(user_input, openai_api_key)
            st.markdown("Grammar plus style improvement by English Agent: " + response)

        elif option == "Only summarise text":
            st.write("You selected Option 3: Only summarise text")
            response = summarise(user_input, openai_api_key)
            st.markdown("Summary by English Agent: " + response)

        # Evaluate the output using a superior agent
        eval_result = evaluate_output(option, user_input, response, openai_api_key)
        st.markdown("Evaluation by superior agent: " + str(eval_result))

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
