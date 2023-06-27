import os
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

#  Place where path to LLM file stored
telegram_llm_model_path_file = ""
llm = None

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


def init():
    global llm
    with open(telegram_llm_model_path_file, "r") as model_path_file:
        data = model_path_file.read().rstrip()
        llm = LlamaCpp(model_path=data, n_ctx=2014, callback_manager=callback_manager, verbose=True)


def get_answer(
        prompt,
        generation_params,
        eos_token,
        stopping_strings,
        default_answer,
        turn_template='',
        **kwargs):
    if "max_tokens" in generation_params:
        llm.max_tokens = generation_params["max_tokens"]
    if "temperature" in generation_params:
        llm.temperature = generation_params["temperature"]
    if "top_p" in generation_params:
        llm.top_p = generation_params["top_p"]
    if "top_k" in generation_params:
        llm.top_k = generation_params["top_k"]
    prompt_template = PromptTemplate(template="{prompt}", input_variables=["prompt"])
    llm.stop = stopping_strings
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)
    answer = llm_chain.run(prompt)
    return answer


def tokens_count(text: str):
    return 0


def get_model_list():
    bins = []
    for i in os.listdir("models"):
        if i.endswith(".bin"):
            bins.append(i)
    return bins


def load_model(model_file: str):
    pass
