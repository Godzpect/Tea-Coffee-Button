import cv2
import mediapipe as mp
handmodel=mp.solutions.hands
handmodeldrawing=mp.solutions.drawing_utils
webcam=cv2.VideoCapture(0)
with handmodel.Hands(min_detection_confidence=0.6,min_tracking_confidence=0.5) as hands:
    while True:
        control,frame=webcam.read()
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=hands.process(rgb)
        height,width,channels=frame.shape
        cv2.rectangle(frame,(100,80),(202,150),(0,255,255),6)
        cv2.putText(frame, "TEA", (115, 127), cv2.FONT_ITALIC, 1.4, (0, 255, 255), 3)
        cv2.rectangle(frame, (400,80), (600,150), (55, 78,111 ), 6)
        cv2.putText(frame, "COFFEE", (415, 127), cv2.FONT_ITALIC, 1.4, (55, 78,111 ), 3)
        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                index_finger_point=handLandmark.landmark[8]
                x=int(index_finger_point.x*width)
                y=int(index_finger_point.y*height)
                #cv2.circle(frame,(x,y),4,(0,255,0),6)
                if 100<x<202 and 80<y<150:
                    cv2.rectangle(frame, (100, 80), (202, 150), (0,255,255), -1)
                    cv2.putText(frame,"TEA IS GREAT",(50,50),cv2.FONT_ITALIC,2,(0,255,255),4)
                elif 400 < x < 600 and 80 < y < 150:
                    cv2.rectangle(frame, (400, 80), (600, 150), (55, 78,111 ), -1)
                    cv2.putText(frame, "COFFEE IS GREAT", (160, 50), cv2.FONT_ITALIC, 1.5, (55, 78,111 ), 4)
                else:
                    cv2.putText(frame, "CHOOSE A BEVERAGE", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,0), 3)
        cv2.imshow("Project",frame)
        if cv2.waitKey(20)==27:
            break



