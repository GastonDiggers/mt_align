import json
import os
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from multiprocessing import Pool

def translate(translator:GoogleTranslator ,text:str) -> str:
    return translator.translate(text)

def translate_xml(file_path):
    # Load the xml file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Initialize a list to store the translations
    translations = []
    translator = GoogleTranslator(source='en', target="fr")

    # Loop through each trans-unit element in the xml file
    for trans_unit in root.iter('{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
        # Get the source text
        source_text = ""
        for child in trans_unit.iter('{urn:oasis:names:tc:xliff:document:1.2}source'):
            if child.text:
                source_text += child.text
            for sub_child in child:
                if sub_child.tail:
                    source_text += sub_child.tail

        # Translate the source text to French
        if source_text:
            translation = translate(translator=translator, text=source_text)

            # Create a JSON object with the source and target text
            translation_obj = {"source": source_text, "target": translation}

            # Add the translation object to the list
            translations.append(translation_obj)

    # Save the list of translations as JSONL file
    output_file_path = os.path.join('output', os.path.basename(file_path).replace('.mqxliff', '_output.jsonl'))
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for translation_obj in translations:
            json.dump(translation_obj, f, ensure_ascii=False)
            f.write('\n')

if __name__ == '__main__':
    # Get a list of all the XML files in the data folder
    data_files = [os.path.join('data', f) for f in os.listdir('data') if f.endswith('.mqxliff')]

    # Use multiprocessing to translate all the XML files in parallel
    with Pool() as pool:
        pool.map(translate_xml, data_files)
