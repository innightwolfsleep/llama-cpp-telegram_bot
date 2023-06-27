import os
from langchain import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

#  Place where path to LLM file stored
telegram_llm_model_path_file = ""
llm = None
# Callbacks support token-wise streaming


def init():
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    global llm
    with open(telegram_llm_model_path_file, "r") as model_path_file:
        data = model_path_file.read().rstrip()
        llm = HuggingFacePipeline.from_model_id(model_id=data, task="text-generation",
                                                model_kwargs={"temperature": 1, "max_length": 16384})
        llm.generate_prompt()


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
