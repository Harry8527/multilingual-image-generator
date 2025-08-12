import gradio as gr
from translation import TranslateUserPrompt
from generate_image import GenerateImage

def process(input_prompt):
    translation_obj = TranslateUserPrompt()
    img_obj = GenerateImage()
    if len(input_prompt.split()) < 4:
        return '<span style="color:red;">Please enter a prompt which has atleast 4 words.</span>', None
    eng_prompt = translation_obj.translate(text=input_prompt)    
    image = img_obj.generate_image(prompt=eng_prompt)
    return eng_prompt, image


# iface = gr.Interface(fn = process,inputs=gr.Textbox(label="Enter your prompt<br>The prompt can be in Hindi, English, Spanish, or Punjabi."), outputs=[gr.Textbox("Output Image"), gr.Image()], title="Multilingual Text-to-Image Generator")
with gr.Blocks() as demo:
    gr.Markdown("# Multi-lingual Text-to-Image generator.\nSupports Hindi, English, Spanish, or Punjabi.")
    with gr.Row():
        input_prompt = gr.Textbox(label="Enter your prompt.")
    with gr.Row():
        translated_prompt = gr.Textbox(label="Translated prompt")
        output_image = gr.Image(label="Output Image")
    submit_btn = gr.Button("Generate Image")
    submit_btn.click(
        fn=process,
        inputs=input_prompt,
        outputs=[translated_prompt, output_image]
    )
    # Logic to show pop-up when the input prompt length is less than 4.

demo.launch(inbrowser=True)
