import cv2

cap = cv2.VideoCapture(0)
flag = 1
ret = True
while(ret):
    print(flag)
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    flag = flag+1

cap.release()
cv2.destroyAllWindows()
img = cv2.

