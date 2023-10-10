import cv2
import numpy as np
import smtplib
import playsound
import threading

Alarm_Status = False
Email_Status = False
Fire_Reported = 0


def play_alarm_sound_function():
    while True:
        playsound.playsound('alarm-sound.mp3', True)


def send_mail_function():
    print("start")
    recipientEmail = "jay.bha.rt20@dypatil.edu"
    recipientEmail = recipientEmail.lower()
    user = "kar.she.rt20@dypatil.edu"
    pwd = "Meshelar@163"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('kar.she.rt20@dypatil.edu', 'Meshelar@163')
        # server.sendmail(user, recipientEmail, "Fire in the hole")
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print(e)

send_mail_function()


# If you want to use webcam use Index like 0,1.
# video = cv2.VideoCapture(0)

# while True:
#     (grabbed, frame) = video.read()
#     if not grabbed:
#         break

#     frame = cv2.resize(frame, (960, 540))

#     blur = cv2.GaussianBlur(frame, (21, 21), 0)
#     hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

#     lower = [18, 50, 50]
#     upper = [35, 255, 255]
#     lower = np.array(lower, dtype="uint8")
#     upper = np.array(upper, dtype="uint8")

#     mask = cv2.inRange(hsv, lower, upper)

#     output = cv2.bitwise_and(frame, hsv, mask=mask)

#     no_red = cv2.countNonZero(mask)

#     if int(no_red) > 15000:
#         Fire_Reported = Fire_Reported + 1

#     cv2.imshow("output", output)

#     if Fire_Reported >= 1:

#         if Alarm_Status == False:
#             threading.Thread(target=play_alarm_sound_function).start()
#             Alarm_Status = True

#         if Email_Status == False:
#             threading.Thread(target=send_mail_function).start()
#             Email_Status = True

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
# video.release()
