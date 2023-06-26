
#  Place where path to LLM file stored
telegram_llm_model_path_file = "telegram_llm_model_path.txt"

mode = "llama_cpp"
n_ctx = 8196
seed = 0
n_gpu_layers = 0

if mode == "llama_cpp":
    from generators.GeneratorLlamaCpp import get_answer as g_get_answer
    from generators.GeneratorLlamaCpp import tokens_count as g_tokens_count
    from generators.GeneratorLlamaCpp import get_model_list as g_get_model_list
    from generators.GeneratorLlamaCpp import load_model as g_load_model
elif mode == "LangchainLlama":
    from generators.GeneratorLangchainLlamaCpp import get_answer as g_get_answer
    from generators.GeneratorLangchainLlamaCpp import tokens_count as g_tokens_count
    from generators.GeneratorLangchainLlamaCpp import get_model_list as g_get_model_list
    from generators.GeneratorLangchainLlamaCpp import load_model as g_load_model
elif mode == "transformers":
    from generators.GeneratorTransformers import get_answer as g_get_answer
    from generators.GeneratorTransformers import tokens_count as g_tokens_count
    from generators.GeneratorTransformers import get_model_list as g_get_model_list
    from generators.GeneratorTransformers import load_model as g_load_model


def get_answer(
        prompt,
        generation_params,
        eos_token,
        stopping_strings,
        default_answer: str,
        turn_template='',
        **kwargs):
    # Preparing, add stopping_strings
    answer = default_answer

    print("mode =", mode)
    print("stopping_strings =", stopping_strings)
    print(prompt, end="")
    answer = g_get_answer(prompt, generation_params, eos_token, stopping_strings, default_answer, turn_template)
    print(answer)
    return answer


def tokens_count(text: str):
    return g_tokens_count(text)


def get_model_list():
    return g_get_model_list()


def load_model(model_file: str):
    return g_load_model(model_file)