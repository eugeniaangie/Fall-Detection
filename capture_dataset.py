import cv2
import time
import os
from datetime import datetime

x=0
while x < 3:
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.release()
    #save to directory
    path = 'D:/You deserve better/1. TA SEMOGA CERIA, 2021 lulus AAMIIN/1. Fall Detection/Dataset/Falling'
    # Our operations on the frame come here
    x=x+1
    current_time = datetime.now()
    image_name = current_time.strftime("%d%H%M%S")
    cv2.imwrite(os.path.join(path, "falling"+image_name+".png"), frame)
    time.sleep(3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()