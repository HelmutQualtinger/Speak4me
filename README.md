# Speak4Me

`speak.py` is a Python script that allows selecting text from a file (`sentences.txt`) and reading it aloud using macOS's text-to-speech feature (`say` command). It provides an interactive user interface based on `fzf` to quickly and efficiently search and select texts.

## Use Case and Motivation

My vocal cords are severely damaged after surgery. I get tired quickly when speaking, and I am hard to understand. I wanted a simple way to have what I type spoken aloud. I am not very fast at typing, and communication this way is very slow. I want the spoken output not only to play through the speakers but also to be routed to a virtual microphone so that I can use it in telephony apps and video conferencing programs. This way, I can type, but other participants hear spoken words.

The macOS text-to-speech feature in Accessibility is decent, but it is not easy to quickly search through a large number of pre-written texts, and you have to switch between mouse and keyboard. That’s why I use the powerful `fzf`. A few keystrokes quickly narrow down the sentences without needing to remember keyboard shortcuts. It works somewhat like text prediction—not quite, but almost like artificial intelligence. The last five inputs are shown at the top of the list to quickly repeat them and as a reminder of what was just said in case the other party didn’t understand.

The longer you use the program, the more texts the system learns, and the more efficient it becomes. The texts are permanently saved in a file.

## Features

- **Text Selection with `fzf`**: The script uses `fzf`, a powerful fuzzy search tool, to select texts from the `sentences.txt` file or a list of recently spoken sentences.
- **Text-to-Speech**: The selected text is read aloud using macOS's text-to-speech feature (`say` command).
- **Speed Settings**: The speaking speed can be adjusted using specific commands:
  - `computer speak slowly`: Sets the speed to slow (50).
  - `computer speak normally`: Sets the speed to normal (180).
  - `computer speak quickly`: Sets the speed to fast (200).
- **Voice Switching**: By entering a command like `switch to Markus`, the voice can be changed, provided the voice is available.
- **History of Spoken Sentences**: The script saves the last five spoken sentences, which are prioritized in the next selection.
- **Automatic Duplicate Removal**: Duplicate entries in the `sentences.txt` file are automatically removed.

## Requirements

- **Operating System**: macOS (as the script uses the `say` command).
- **Python Version**: Python 3.x.
- **Additional Tools**:
  - `fzf` must be installed. It can be installed via Homebrew:
  
    ```bash
    brew install fzf
    ```

## Installation

1. Clone the repository or copy the `speak.py` file into a directory.
2. Ensure the `sentences.txt` file exists. If not, it will be created automatically.
3. Install `fzf` if it is not already installed.

## Usage

1. Start the script:
  
   ```bash
   python3 speak.py
   ```
