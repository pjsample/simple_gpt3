#!/usr/bin/env python
import openai
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Run GPT-3 from the terminal.')
    parser.add_argument('prompt', type=str, help='Prompt submitted to GPT-3.')
    parser.add_argument('--model', type=str, help='The GPT-3 model that will be called.', default='text-davinci-002')
    parser.add_argument('--max-tokens', type=str, help='The max tokens to return.', default='100')
    
    return parser.parse_args()


def submit_prompt(prompt, model="text-davinci-002", max_tokens=100, temperature=0, open_api_key=None):
    """
    Submit a prompt to GPT-3 and return the response. 
    """
    if open_api_key is not None:
        openai.api_key = open_api_key
    response = openai.Completion.create(model=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens)
    return response['choices'][0]['text']

def get_api_key():
    '''
    Get the OpenAI API key from the environment variable OPENAI_API_KEY.
    '''
    return os.getenv("OPENAI_API_KEY")

def main():
    args = parse_args()

    prompt = args.prompt
    max_tokens = int(args.max_tokens)
    model = args.model

    openai.api_key = get_api_key()

    if open.api_key is None:
        print("Please set the OPENAI_API_KEY environment variable. Eg: export OPENAI_API_KEY=sk-XXXXXX")
        exit(1)

    response = submit_prompt(prompt, model=model, max_tokens=max_tokens)

    print(f'\nPrompt:\n\"{prompt}\"\n')
    print(f'#------ GPT-3 ------#{response}\n\n#------  End  ------#\n')


if __name__ == "__main__":
    main()