from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer



class TranslateUserPrompt():
    def __init__(self):
        self.supported_languages = {
            "hi" : "Hindi", 
            "en" : "English",
            "es" : "Spanish",
            "pa" : "Punjabi"
        }

    def find_language(self,user_prompt):
        self.lang = detect(user_prompt)
        if self.lang in self.supported_languages:
            print(f"The input is in: {self.supported_languages[self.lang]}")
        else:
            print(f"Prompt is provided in unsupported language by the user.")
        return self.lang


    def initialize_model_name(self, input_lang):
        if input_lang == "en":
            return None
        else:
            model_name = f"Helsinki-NLP/opus-mt-{input_lang}-en"
            return model_name

    def get_tokenizer_and_model_obj(self, model_name):
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model= MarianMTModel.from_pretrained(model_name)
        return tokenizer,model

    def translate(self, text):
        lang = self.find_language(user_prompt=text)
        model_name = self.initialize_model_name(input_lang = lang)
        tokenizer, model = self.get_tokenizer_and_model_obj(model_name=model_name)
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        return tokenizer.decode(translated[0], skip_special_tokens=True)

# def main(input_text):
#     translated_eng_prompt=""
#     input_language = find_language(input_text)
#     model_name = initialize_model_name(input_language=input_language)

#     if not (model_name):
#         print("User input is already in English, no translation is required.")
#         translated_eng_prompt = input_text
#     else:      
#         model_name = initialize_model_name(input_language=input_language)
#         tokenizer, model = get_tokenizer_and_model_obj(model_name=model_name)
#         translated_eng_prompt = translate(text=input_text, tokenizer=tokenizer, model=model)
#         print(f"Translated text: {translated_eng_prompt}")
#     image_obj = GenerateImage()
#     prompt_image = image_obj.generate_image(prompt=translated_eng_prompt)
#     prompt_image.show()
#     prompt_image.save("model_house_image_with_punjabi")
    
# if __name__== "__main__":    
#     # parser = argparse.ArgumentParser()
#     # parser.add_argument("--prompt", type=str, help="Enter prompt to generate image.")
#     # args = parser.parse_args()
    
#     # input_text = "एक बिल्ली की तस्वीर बनाएं"
#     # input_text = "generar una imagen de una casa"
#     input_text = "ਘਰ ਦੀ ਤਸਵੀਰ ਬਣਾਓ"
#     # input_text = "Create an image of a House"

#     main(input_text=input_text)
