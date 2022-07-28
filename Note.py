
import Speak

import Word_Correction

from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError

import os


def voice_Text():

    recognition = Recognizer()

    mic = Microphone()

    with mic:

        recognition.adjust_for_ambient_noise(mic, duration=0.2)

        print("Talk")

        audio = recognition.record(mic, 5)

    try:
        recognized = recognition.recognize_google(audio)

        print('You Said : ', recognized)

        return recognized

    except UnknownValueError:

        print('Unable to Recognize audio')

        return 'None'

    except RequestError as error:

        print('Error Detected : ', error)

        return 'None'

    return recognized


def note_function():

    Speak.Speak("Please tell me what is name for your note")

    note_name = voice_Text().lower()


    #note_name = note_name.replace(" ", "_")

    note_path = "notes/"+note_name+".note"

    file = open(note_path, "a")

    file_status = os.path.exists(note_name+".note")

    if os.path.isfile(note_path):

        Speak.Speak("Note Create Successfully")

        file.close()

        write_note(note_path)
    else:

        Speak.Speak("Problem Found In System")

        file.close()


def write_note(doc_path: str):

    while True:

        Speak.Speak("What are you want to add this note")

        note = voice_Text().lower()

        print(note)

        if 'finish note' in note:

            file.close()

            Speak.Speak("Note Completely Finished")

        file = open(doc_path, 'a')

        note = Word_Correction.correct_sentence_spelling(note)

        file.write(note+"\n")


note_function()




