import speech_recognition as sr


def mic_get():

    audio_Input = sr.Recognizer()

    with sr.Microphone() as source:

        audio_Input.adjust_for_ambient_noise(source)

        print("Say something: ")

        audio = audio_Input.listen(source)

        try:
            respond = audio_Input.recognize_google(audio, language='en-US')

            print("You said: " + respond)

            return respond

        except:

            print("Speech not recognised")

            return 'none'


while True:

    mic_get()



