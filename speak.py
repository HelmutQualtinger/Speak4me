import os
import subprocess
import time

# Path to the file containing sentences
SENTENCES_FILE = "/Users/haraldbeker/logbook/sentences.txt"

# Ensure the sentences file exists
open(SENTENCES_FILE, 'a').close()
voice = 'Markus'

# List to store the last 5 spoken sentences
last_spoken = []
speed = 180

while True:
    # Combine last spoken sentences with the sentences file for fzf input
    reversed_last_spoken = last_spoken[::-1]
    
    fzf_input = '\n'.join(reversed_last_spoken) + '\n' + open(SENTENCES_FILE).read()
    
    # Use fzf to find a fuzzy match in the sentences file, ignoring case
    result = subprocess.run(['fzf', '--print-query', '--exact', '--ignore-case', '--algo=v2'], 
                            input=fzf_input, 
                            text=True, capture_output=True)
    match = result.stdout.strip().split('\n')[-1]
    print(f"Spreche: {match}")
    
    # Adjust the speaking speed based on the match
    if match.lower() == "computer sprich langsam":
        speed = 50
        print("Speed set to slow (50).")
    elif match.lower() == "computer sprich normal":
        speed = 180
        print("Speed set to normal (180).")
    elif match.lower() == "computer sprich schnell":
        speed = 200
        print("Speed set to fast (200).")
    # Add the input to the sentences file if it's not already there
    with open(SENTENCES_FILE, 'a') as f:
        f.write(match + '\n')
    
    # Check if the match contains "auf * umschalte" to switch the voice
    if match.lower() == "exit":
        print("Exiting program.")
        break
    
    if "auf" in match and "umschalten" in match:
        new_voice = match.split()[1]
        if new_voice in subprocess.run(['say', '-v', '?'], capture_output=True, text=True).stdout:
            voice = new_voice
            print(f"Voice switched to: {voice}")
        else:
            print(f"Voice {new_voice} not found")
        time.sleep(2)
    # Use the 'say' utility to pronounce the text in the background
    subprocess.Popen(['say', '-r', f'{speed}', '-v', voice, match], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen(['say', '-r', f'{speed}', '-v', voice, '-a', '90', match], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Saying: " + match)
    
    # Update the last spoken list
    last_spoken.append(match)
    if len(last_spoken) > 5:
        last_spoken.pop(0)  # Keep only the last 5 entries
    
    # Remove duplicate lines from the sentences file
    with open(SENTENCES_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line.rstrip('-$\n') + '\n' for line in lines]
    with open(SENTENCES_FILE, 'w') as f:
        f.writelines(sorted(set(lines)))
