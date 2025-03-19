from deep_translator import GoogleTranslator

def translate_to_english(text):
    translator = GoogleTranslator(source='auto', target='it')
    translation = translator.translate(text)
    return translation

def main():
    with open('sentences.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for i,line in enumerate(lines):
        translated_line = translate_to_english(line.strip())
        print(f"{translated_line}")

if __name__ == "__main__":
    main()