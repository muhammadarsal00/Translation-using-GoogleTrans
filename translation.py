from googletrans import Translator
from googletrans import LANGUAGES

def translate_text(text, target_language):
    # Initialize the translator
    translator = Translator()

    # Perform the translation
    translation = translator.translate(text, dest=target_language)

    # Return the translated text
    return translation.text

def main():
    # Get user input for the text to translate
    text_to_translate = input("Enter text to translate: ")

    # To select the code of the language which you waant to translate
    for lang_code, lang_name in LANGUAGES.items():
        print(f'{lang_code} : {lang_name}')
    
    # Get user input for the target language code
    target_language = input("Enter target language code : ")

    
    # Translate the text
    translated_text = translate_text(text_to_translate, target_language)
    
    # Display the translated text
    print(f"Translated Text: {translated_text}")

if __name__ == "__main__":
    main()



