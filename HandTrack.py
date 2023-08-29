import cv2
import mediapipe as mp
import time
import pyautogui as pag

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
a = 0
while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    a += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('r'):
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        a = 0
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            ary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for id, lm in enumerate(handlms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                cv2.circle(image, (cx, cy), 15, (154, 47, 69), cv2.FILLED)
                mpDraw.draw_landmarks(
                    image, handlms, mpHands.HAND_CONNECTIONS)
                ary[id] = abs(h-cy)
            if a >= 11 and a < 12:
                if ary[8] < ary[5] and ary[12] < ary[9]:
                    print(" you picked ___stone___    I picked ___paper____")
                elif ary[8] > ary[7] and ary[12] > ary[11] and ary[16] > ary[15]:
                    print("you picked ___paper___    I picked ___Scissor____")
                else:
                    print("you picked ___Scissor___    I picked ___stone____")
    cv2.imshow('preview', image)
cap.release()
cv2.destroyAllWindows()
