from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lb1=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=45)
#top_image
        img_top = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\TOP1.jpg")
        img_top = img_top.resize((1530,325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb3 = Label(self.root, image=self.photoimg_top)
        f_lb3.place(x=0, y=55, width=1530, height=325)
#train_button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="black",fg="red")
        b1_1.place(x=0, y=380, width=1530, height=60)
       
#buttom_image
        img_buttom = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\BU.jpg")
        img_buttom = img_buttom.resize((1530,325), Image.LANCZOS)
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)

        f_lb3 = Label(self.root, image=self.photoimg_buttom)
        f_lb3.place(x=0, y=440, width=1530, height=325)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            """ cv2.resize(imageNp,(500,500)) """
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Train Data",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)


        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Training datasets completed!",parent=self.root)
    


       













if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

