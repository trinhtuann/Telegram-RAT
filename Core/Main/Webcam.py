import cv2
import time


# Takes a photo from a webcam

def TakeWebcamPhoto(File):
 cap = cv2.VideoCapture(0)
 for i in range(30):
    cap.read()
 ret, frame = cap.read()
 cv2.imwrite(File, frame)
 cap.release()


# Records webcam video

def VideoRecorder(Seconds, File):
 capture_duration = float(Seconds)
 cap = cv2.VideoCapture(0)
 fourcc = cv2.VideoWriter_fourcc(*'XVID')
 out = cv2.VideoWriter(File,fourcc, 20.0, (640,480))
 start_time = time.time()
 while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
    else:
        break
 cap.release()
 out.release()
 cv2.destroyAllWindows()
