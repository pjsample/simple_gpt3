#!/usr/bin/env python
import openai
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Run GPT-3 from the terminal.')
    parser.add_argument('prompt', type=str, help='Prompt submitted to GPT-3.')
    parser.add_argument('--max-tokens', type=str, help='The max tokens to return.')

    return parser.parse_args()


def submit_prompt(prompt, model="text-davinci-002", max_tokens=100):
    response = openai.Completion.create(model=model, prompt=prompt, temperature=0, max_tokens=max_tokens)
    return response['choices'][0]['text']


def main():
    args = parse_args()
    prompt = args.prompt

    response = submit_prompt(prompt)

    print(f'Prompt:\n{prompt}\n')
    print(f'Response:{response}\n')


if __name__ == "__main__":
    main()