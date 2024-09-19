from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

#===============variables==========
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #first image
        img = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\label.jpg")
        img = img.resize((1530, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1530, height=130)
        #second image
        img1 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\students2")
        #img1 = img1.resize((500, 130), Image.LANCZOS)
        #self.photoimg1 = ImageTk.PhotoImage(img1)

       # f_lb2 = Label(self.root, image=self.photoimg1)
        #f_lb2.place(x=500, y=0, width=500, height=130)
        #third image
        img2 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\students")
       # img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        #f_lb3 = Label(self.root, image=self.photoimg2)
        #f_lb3.place(x=1000, y=0, width=500, height=130)

        # bg_image
        img3 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\pic6")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=0,width=1500,height=650)
#left frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="student details",font= ("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\th (2).jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb3 = Label(left_frame, image=self.photoimg2)

        f_lb3.place(x=5, y=0, width=720, height=130)

        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font= ("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=115)
        

        
       
      #Deparment
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)
       
#     Department Combobox
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo['values'] = ("select department", "Computer", "IT", "civil", "Iot", "mechanical", "csn")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky="W")


        #Course
        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("select a course", "B-tech", "M-tech", "Mba")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        

        #YEAR

        year_label=Label(current_course_frame,text="year",font=("times new roman", 12, "bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 12, "bold"),state="readonly",width=20)
        year_combo["values"]=("select a year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        semeseter_label=Label(current_course_frame,text="semester",font=("times new roman", 12, "bold"),bg="white")
        semeseter_label.grid(row=1,column=2,padx=10,sticky=W)

        semeseter_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 12, "bold"),state="readonly",width=20)
        semeseter_combo["values"]=("select a semester","sem-1","sem-2","sem-3","sem-4","sem-5","sem-6","sem-7","sem-8 ")
        semeseter_combo.current(0)
        semeseter_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class student information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=260, width=720, height=970)

        #student ID
        StudentID_label = Label(class_student_frame, text="studentID:", font=("times new roman", 12, "bold"), bg="white")
        StudentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        StudentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        StudentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        #student name
        StudentName_label = Label(class_student_frame, text="studentname:", font=("times new roman", 12, "bold"), bg="white")
        StudentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        StudentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        StudentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #class division
        #class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, width=12, font=("times new roman", 12, "bold"), state="readonly")
        div_combo["values"] = ("No Division","A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        

        

        


        #Roll No
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
    
        #Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        

        #combo box 
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=12,font=("times new roman", 12, "bold"),state="readonly")
        gender_combo["values"]=("male","Others","female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date of Birth
        student_dob_label = Label(class_student_frame,text="DOB:",font=("times new roman" ,12,"bold"),bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Email
        student_email_label = Label(class_student_frame,text="email:",font=("times new roman",12,"bold"),bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        student_mob_label =Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white") 
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry =ttk.Entry(class_student_frame,textvariable=self.var_mob,width=20,font=("times new roman",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        student_address_label =Label(class_student_frame,text="address:",font=("times new roman",12,"bold"),bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_address_entry =ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)
         #Teacher Name
        student_tutor_label = Label(class_student_frame,text="Teacher name:",font=("times new roman",12,"bold"),bg="white")
        student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        # Button Frame
        btn_frame = Frame(class_student_frame, bd="2", relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=200, width=715, height=50)

# Save button
        save_btn = Button (btn_frame, text="save",command=self.add_data, width=17, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        save_btn.grid(row=0, column=0,)
 
# Update button
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 12, "bold"), fg="white",bg="navyblue")
        update_btn.grid(row=0, column=1, padx=5, pady=8, sticky=W)

# Delete button
        del_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)
 
# Reset button
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        reset_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

# Button Frame 1
        btn_frame1 = Frame(class_student_frame, bd="2", relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=40)

# Take photo button

        take_photo_btn = Button(btn_frame1, text="Take a Photo Sample",command=self.generate_dataset, width=35, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")

        take_photo_btn.grid(row=0, column=0, padx=5, pady=10, sticky=W)

# Update photo button
        update_photo_btn = Button(btn_frame1, text="Update a Photo Sample", width=35, font=("verdana", 10, "bold"), fg="white", bg="navyblue")
        update_photo_btn.grid(row=0, column=1, padx=5, pady=10, sticky=W)


       
        

       
       






#RIGHT FRAME
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="student details",font= ("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=660,height=580)
        img_right = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\th (2).jpeg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lb3 = Label(right_frame, image=self.photoimg_right)

        f_lb3.place(x=5, y=0, width=720, height=130)
        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font= ("times new roman",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=135,width=710,height=70)

        #Phone Number
        search_label = Label(search_frame,text="Search by:",font= ("times new roman",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        #self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,width=12,font= ("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("select","Roll_no","phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        #self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,width=12,font= ("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="search",width=10,font= ("times new roman",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,text="show all",width=10,font= ("times new roman",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=630,height=350)
        
        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="studentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="roll_no")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("teacher",text="teacher")
        self.student_table.heading("photo",text="PhotoSamplestatus")
        self.student_table["show"]="headings"

        # Set Width of Colums 
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
   

   # ==================Function Decleration==============================    
         
    def add_data(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
         else:
            messagebox.showinfo("success","data uploaded")
            try:
                conn = mysql.connector.connect(user='root', password='Lbnagar@1786',host='localhost',database="table1",port=3306)
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                 (self.var_dep.get(),
                  self.var_course.get(),
                  self.var_year.get(),
                  self.var_semester.get(),
                  self.var_std_id.get(),
                  self.var_std_name.get(),
                  self.var_div.get(),
                  self.var_roll.get(),
                  self.var_gender.get(),
                  self.var_dob.get(),
                  self.var_email.get(),
                  self.var_mob.get(),
                  self.var_address.get(),
                  self.var_teacher.get(),
                  self.var_radio1.get()),)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
   # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='Lbnagar@1786',host='localhost',database='table1',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
   #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mob.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
   
   # ========================================Update Function==========================
    def update_data(self):
      if (
        self.var_dep.get() == "Select Department"
        or self.var_course.get == "Select Course"
        or self.var_year.get() == "Select Year"
        or self.var_semester.get() == "Select Semester"
        or self.var_std_id.get() == ""
        or self.var_std_name.get() == ""
        or self.var_div.get() == ""
        or self.var_roll.get() == ""
        or self.var_gender.get() == ""
        or self.var_dob.get() == ""
        or self.var_email.get() == ""
        or self.var_mob.get() == ""
        or self.var_address.get() == ""
        or self.var_teacher.get() == ""
       ):
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try:
            Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if Update:
                conn = mysql.connector.connect(
                    user="root", password="Lbnagar@1786", host="localhost", database="table1", port=3306
                )
                mycursor = conn.cursor()
                
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_year.get(),
                                                                                    self.var_semester.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_std_name.get(),
                                                                                    self.var_div.get(),
                                                                                    self.var_roll.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_dob.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_teacher.get(),
                                                                                    self.var_radio1.get()
                                                                                
                                                                                    
                ))
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
  #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='Lbnagar@1786',host='localhost',database='table1',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
   # #Reset Function 
    def reset_data(self):
        
        self.var_dep.set("select department")
        self.var_course.set("select course")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("a")
        self.var_roll.set("")
        self.var_gender.set("male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mob.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    """def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='2912002',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)"""
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if (
          self.var_dep.get() == "Select Department"
          or self.var_course.get() == "Select Course"
          or self.var_year.get() == "Select Year"
          or self.var_semester.get() == "Select Semester"
          or self.var_std_id.get() == ""
          or self.var_std_name.get() == ""
          or self.var_div.get() == ""
          or self.var_roll.get() == ""
          or self.var_gender.get() == ""
          or self.var_dob.get() == ""
          or self.var_email.get() == ""
          or self.var_mob.get() == ""
          or self.var_address.get() == ""
          or self.var_teacher.get() == ""
    ):
           messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
             
                  conn = mysql.connector.connect(user="root", password="Lbnagar@1786", host="localhost", database="table1", port=3306)
                  my_cursor = conn.cursor()
                  my_cursor.execute("select * from student")
                  myresult=my_cursor.fetchall()
                  id=0
                  for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Name=%s,dep=%s,course=%s,year=%s,semester=%s,division=%s,roll=%s,gender=%s,dob=%s,phone=%s,address=%s,email=%s,teacher=%s,photosamplle=%s where student_id=%s",(
                                                                             self.var_dep.get(),
                                                                             self.var_course.get(),
                                                                             self.var_year.get(),
                                                                             self.var_semester.get(),
                                                                             self.var_std_name.get(),
                                                                             self.var_div.get(),
                                                                             self.var_roll.get(),
                                                                             self.var_gender.get(),
                                                                             self.var_dob.get(),
                                                                             self.var_email.get(),
                                                                             self.var_mob.get(),
                                                                             self.var_address.get(),
                                                                             self.var_teacher.get(),
                                                                             self.var_radio1.get(),
                                                                             self.var_std_id.get()
                
))

                  conn.commit()
                  self.fetch_data()
                  self.reset_data()
                  conn.close() 

#part of open cv2
                  face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                  def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                  cap=cv2.VideoCapture(0)
                  img_id=0
                  while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        
                        face=cv2.resize(face_croped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                  cap.release()
                  cv2.destroyAllWindows()
                  messagebox.showinfo("Result","generating data sets completed",parent=self.root)

                   
            except Exception as es:
                      messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()