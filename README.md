# Simple GPT-3
A lightweight client for interacting with GPT-3 in your terminal or by using a web UI that you run locally. All calls to GPT-3 use the GPT-3 API so you'll need an OPENAI API key. [OpenAI](https://openai.com/api/)


### Useful for work
![Simple_GPT-3 Example2](https://github.com/pjsample/simple_gpt3/blob/main/images/simple_gpt3_example2.png)

### And fun!
![Simple_GPT-3 Example1](https://github.com/pjsample/simple_gpt3/blob/main/images/simple_gpt3_example1.png)


## Getting it to work
```
pip install openai
git clone git@github.com:pjsample/simple_gpt3.git

cd simple_gpt3
chmod +x simple_gpt3.py
cp simple_gpt3.py simple_gpt3

export PATH=$PATH:$PWD

export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

simple_gpt3
```

#### Optional parameters
```
usage: simple_gpt3 [--model MODEL] [--max-tokens MAX_TOKENS] [--temperature TEMPERATURE]
                      [--api_key API_KEY]

Defaults:
--model text-davinci-002
--max-tokens 2000
--temperature 0
```

### To permanently add environment variables
```
Add these lines to `~/.zshrc` (or whichever file is appropriate for your terminal)

export PATH="/DIR_WHERE_YOU_CLONED_SIMPLE_GPT3:$PATH"

export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

### Local Web UI
![WebUI Example](https://github.com/pjsample/simple_gpt3/blob/main/images/webUI_example.png)
#### Local Web UI Setup
```
pip install openai
pip install gradio
git clone git@github.com:pjsample/simple_gpt3.git

export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

cd simplt_gpt3

# Run the web UI
python web_UI.py

# Then follow think link in the terminal
```
