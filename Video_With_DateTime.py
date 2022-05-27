# Time conversion:
# %I  Hour (12-hour clock) as a decimal number [01,12].
# %H  Hour (24-hour clock) as a decimal number [00,23].
# %A  Locale's full weekday name
# %B  Locale's full month name.
# %d  Day of the month as a decimal number
# %Y  Year with century as a decimal number.

import os
import cv2
import datetime
import speech_recognition as sr
import pyaudio
from gtts import gTTS

# Here we connect to capture source
cam = cv2.VideoCapture(0)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(2) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


while cam.isOpened():
    ret, frame = cam.read()

    # Here we gather current system date and time
    cron = datetime.datetime.now()

    # Here we set the variable for the font for the text on the video output
    font = cv2.FONT_HERSHEY_PLAIN

    # Here we set the variable for, the text and format it for video output,
    # the location on screen, font, scale, color, thickness, and line type.
    frame = cv2.putText(frame, cron.strftime('%I:%M:%S on %A, %B the %dth, %Y'), (10, 40), font, 1,
                        (255, 150, 0), 2, cv2.LINE_AA)

    # show image
    cv2.imshow('Webcam', frame)
    get_audio()

    # This checks whether q has been hit and stops the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# This releases the capture device
cam.release()

# This closes the frame
cv2.destroyAllWindows()
