import cv2 as cv

capture = cv.VideoCapture(0)    

if not capture.isOpened():
    print("error accessing/opening the cam")
    exit()

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("error reading the frame")
        break
    cv.imshow("cc cam", frame)
    

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

