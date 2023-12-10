# English Improvement Agent

This is a streamlit app to accomplish the task provided in the file [Test_Instructions](./Test_Instructions.pdf). 

## Instructions to run the app

Create a separate virtual environment ideally and/or run 

```
pip install -r requirments.txt
```
Essentially you need to do 
```
pip install langchain streamlit openai
```

After that from the directory where you have the app.py file, run:

```
streamlit run app.py
```

Note: You need to provide your own OpenAI API key for that. You can create one by following this link: https://platform.openai.com/docs/quickstart?context=python


## Implentation details

The english improvement agent is based on OpenAI's GPT-3.5 model and GPT-4 model (only used for evaluation).

The three tasks are completed only using prompt engineering and there is no RAG needed. Reasons for not using RAG are:

1. No external data or knowledge or facts needed to perform the three tasks.
2. Summarisation could use some reference summaries, but that's more about doing few shot prompting than RAG.
3. Style improvement could have instead used fine-tuning to teach the agent a particular style, but it was not allowed in the assignment description.

Basic prompt engineering (zero-shot) is being used in the three tasks. It is always mentioned in the prompt that the text is written by a native english speaker which could contain ambiguity and inconsistency and that the agent needs to keep that in mind while performing the three tasks. 

In the summarisation task, where input text is more than 500 words (split by whitespace), I consider the 'refine' prompt method which sends chunks of the context via multiple LLM calls and refines the summary, instead of sending all the context in one single prompt.

## Evaluation

Evaluation is generally done by comparing the output text of an LLM with a reference text or through human feedback.

Since we lack both of these, a third, relatively new method of using an LLM to evaluate another LLM is used here.


Specifically, I use the [G-Eval](https://arxiv.org/pdf/2303.16634.pdf) evaluation criteria and use code inspired by this link: https://cookbook.openai.com/examples/evaluation/how_to_eval_abstractive_summarization. 

Essentially for all three tasks, there are 4 criteria to evaluate which are listed [here](./eval_metrics_info.md). These criteria and associated steps are fed as a prompt to a superior model (GPT-4 in this case), to evaluate the performance of the model used in the three tasks.

Grammar is evaluated as part of the fluency metric.


Summaries are evaluated as part of the relevance and coherence metric.

Style is evaluated as part of the consistency metric.