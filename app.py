import gradio as gr
from translation import TranslateUserPrompt
from generate_image import GenerateImage

def process(input_prompt):
    translation_obj = TranslateUserPrompt()
    img_obj = GenerateImage()
    eng_prompt = translation_obj.translate(text=input_prompt)
    image = img_obj.generate_image(prompt=eng_prompt)
    return eng_prompt, image


# iface = gr.Interface(fn = process,inputs=gr.Textbox(label="Enter your prompt<br>The prompt can be in Hindi, English, Spanish, or Punjabi."), outputs=[gr.Textbox("Output Image"), gr.Image()], title="Multilingual Text-to-Image Generator")

with gr.Blocks() as demo:
    gr.Markdown("# Multi-lingual Text-to-Image generator.\nSupports Hindi, English, Spanish, or Punjabi.")
    with gr.Row():
        input_prompt = gr.Textbox(label="Enter your prompt here.")
    with gr.Row():
        translated_prompt = gr.Textbox(label="Translated prompt")
        output_image = gr.Image(label="Output Image")
    submit_btn = gr.Button("Generate Image")
    submit_btn.click(fn=process, inputs=input_prompt, outputs=[translated_prompt, output_image])

demo.launch(inbrowser=True)
