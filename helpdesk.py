from tkinter import *
from PIL import Image, ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox

# Developer's email information
developer_email = "mohdabdulrafi17@gmail.com"

class Helpdesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1 = Label(self.root, text="HELPDESK", font=("times new roman", 35, "bold"), bg="black", fg="RED")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # Background image
        img3 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\405901475.jpg")
        img3 = img3.resize((1530, 790), Image.LANCZOS)  # Adjusted height to match window height
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=45, width=1530, height=790)

     

        # Form elements
          # Frame for the form elements
         # Frame for the form elements
        form_frame = Frame(bg_img, bg="black")
        form_frame.place(x=30, y=80, width=480, height=600)  # Adjusted x, y, width, height as needed

        # Form elements
        self.name_label = Label(form_frame, text="Name:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.name_entry = Entry(form_frame, font=("times new roman", 15),width=28)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.email_label = Label(form_frame, text="Email:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.email_entry = Entry(form_frame, font=("times new roman", 15), width=28)  
        self.email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.issue_label = Label(form_frame, text="Issue Description:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.issue_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

        self.issue_entry = Text(form_frame, font=("times new roman", 15), width=28, height=16)  # Reduced width and height
        self.issue_entry.grid(row=2, column=1, padx=10, pady=10, rowspan=2, sticky="w")
        self.password_label = Label(form_frame, text="Email Password:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.password_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.password_entry = Entry(form_frame, font=("times new roman", 15),width=28, show="*")  # Masked input
        self.password_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        submit_btn = Button(form_frame, text="Submit Ticket", command=self.raise_ticket, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        submit_btn.grid(row=6, column=0, columnspan=2, pady=20)

        # Add a styled text label
        self.intro_label = Label(bg_img, text="", font=("Helvetica", 14, "italic"), bg="black", fg="#00FF00", wraplength=800, justify="left", padx=20, pady=20)
        self.intro_label.place(x=600, y=80, width=880, height=600)

        
        # Add typing effect
        self.add_intro_text()

    def add_intro_text(self):
        # Styled text
        self.text = ( "INSTRUCTIONS FOR USER\n"
    "Steps to Use App Passwords:\n"
    "1. **Enable 2-Step Verification**:\n"
    "   - Go to your Google Account Security page.\n"
    "   - In the 'Signing in to Google' section, look for 2-Step Verification.\n"
    "   - Click on it and follow the steps to enable 2-Step Verification if it's not already enabled.\n\n"
    "2. **Generate an App Password**:\n"
    "   - After enabling 2-Step Verification, go back to your Google Account Security.\n"
    "   - Under 'Signing in to Google', you'll see an option for App Passwords.\n"
    "   - Click on App Passwords.\n"
    "   - Choose Mail as the app and Other for the device, then enter a name like 'Python Script'.\n"
    "   - Google will generate a 16-character App Password.\n"
    "   - Use this generated password instead of your regular Google account password in the script.\n\n"
    "3. **Update Your Script**:\n"
    "   - Replace the password field in your script with the newly generated App Password."
)

        
        self.index = 0  # Starting index for the text
        self.typing_effect()  # Start the typing effect

    def typing_effect(self):
        if self.index < len(self.text):
            # Add one character at a time to the label text
            self.intro_label.config(text=self.text[:self.index+1])
            self.index += 1
            # Call this method again after a delay
            self.root.after(50, self.typing_effect)  # Adjust delay to change typing speed

    # Function to raise a ticket
    def raise_ticket(self):
        user_name = self.name_entry.get()
        user_email = self.email_entry.get()
        issue = self.issue_entry.get("1.0", END).strip()
        email_password = self.password_entry.get()

        if user_name == "" or user_email == "" or issue == "" or email_password == "":
            messagebox.showerror("Input Error", "All fields are required.")
            return

        # Save ticket to a file
        ticket = f"Name: {user_name}\nEmail: {user_email}\nIssue: {issue}\n\n"
        with open("tickets.txt", "a") as file:
            file.write(ticket)

        # Send email notification to developer
        subject = f"New Helpdesk Ticket from {user_name}"
        body = f"User: {user_name}\nEmail: {user_email}\nIssue: {issue}"
        self.send_email(subject, body, email_password)

        # Display a confirmation message box
        messagebox.showinfo("Ticket Submitted", "Thank you for your submission! Please hold on while our developers review and resolve your issue. We will get back to you soon.")

    # Function to send email to developer
    def send_email(self, subject, body, email_password):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_entry.get()  # Sender's email from the form
            msg['To'] = developer_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            # SMTP server setup (for Gmail)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_entry.get(), email_password)

            # Send email
            text = msg.as_string()
            server.sendmail(self.email_entry.get(), developer_email, text)
            server.quit()

            print("Ticket has been emailed to the developer!")
        except Exception as e:
            print(f"Failed to send email. Error: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Helpdesk(root)
    root.mainloop()
