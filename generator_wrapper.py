from llama_cpp import Llama

#  Place where path to LLM file stored
telegram_llm_model_path_file = "telegram_llm_model_path.txt"

#  Get llm_generator
with open(telegram_llm_model_path_file, "r") as model_path_file:
    llm_generator = Llama(model_path=model_path_file.read())


def get_answer(prompt, generation_params, eos_token, stopping_strings, default_answer):
    answer = default_answer
    try:
        answer = llm_generator(
            prompt=prompt,
            temperature=generation_params["temperature"],
            top_p=generation_params["top_p"],
            top_k=generation_params["top_k"],
            repeat_penalty=generation_params["repetition_penalty"],
            stop=eos_token,
            max_tokens=generation_params["max_new_tokens"],
            echo=True)
        print(answer)
        answer = answer["choices"][0]["text"].replace(prompt, "")
    except Exception as exception:
        print("generator_wrapper get answer error ", exception)
    return answer


def get_server():
    return None


def get_shared():
    return None
