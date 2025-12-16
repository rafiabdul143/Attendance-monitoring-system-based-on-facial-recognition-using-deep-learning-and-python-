from tkinter import * 
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import csv
import os

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #================VARIABLE==========================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # first image
        img = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\students")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=800, height=200)

        # second image
        img1 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\students2")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2 = Label(self.root, image=self.photoimg1)
        f_lb2.place(x=800, y=0, width=800, height=200)

        # bg_image
        img3 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\pic6")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lb1 = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="red", fg="white")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=0, width=1500, height=650)

        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="student attendance details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=800, height=580)

        img_left = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\last1.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb3 = Label(left_frame, image=self.photoimg_left)
        f_lb3.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(left_frame, relief=RIDGE, bd=2, bg="white")
        left_inside_frame.place(x=0, y=135, width=700, height=400)  # Increase the height to 400

        # Labels and entry
        # attendanceid
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # roll_no
        rolllabel = Label(left_inside_frame, text="Roll:", font=("times new roman", 11, "bold"), bg="white")
        rolllabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        rollentry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=20, font=("times new roman", 11, "bold"))
        rollentry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # name
        namelabel = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        namelabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # attendance
        attendanceId_label = Label(left_inside_frame, text="AttendanceStatus:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.attend_combo = ttk.Combobox(left_inside_frame, width=13, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly")
        self.attend_combo["values"] = ("Status", "Present", "Absent")
        self.attend_combo.current(0)
        self.attend_combo.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        btn_frame = Frame(left_inside_frame, bd="2", relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=350, width=715, height=50)  # The buttons will now fit within the height of left_inside_frame

        # Place the buttons within btn_frame
        # Save button
        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        save_btn.grid(row=0, column=0)

        # export button
        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        update_btn.grid(row=0, column=1, padx=5, pady=8, sticky=W)
        

        # update button
        del_btn = Button(btn_frame, text="update", width=17,command=self.update_data, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # Reset button
        reset_btn = Button(btn_frame, text="reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), fg="white", bg="navyblue")
        reset_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="student attendance details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_frame, bd="2", relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # create table
        self.attendanceReport = ttk.Treeview(table_frame, column=("Id", "Roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("Id", text="Attendance ID")
        self.attendanceReport.heading("Roll", text="roll_no")
        self.attendanceReport.heading("name", text="Name")
        self.attendanceReport.heading("department", text="Department")
        self.attendanceReport.heading("time", text="Time")
        self.attendanceReport.heading("date", text="Date")
        self.attendanceReport.heading("attendance", text="Attendance")

        self.attendanceReport["show"] = "headings"

        self.attendanceReport.column("Id", width=100)
        self.attendanceReport.column("Roll", width=100)
        self.attendanceReport.column("name", width=100)
        self.attendanceReport.column("department", width=100)
        self.attendanceReport.column("time", width=100)
        self.attendanceReport.column("date", width=100)
        self.attendanceReport.column("attendance", width=100)

        self.attendanceReport.pack(fill=BOTH, expand=1)
        self.attendanceReport.bind("<ButtonRelease>", self.get_cursor_left)

    # Fetch data
    def fetchData(self, rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("", END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")), parent=self.root)
        
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", defaultextension=".csv", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")), parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",") 
                    for i in mydata:
                        exp_write.writerow(i)
                messagebox.showinfo("Data export", f"Your data is exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    #==================================UPDATE====================
    def update_data(self):
        cursor_focus = self.attendanceReport.focus()
        if cursor_focus:
            content = self.attendanceReport.item(cursor_focus)
            selected_row = content["values"]

            # Get the index of the selected row
            index = self.attendanceReport.index(cursor_focus)

            # Update the data in mydata list
            mydata[index] = [
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            ]

            # Update the data in the Treeview widget
            self.attendanceReport.item(cursor_focus, values=(
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            ))
            messagebox.showinfo("Success", "Data Updated Successfully")
        else:
            messagebox.showerror("Error", "Please select a record to update")



    

    def get_cursor_left(self, event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_atten_id.set(data[0]),
        self.var_atten_roll.set(data[1]),
        self.var_atten_name.set(data[2]),
        self.var_atten_dep.set(data[3]),
        self.var_atten_time.set(data[4]),
        self.var_atten_date.set(data[5]),
        self.var_atten_attendance.set(data[6]) 

    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set("") 

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
