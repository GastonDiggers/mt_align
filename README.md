# Translation Reversal Tool - MT_Align

## Description

This project aims to generate 'fake' source sentences for given target translations. This is useful when the original source files are unavailable. The generated 'fake' source can then be used to fill in missing source sentences in translation files.

## Getting Started

These instructions will guide you on how to use this tool.

### Prerequisites

Before running the script, you need to install the required Python libraries. You can install them using pip:

```shell
pip install -r requirements.txt
```

### Usage
Before running the application, ensure that Python is installed on your system and added to the PATH environment variable.

Run the run.bat script. This can be done by double-clicking on the file in your file explorer.

The GUI will open. Select the input folder which contains the translation files that you want to generate a 'fake' source from.

The 'input folder' is the directory where the provided language files are stored. The generated files will be saved inside this folder.

Select the Provided Language (the language of the text you have).

Select the Desired Source Language (the language you want to generate).

Click the "Run Script" button. The script will create a new folder named "output_<current_datetime>" in the input folder. This new folder will contain the generated source files.

Note: In the generated source files, 'fake' translations are prefixed with "!! ". This is done to make it easy to distinguish them in translation comparisons. As these are generated translations, they won't match 100% with the actual source sentences. This prefix also helps to avoid the misinterpretation of these generated translations as perfect matches.

## Built With
Python
GoogleTranslator from the deep_translator library
Tkinter for the GUI
## Authors
Gaston Guyot