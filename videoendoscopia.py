#######################################################################################################################################
###########################  Francisco Caussa  - 2020 #################################################################################
#######################################################################################################################################
## El siguiente script es utilizado para simular un equipo de video endscopias a traves de la implementacion de una camara web
## o un borosocpio. El mismo muestra por defecto las imagenes adquiridas a traves de la camara web/boroscopio, y al momento de 
## ingresar dentro de una cavidad simulada, se presiona la tecla "q" (o el boton/pedal que se adjunta en el proyecto) el cual alterna
## la visualizacion por un video pregrabado de una videoendoscopia ALTA
########################################################################################################################################


# importing libraries
import cv2
import numpy as np
import ctypes
from datetime import datetime
import time
import os,sys
user32 = ctypes.windll.user32

def endoscopia():
    w=user32.GetSystemMetrics(0)
    h= user32.GetSystemMetrics(1)
    # Full screen mode
    cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    camara = True
    cam = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(os.getcwd()+'/endoscopia.wmv')
    previous_frame_timestamp = 0
    while True:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)
        frame = canvas
        if (time.time() - previous_frame_timestamp) > 1./fps:
            previous_frame_timestamp = time.time()
            if camara:
                ret_val, frame = cam.read()
            else:
                ret, frame = cap.read()  
                if frame is None:
                    #go to Frame 1
                    cap.set(cv2.CAP_PROP_POS_FRAMES,1)
                    #ask again for the frame!
                    ret, frame = cap.read()

        img = cv2.resize(frame, ((int)(w*.6),(int)(h*.75)))
        x=(int)(w*.95)-img.shape[1]
        y=(int)(h*.85)-img.shape[0]
        x_=(int)(w*.5)-174
        y_= (int)(h*.9)
        pt1 = (0, 0)
        pt2 = (0, 100)
        pt3 = (100, 0)
        triangle_cnt = np.array([pt1, pt2, pt3])
        cv2.drawContours(img, [triangle_cnt], 0, (0, 0, 0), -1)
        pt1 = (img.shape[1], 0)
        pt2 = (img.shape[1]-100,0)
        pt3= (img.shape[1],100)
        triangle_cnt = np.array([pt1, pt2, pt3])
        cv2.drawContours(img, [triangle_cnt], 0, (0, 0, 0), -1)
        pt1 = (0, img.shape[0])
        pt2 = (0, img.shape[0]-100)
        pt3 = (100, img.shape[0])
        triangle_cnt = np.array([pt1, pt2, pt3])
        cv2.drawContours(img, [triangle_cnt], 0, (0, 0, 0), -1)
        pt1 = (img.shape[1], img.shape[0])
        pt2 = (img.shape[1], img.shape[0] - 100)
        pt3 = (img.shape[1]-100, img.shape[0])
        triangle_cnt = np.array([pt1, pt2, pt3])
        cv2.drawContours(img, [triangle_cnt], 0, (0, 0, 0), -1)

        canvas[y:y + img.shape[0], x:x + img.shape[1]] = img
        #si se agrega un logo, descomentar
        #logo = cv2.imread(os.getcwd()+'/path/to/logo.png', cv2.IMREAD_UNCHANGED)
        #canvas[y_:y_ + logo.shape[0], x_:x_ + logo.shape[1]] = logo

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 2
        fecha = datetime.now()
        cv2.putText(canvas, fecha.strftime("%m/%d/%Y, %H:%M:%S"),(100,100), font, fontScale, fontColor, lineType)
        cv2.putText(canvas, 'V.E.S.', (100, 150), font, fontScale, fontColor, lineType)
        cv2.putText(canvas, 'Patient: Francisco Caussa', (100, 200), font, fontScale, fontColor, lineType)
        cv2.putText(canvas, 'D.o.B: 2005-04-22', (100, 250), font, fontScale, fontColor, lineType)
        cv2.putText(canvas, 'Age: 16', (100, 300), font, fontScale, fontColor, lineType)
        cv2.putText(canvas, 'Study: V.E.D.A.', (100, 350), font, fontScale, fontColor, lineType)
        cv2.putText(canvas, 'Dr. Cabrera, Daniel', (100, 400), font, fontScale, fontColor, lineType)

        cv2.imshow(WINDOW_NAME, canvas)
        # Presionar la tecla Q alterna entre Camara y Video
        if cv2.waitKey(25) & 0xFF == ord('q'):
           if camara == True:
               camara=False
           else:
               camara=True
        #Presionar ESC cierra el programa
        if cv2.waitKey(1) == 27: 
            break  # 
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    WINDOW_NAME = 'VideoEndoscopio Simulado'
    fps = 30
    endoscopia()
    sys.exit(0)