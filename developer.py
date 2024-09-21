from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lb1 = Label(self.root, text="DEVELOPERS INFO", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # Background Image
        img3 = Image.open(r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\3771873.jpg")
        img3 = img3.resize((1530, 790), Image.LANCZOS)  # Adjusted to match window height
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=45, width=1530, height=790)

        # Add a styled text label
        self.intro_label = Label(self.root, text="", font=("Helvetica", 14, "italic"), bg="black", fg="#00FF00", wraplength=1000, justify="left", padx=20, pady=20)
        self.intro_label.place(x=250, y=80, width=1000, height=500)
        
        # Social Media Icons
        self.add_social_media_icons()

        # Add typing effect
        self.add_intro_text()

    def add_intro_text(self):
        # Styled text
        self.text = (
    "As a Computer Science Engineering student, I have developed an attendance monitoring system using face recognition with deep learning.\n"
    "This project prominently features a fully functioning GUI, developed using Tkinter. I utilized OpenCV and dlib libraries for face recognition, "
    "while MySQL was employed for database management.\n"
    "The project incorporates several libraries:\n"
    "- Tkinter: For creating the graphical user interface (GUI).\n"
    "- PIL (Pillow): For image processing tasks.\n"
    "- cv2 (OpenCV): For computer vision tasks, such as face recognition.\n"
    "- numpy: For handling numerical operations.\n"
    "- mysql.connector: For database connectivity.\n"
    "- datetime: For managing date and time operations.\n"
    "- webbrowser: For opening URLs from the application.\n"
    "- face_recognition: For the core face recognition functionality.\n\n"
    "I invite you to follow me on the provided social media handles. I would be delighted to hear any modifications or innovative ideas you might have "
    "for this project, and I will definitely consider your suggestions.\n\nThank you!"
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

    def add_social_media_icons(self):
        # Define the paths for your social media icons
        icons = {
            'Instagram': r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\instagram-logo.png",
            'LinkedIn': r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\linkedIn_PNG8.png",
            'Gmail': r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\Gmail-Logo.png",
            'GitHub': r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\github.jpeg",
            'Credly': r"C:\Users\Abdul Raqeeb\OneDrive\Desktop\mini project\mini project - Copy\images\credly.png"
        }
        
        # Define URLs
        urls = {
            'Instagram': 'https://www.instagram.com/abdul_rafi143/profilecard/?igsh=MWJsZ2ZmOG04aWx3NA==',
            'LinkedIn': 'https://www.linkedin.com/in/yourusername',
            'Gmail': 'mailto:mohdadbulrafi17@gmail.com',
            'GitHub': 'https://github.com/rafiabdul143/Attendance-monitoring-system-based-on-facial-recognition-using-deep-learning-and-python-',
            'Credly': 'https://www.credly.com/users/abdul-rafi.6d3fc463/edit'
        }
        
        # Position the icons at the bottom of the window
        x_start = 500
        y_start = 680  # Positioning them near the bottom of the window
        icon_size = (80, 80)  # Size of the icons

        for i, (name, path) in enumerate(icons.items()):
            img = Image.open(path)
            img = img.resize(icon_size, Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            btn = Button(self.root, image=photo, command=lambda url=urls[name]: webbrowser.open(url))
            btn.image = photo  # Keep a reference to avoid garbage collection
            btn.place(x=x_start + i * 100, y=y_start, width=icon_size[0], height=icon_size[1])

if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()
