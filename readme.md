#Extension connecting llm_python to telegram bot api.
-
![Image1](https://github.com/innightwolfsleep/storage/raw/main/textgen_telegram.PNG)

Providing chat like telegram bot interface with [abetlen/llm_python](https://github.com/abetlen/llm_python), [langchain](https://pypi.org/project/langchain/) or transformers (tbc) 

REQUIREMENTS:
- python-telegram-bot==13.15
- pyyaml
- deep-translator==1.9.2
- llm_python

HOW TO INSTALL:
1) clone this repo to "text-generation-webui\extensions"
```
cd text-generation-webui
git clone https://github.com/innightwolfsleep/llm_telegram_bot 
```
2) install requirements. 
```
pip install -r llm_telegram_bot\requirements.txt
```

HOW TO USE:
1) add your bot token to llm_telegram_bot/telegram_token.txt (ask https://t.me/BotFather how to get token)
2) add your model bin file to llm_telegram_bot/models
3) write path to your bin model file in llm_telegram_bot/telegram_llm_model_path.txt
2) run "python llm_telegram_bot/main.py"

FEATURES:
- chat and notebook modes
- session for all users are separative (by chat_id)
- local session history - conversation won't be lost if server restarts. Separated history between users and chars.
- nice "X typing" during generating (users will not think that bot stucking)
- buttons: continue previous message, regenerate last message, remove last messages from history, reset history button, new char loading menu
- you can load new characters from text-generation-webui\characters with "/load" command!!!
- you can load new model during conversation with /models 
- chatting # prefix for impersonate: "#You" or "#Castle guard" or "#Alice thoughts about me"
- "!" prefix to replace last bot message
- "++" prefix permanently replace bot name during chat (switch conversation to another character)
- save/load history in chat by downloading/forwarding to chat .json file
- integrated auto-translate (you can set model/user language parameter) 
