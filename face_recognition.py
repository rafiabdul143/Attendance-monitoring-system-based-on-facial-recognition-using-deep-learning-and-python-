from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1 = Label(self.root, text="Facial Recognition", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\ATTENDANCE MONITORING SYSTEM\images\10450457.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb3 = Label(self.root, image=self.photoimg_top)
        f_lb3.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\ATTENDANCE MONITORING SYSTEM\images\10450599.png")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb3 = Label(self.root, image=self.photoimg_bottom)
        f_lb3.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lb3, text="facial recognition", cursor="hand2", font=("times new roman", 18, "bold"),
                      bg="red", fg="white", command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)
    #==============attendance======
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n},{d}, {dtString}, {d1},Present")

    # ================== face recognition============
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in featuers:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(user='root', password='Lbnagar@1786', host='localhost',
                                               database='table1', port=3306)
                cursor = conn.cursor()

                cursor.execute("select Semester from student where student_id=" + str(id))
                n = cursor.fetchone()
                if n:
                    n = n[0]  # Accessing the first element of the fetched row
                else:
                    n = "Unknown"

                cursor.execute("select roll from student where student_id=" + str(id))
                r = cursor.fetchone()
                if r:
                    r = r[0]  # Accessing the first element of the fetched row
                else:
                    r = "Unknown"
                cursor.execute("select Name from student where student_id=" + str(id))
                d = cursor.fetchone()
                if d:
                    d = d[0]  # Accessing the first element of the fetched row
                else:
                    d = "Unknown"
                
                i=str(id)
                if confidence > 80:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"dep:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_Cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_Cap.read()
            
            print("Capture successful:", ret)
            img = recognize(img, clf, faceCascade)

            cv2.imshow("welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_Cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
