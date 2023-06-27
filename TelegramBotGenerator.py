
#  Place where path to LLM file stored
telegram_llm_model_path_file = "telegram_llm_model_path.txt"

mode = "GeneratorLlamaCpp"
n_ctx = 8196
seed = 0
n_gpu_layers = 0

# import generator
if mode == "GeneratorLlamaCpp":
    from generators.GeneratorLlamaCpp import Generator
    generator = Generator(telegram_llm_model_path_file, n_ctx, seed, n_gpu_layers)
elif mode == "GeneratorLangchainLlamaCpp":
    import generators.GeneratorLangchainLlamaCpp as Generator
    generator = Generator(telegram_llm_model_path_file, n_ctx, seed, n_gpu_layers)
elif mode == "GeneratorTransformers":
    import generators.GeneratorTransformers as Generator
    generator = Generator(telegram_llm_model_path_file, n_ctx, seed, n_gpu_layers)


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
    try:
        answer = generator.get_answer(prompt, generation_params, eos_token, stopping_strings, default_answer, turn_template)
    except Exception as e:
        print("generation error:", e)
    print(answer)
    return answer


def tokens_count(text: str):
    return generator.tokens_count(text)


def get_model_list():
    return generator.get_model_list()


def load_model(model_file: str):
    return generator.load_model(model_file)