import cv2
import numpy as np
import time
import autopy
import htm
import pyautogui

plocX, plocY = 0, 0
clocX, clocY = 0, 0
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
wScr, hScr = autopy.screen.size()
frameR = 100     # Frame Reduction
smoothening = 7  # random value
detector = htm.HandDetector(maxhands=1)

while True:
    # 1. Find hand landmarks
    # detector = htm.HandDetector(maxhands=1)
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # print(lmList)

    # 2. Tip of index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

    # 3. Check which fingers are up
        fingers = detector.fingersUp()
        # print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
    # 4. only index finger: moving mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            # x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
    # 6. Smoothen values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
    # 7. Move mouse
            autopy.mouse.smooth_move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
    # 8. Both index and middle up: clicking mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # 10. Click if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
                # autopy.mouse.click()
        if fingers[0] == 1 and fingers[1] == 1:
            length2, img, linfo = detector.findDistance(4, 8, img)
            # print(length2)
            if length2 < 30:
                # pyautogui.doubleClick()
                # pyautogui.click(clicks=2, interval=0.15)
                pyautogui.scroll(-5)
        if fingers[1] == 1 and fingers[4] == 1:
            length3, img, lineinfo3 = detector.findDistance(8, 20, img)
            if length3 < 40:
                pyautogui.scroll(5)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:
            length4, img, lineinfo4 = detector.findDistance(8, 12, img)
            length5, img, lineinfo5 = detector.findDistance(12, 16, img)
            length6, img, lineinfo6 = detector.findDistance(8, 16, img)
            if length4 < 30 and length5 < 30 and length6 < 30:
                pyautogui.click(button='right')
                # time.sleep(0.5)

    # 11. Frame Rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 80), cv2.FONT_ITALIC, 3, (255, 0, 255), 3)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
