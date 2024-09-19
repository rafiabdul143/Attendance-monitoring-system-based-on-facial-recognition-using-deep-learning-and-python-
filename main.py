from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #first image
        img = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\label.jpg")
        img = img.resize((1530, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1500, height=130)
       
        # bg_image
        img3 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\bg1.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #student_button
        img4 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\students")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)
        #"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\images\face"
       #detect_face 
        img5 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\10450457.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=220,height=220)

        b1_1=Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=500, y=300, width=220, height=40)

        #attendance face button
       
        img6 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\attendancea.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=800, y=300, width=220, height=40)

        #help face button
       
        img7 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\helpdeskh.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=1100, y=300, width=220, height=40)


         #train_face_button
       
        img8 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\train_data")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=200, y=400, width=220, height=40)



         #photos button"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\images\pic4.jpg"
       
        img9 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\photose")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=500, y=400, width=220, height=40)
        

         #developer
       
        img10 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\dev")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=800, y=400, width=220, height=40)

         #exit
       
        img11 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\exite")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,command=self.Close,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Close,font=("times new roman",15,"bold"),bg="darkblue",fg="red")
        b1_1.place(x=1100, y=400, width=220, height=40)
    def open_img(self):
        os.startfile("data")
         
        
        # ==================Functions Buttons=====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
       # self.new_window.state('zoomed')
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
       # self.new_window.state('zoomed')
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Close(self):
        root.destroy()



     


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
