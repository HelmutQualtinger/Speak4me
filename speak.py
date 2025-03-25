#!/usr/bin/env python3
"""
This script uses the 'say' utility on macOS to speak sentences from a file.
It uses fzf to select a sentence and supports changing speed and voice.
It remembers the last spoken sentences and removes duplicates from the file.
The script exits when the user types 'exit.'.
"""
import os
import subprocess
import time

# Configuration constants
SENTENCES_FILE = os.path.expanduser("~/Speak4me/sentences.txt")
DEFAULT_VOICE = 'Markus'
DEFAULT_SPEED = 180
SLOW_SPEED = 50
FAST_SPEED = 200
MAX_LAST_SPOKEN = 10

# Ensure the sentences file exists
open(SENTENCES_FILE, 'a').close()

# For quick access to last spoken sentences
last_spoken = []


def get_fzf_selection():
    """Use fzf to select a sentence from file and last spoken entries."""
    # Prepare fzf input content
    reversed_last_spoken = last_spoken[::-1]
    with open(SENTENCES_FILE, 'r') as f:
        content = f.read()
    fzf_input = "\n".join(reversed_last_spoken) + "\n" + content

    result = subprocess.run(
        ['fzf', '--print-query', '--exact', '--ignore-case', '--algo=v2'],
        input=fzf_input,
        text=True,
        capture_output=True
    )
    
    # Get the last line from the output (the selection or query)
    return result.stdout.strip().split('\n')[-1].rstrip('-')


def update_speed_and_message(match, current_speed):
    """Update speech speed on recognized commands."""
    match_lower = match.lower()
    commands = {
        "computer sprich langsam": (SLOW_SPEED, f"Speed set to slow ({SLOW_SPEED})."),
        "computer sprich normal": (DEFAULT_SPEED, f"Speed set to normal ({DEFAULT_SPEED})."),
        "computer sprich schnell": (FAST_SPEED, f"Speed set to fast ({FAST_SPEED}).")
    }
    return commands.get(match_lower, (current_speed, None))


def update_voice(match, current_voice):
    """Update voice if the command is to change voice."""
    tokens = match.split()
    if len(tokens) >= 3 and "auf" in match.lower() and "umschalten" in match.lower():
        new_voice = tokens[1]
        voices = subprocess.run(['say', '-v', '?'], capture_output=True, text=True).stdout
        if new_voice in voices:
            print(f"Voice switched to: {new_voice}")
            return new_voice, f"New voice {new_voice}"
        else:
            print(f"Voice {new_voice} not found")
    return current_voice, match


def speak_phrase(phrase, speed, voice):
    """Speak the phrase using say utility."""
    for amp in ['', '-a', '90']:
        args = ['say', '-r', str(speed), '-v', voice, phrase]
        if amp != '':
            args.insert(-1, amp)
        subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Saying: " + phrase)


def remove_duplicates():
    """Remove duplicate lines from the sentences file."""
    with open(SENTENCES_FILE, 'r') as f:
        lines = f.readlines()
    # Remove trailing unwanted characters and create a unique set
    cleaned = {line.rstrip('-$\n') + '\n' for line in lines}
    with open(SENTENCES_FILE, 'w') as f:
        f.writelines(sorted(cleaned))


def append_sentence(sentence):
    """Append the given sentence to the sentences file."""
    with open(SENTENCES_FILE, 'a') as f:
        f.write(sentence + "\n")


def main():
    voice = DEFAULT_VOICE
    speed = DEFAULT_SPEED

    while True:
        match = get_fzf_selection()
        print(f"Spreche: {match}")

        # Adjust speed based on recognized commands
        speed, speed_message = update_speed_and_message(match, speed)
        if speed_message:
            print(speed_message)

        # Exit condition
        if match.lower() == "exit.":
            print("Exiting program.")
            break

        # Handle voice change commands
        voice, match_to_speak = update_voice(match, voice)

        # Append to sentences file
        append_sentence(match)

        # Speak out the text
        speak_phrase(match_to_speak, speed, voice)

        # Update last spoken sentences with a maximum history
        last_spoken.append(match)
        if len(last_spoken) > MAX_LAST_SPOKEN:
            last_spoken.pop(0)

        # Clean file duplicates
        remove_duplicates()
        # Short delay to prevent rapid-fire loops
        time.sleep(0.5)


if __name__ == "__main__":
    main()
