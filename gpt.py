#!/usr/bin/env python
import openai
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Run GPT-3 from the terminal.')
    parser.add_argument('prompt', type=str, help='Prompt submitted to GPT-3.')
    parser.add_argument('--max-tokens', type=str, help='The max tokens to return.', default='100')

    return parser.parse_args()


def submit_prompt(prompt, model="text-davinci-002", max_tokens=100):
    response = openai.Completion.create(model=model, prompt=prompt, temperature=0, max_tokens=max_tokens)
    return response['choices'][0]['text']


def main():
    args = parse_args()
    prompt = args.prompt
    max_tokens = int(args.max_tokens)

    response = submit_prompt(prompt, max_tokens=max_tokens)

    print(f'\nPrompt:\n\"{prompt}\"\n')
    print(f'#------ GPT-3 ------#{response}\n\n#------  End  ------#\n')


if __name__ == "__main__":
    main()