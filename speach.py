import sys
import subprocess
import platform


#!/usr/bin/env python3

def speak_text(text):
    """Speak the given text using the appropriate command for the OS."""
    system = platform.system()
    
    try:
        if system == 'Darwin':  # macOS
            subprocess.run(['say', text])
        elif system == 'Linux':
            subprocess.run(['spd-say', text])
        elif system == 'Windows':
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        else:
            print(f"Sorry, speech is not supported on {system}")
            print(f"Would have spoken: {text}")
    except Exception as e:
        print(f"Error speaking text: {e}")
        print(f"Would have spoken: {text}")

def main():
    # Get all command line arguments except the program name
    args = sys.argv[1:]
    
    if not args:
        print("Usage: python speach.py [text to speak]")
        return
    
    # Join all arguments into a single string
    text_to_speak = " ".join(args)
    
    # Speak the text
    speak_text(text_to_speak)

if __name__ == "__main__":
    main()