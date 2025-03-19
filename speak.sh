#!/bin/bash

# Path to the file containing sentences
SENTENCES_FILE="/Users/haraldbeker/logbook/sentences.txt"

# Ensure the sentences file exists
touch "$SENTENCES_FILE"

while true; do
 
    # Use fzf to find a fuzzy match in the sentences file, ignoring case
    match=$(cat $SENTENCES_FILE | fzf --print-query --ignore-case | tail -n 1)
    echo "Spreche: $match"

    # Add the input to the sentences file if it's not already there

    # Use the 'say' utility to pronounce the text
    say   -v "Markus"  "$match" &
    #say -a 90   -v "Markus"  "$match" &

    # Remove duplicate lines from the sentences file
    echo "$match" >> "$SENTENCES_FILE"
    sort -u "$SENTENCES_FILE" -o "$SENTENCES_FILE"
done
