# from gtts import gTTS
# import os
# import pyttsx3
# def text_to_speech(text,name):
#     # mytext = text
#     # # Language in which you want to convert
#     # language = 'en'
#     # te= 'co.in'
#     #
#     # myobj = gTTS(text= mytext, lang=language, tld=te ,slow=False)
#     #
#     # filename=name+'.mp3'
#     # myobj.save(filename)
#     #
#     # # os.system(filename)
#     # return filename


#     # init function to get an engine instance for the speech synthesis
#     engine = pyttsx3.init()
#     voice = engine.getProperty('voices')  # get the available voices
#     # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
#     engine.setProperty('voice', voice[0].id)
#     engine.setProperty('volume', 1.0)
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', rate - 50)
#     tex = text
#     tex = tex.replace(". ", " ")
#     #
#     # # print(tex)
#     filename=name+'.mp3'
#     engine.save_to_file(tex, filename)
#     engine.runAndWait()
#     return filename
#     # say method on the engine that passing input text to be spoken
#     # engine.say(tex)

#     # run and wait method, it processes the voice commands.
#     # engine.runAndWait()

# # text_to_speech("hello how are you this is texting video so please adjust and corporate with us inorder to get the testing video successfully executed","hello")

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

import pyttsx3

def text_to_speech(text, name):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Get the available voices
    voices = engine.getProperty('voices')
    
    # Attempt to find a female voice based on common names/IDs
    female_voice = None
    for voice in voices:
        if "female" in voice.name.lower() or "Zira" in voice.name or "Samantha" in voice.name:
            female_voice = voice
            break
    
    if female_voice is not None:
        engine.setProperty('voice', female_voice.id)
    else:
        # If a female voice is not found, use the first voice
        engine.setProperty('voice', voices[0].id)
    
    # Set volume and rate for a clear, reporter-like delivery
    engine.setProperty('volume', 1.0)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 30)  # Slightly slower than default for clarity

    # Punctuate the text properly
    punctuated_text = text.replace(". ", ".\n")
    
    # Prepare the filename
    filename = name + '.mp3'
    
    # Save the text to speech to a file
    engine.save_to_file(punctuated_text, filename)
    engine.runAndWait()
    
    return filename

# Example usage
# news_text = "India and Mongolia recently concluded their 12th Joint Working Group meeting on defense cooperation in Ulaanbaatar. The two sides expressed satisfaction with existing initiatives, explored further cooperation opportunities, and discussed the current geopolitical landscape. India emphasized the potential of its defense industry for partnership with Mongolia, who expressed confidence in India's capabilities.  The meeting underscores the deepening ties between the two nations, built on shared history, cultural links, and common values."


# filename = text_to_speech(news_text, "test_Audio")
# print(f"File saved as {filename}")
