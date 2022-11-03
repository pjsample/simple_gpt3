import gradio as gr
import gpt


def submit_gradio_prompt(prompt, model, max_tokens):
    return gpt.submit_prompt(prompt, model, int(max_tokens))



with gr.Blocks() as demo:
    gr.Markdown('## Simple GPT-3')
    with gr.Column():
        with gr.Row():
            with gr.Column(scale=2):
                prompt = gr.Textbox(label="Prompt")
                output = gr.Textbox(label="GPT-3")


            with gr.Column(scale=1):
                    model = gr.Dropdown(["text-davinci-002", 'text-curie-001', 'text-babbage-001', 'text-ada-001'], label='Model', value='text-davinci-002')
                    max_tokens = gr.Textbox(label="Max Tokens", value=200)

        greet_btn = gr.Button("Submit Prompt")
        greet_btn.click(fn=submit_gradio_prompt, inputs=[prompt, model, max_tokens], outputs=output)
demo.launch()

