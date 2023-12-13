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

def print_scores(task_metric_scores: dict):
    """
    Print relevant metric scores based on the specified task type.

    Parameters:
    - task_metric_scores (list of dict): A list of dictionaries containing task, metric names and their corresponding scores.

    Prints:
    - Prints metric scores based on the task type. For 'Improve grammar', prints Fluency score.
      For 'Summarisation', prints Relevance and Coherence scores. For 'Improve grammar and style',
      prints Fluency and Consistency scores.
    """
    task_type = task_metric_scores['Task Type']
    metric_scores = task_metric_scores['metric_score']
    for metric in metric_scores:
        metric_name = list(metric.keys())[0]
        metric_value = list(metric.values())[0]

        if task_type == 'Improve grammar':
            if metric_name == 'Fluency':
                return(f"{metric_name}: {metric_value}/3")
        elif task_type == 'Summarise text':
            if metric_name in ['Relevance', 'Coherence']:
                return(f"{metric_name}: {metric_value}/5")
        elif task_type == 'Improve both grammar and style':
            if metric_name in ['Fluency', 'Consistency']:
                return(f"{metric_name}: {metric_value}/5")


# Main function to run the Streamlit app
def main():
    st.title("Welcome to GrammarCraft!")
    st.markdown("### I am an assistant to help non-native english speakers improve their writing or comprehension skills.")
    st.markdown("### You can send me any text and I can help you to improve its grammar, style or even summarise it for you!")
    st.markdown('### As I am still new to this domain, I have a superior agent who reviews and scores my performance as well!')

    # User inputs OpenAI API Key in the sidebar
    openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key (Optional)', type='password')
    if not openai_api_key:
        openai_api_key = st.secrets['api_key']

    # User selects an option
    option = st.radio("Select an option:", ["Improve grammar", "Improve both grammar and style", "Summarise text"])

    # User inputs text
    user_input = st.text_input("Enter your text:")

    # User clicks the "Submit" button
    if st.button("Submit"):
        if option == "Improve grammar":
            st.write(f"You selected Option 1: {option}")
            response = improve_grammar(user_input, openai_api_key)
            st.markdown("### Grammar improvement by GrammarCraft Agent: \n" + response)

        elif option == "Improve both grammar and style":
            st.write(f"You selected Option 2: {option}")
            response = improve_grammar_and_style(user_input, openai_api_key)
            st.markdown("### Grammar plus style improvement by GrammarCraft Agent: \n" + response)

        elif option == "Summarise text":
            st.write(f"You selected Option 3: {option}")
            response = summarise(user_input, openai_api_key)
            st.markdown("### Summary by GrammarCraft Agent: \n" + response)

        # Evaluate the output using a superior agent
        eval_result = evaluate_output(option, user_input, response, openai_api_key)
        eval_display = print_scores(eval_result)
        print(type(eval_display), eval_display)
        st.markdown("### Evaluation by GrammarCraft's superior : \n" + eval_display)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
