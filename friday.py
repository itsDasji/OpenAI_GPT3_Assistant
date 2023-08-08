# Developed by Toasty | 614 eShop x Dawnstar

# Version 0.0.1


import openai
import pyttsx3
import speech_recognition as sr
import time

# openai API key 
openai.api_key = "KEY_HERE"

# initialize text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Reconizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognizer_google(audio)
    except:
        print('skipping unexpected error')

# gpt-3 Auto Generated Responses
def generate_response(prompt):
    reponse = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000, # this is max by the engine. Lower this to increase query speed.
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
    
def main():
    while True:
        # wait for user to say "f.r.i.d.a.y."
        print("Say 'Friday' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "friday":
                    # record audio
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                            
                            # transcribe audio to text
                            text = transcribe_audio_to_text(filename)
                            if text:
                                print(f"You said: {text}")
                                
                                # generate response using GPT-3
                                response = generate_response(text)
                                print(f"GPT-3 says: {response}")
                                
                                # read response using text-to-speech
                                speak_text(response)
                except Expectation as e:
                    print("An error occurred: {}".format(e))
                    
if __name__ == "__main__":
    main()