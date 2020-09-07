import cv2
face=cv2.CascadeClassifier("frontal_face.xml")
nose=cv2.CascadeClassifier("Nariz.xml")
capture=cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        color_face=frame[y:y+h,x:x+w]
        grey_face=cv2.cvtColor(color_face,cv2.COLOR_BGR2GRAY)
        noses=nose.detectMultiScale(grey_face,1.7,5)
        print(noses)
        if noses==():
            cv2.putText(frame, "MASK IS THERE", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, 1)
        else:
            for (a, b, c, d) in noses:
                cv2.putText(frame,"NO MASK",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,1)
                cv2.rectangle(color_face, (a, b), (a + c, b + d), (0, 0, 255), 4)
    cv2.imshow("Abhinav's Frame",frame)
    if cv2.waitKey(1)==13:
        break
capture.release()
cv2.destroyAllWindows()