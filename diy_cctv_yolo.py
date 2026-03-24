
import cv2 as cv
from ultralytics import YOLO
from twilio.rest import Client
import time
#import os
#print(os.getcwd())

account_sid = "XXXXXXXXXXXXX"
auth_token =  "xxxxxxxxxx"
twilio_number = "+13XXXx14691"
your_number = "+919XXXX514"

client = Client(account_sid, auth_token) 

model = YOLO("yolov8n.pt")
last_sent_time = 0
cooldown = 30  # seconds
person_detected = False

#model = YOLO(r"durga\opencvwork\OpenCV\yolov8n-face.pt")

capture = cv.VideoCapture("http://192.168.68.109:8080/video", cv.CAP_FFMPEG)    


if not capture.isOpened():
    print("error accessing/opening the cam")
    exit()

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("error reading the frame")
        break

    results = model(frame, stream=True)
   
    for r in results:
        if len(r.boxes) > 0:
            person_detected = True

            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

    # 🔥 Send SMS (with cooldown)
    current_time = time.time()

    if person_detected and (current_time - last_sent_time > cooldown):
        message = client.messages.create(
            body="🚨 Alert: Person detected on camera!",
            from_=twilio_number,
            to=your_number
        )
        print("SMS sent:", message.sid)
        last_sent_time = current_time
        person_detected = False

    cv.imshow("YOLO Detection", frame)

    

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

