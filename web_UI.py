import gradio as gr
import gpt
import os

def submit_gradio_prompt(prompt, model, max_tokens, temperature):
    return gpt.submit_prompt(prompt, model, int(max_tokens), temperature, openai_api_key)

openai_api_key = os.getenv("OPENAI_API_KEY")

with gr.Blocks() as app:
    gr.Markdown('## Simple GPT-3')
    with gr.Column():
        with gr.Row():
            with gr.Column(scale=2):
                prompt = gr.Textbox(label="Prompt")
                output = gr.Textbox(label="GPT-3")


            with gr.Column(scale=1):
                    model = gr.Dropdown(['text-davinci-002', 'code-davinci-002', 
                                        'code-cushman-001', 'text-curie-001',
                                        'text-babbage-001', 'text-ada-001'],
                                        label='Model', value='text-davinci-002')
                    max_tokens = gr.Textbox(label="Max Tokens", value=500)
                    temperature = gr.Slider(minimum=0, maximum=1, value=0, label='Temperature')

        greet_btn = gr.Button("Submit Prompt").style(full_width=False)
        greet_btn.click(fn=submit_gradio_prompt,
                        inputs=[prompt, model, max_tokens, temperature],
                        outputs=output)

app.launch(server_name='0.0.0.0', )

