#!/bin/bash

# Path to the file containing sentences
SENTENCES_FILE="$HOME/Speak4me/sentences.txt"

# Ensure the sentences file exists
touch "$SENTENCES_FILE"
voice="Markus"

# Array to store the last 5 spoken sentences (in Bash)
declare -a last_spoken
speed=180

while true; do
    # Reverse the last spoken sentences and create fzf input
    fzf_input=""
    for ((i=${#last_spoken[@]}-1; i>=0; i--)); do
        fzf_input="${fzf_input}${last_spoken[$i]}"$'\n'
    done
    fzf_input="${fzf_input}$(cat "$SENTENCES_FILE")"
    
    # Use fzf to find a fuzzy match in the sentences file, ignoring case
    match=$(echo "$fzf_input" | fzf --print-query --exact --ignore-case --algo=v2 | tail -n1)
    echo "Spreche: $match"
    
    # Adjust the speaking speed based on the match
    if [[ "$match" == "computer sprich langsam" ]]; then
        speed=50
        echo "Speed set to slow (50)."
    elif [[ "$match" == "computer sprich normal" ]]; then
        speed=180
        echo "Speed set to normal (180)."
    elif [[ "$match" == "computer sprich schnell" ]]; then
        speed=200
        echo "Speed set to fast (200)."
    fi
    
    # Add the input to the sentences file
    echo "$match" >> "$SENTENCES_FILE"
    
    # Check if the match is exit command
    if [[ "$match" == "exit" ]]; then
        echo "Exiting program."
        break
    fi
    
    # Check if the match contains "auf * umschalten" to switch the voice
    if [[ "$match" == *"auf"* ]] && [[ "$match" == *"umschalten"* ]]; then
        new_voice=$(echo "$match" | awk '{print $2}')
        if say -v ? | grep -q "$new_voice"; then
            voice="$new_voice"
            echo "Voice switched to: $voice"
        else
            echo "Voice $new_voice not found"
        fi
        sleep 2
    fi
    
    # Use the 'say' utility to pronounce the text in the background
    say -r "$speed" -v "$voice" "$match" >/dev/null 2>&1 &
    say -r "$speed" -v "$voice" -a 90 "$match" >/dev/null 2>&1 &
    echo "Saying: $match"
    
    # Update the last spoken list (array in bash)
    last_spoken+=("$match")
    if [ ${#last_spoken[@]} -gt 5 ]; then
        # Remove the oldest element (shift the array)
        last_spoken=("${last_spoken[@]:1}")
    fi
    
    # Remove duplicate lines from the sentences file
    sort -u "$SENTENCES_FILE" | sed 's/-$//g' > "$SENTENCES_FILE.tmp"
    mv "$SENTENCES_FILE.tmp" "$SENTENCES_FILE"
done
