from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
import sqlite3
from tkinter import messagebox

class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        ###############     background colours
        left_lbl=Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl=Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        ####################       frames
        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title=Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        email=Label(login_frame, text="Email Address", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email=Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_=Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
        self.txt_pass_=Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame, cursor="hand2", command=self.register_window, text="Register new account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)

        btn_login=Button(login_frame, cursor="hand2", text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=250, y=380, width=180, height=40)

        ###############     clock
        self.lbl=Label(self.root,text="\nRishav's Clock", font=("Book Antiqua", 25, "bold"),fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        #self.clock_image()
        self.working()

    def register_window(self):
        self.root.destroy()
        import register


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error", "Please enter both email and password", parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="employee2.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=? AND password=?", (self.txt_email.get(), self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid username and password", parent=self.root)
                    
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    import dashboard
                    
                con.close()   


            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        


    def clock_image(self, hr, min_, sec_):
        clock=Image.new("RGB", (400, 400), (8,25, 35))
        draw=ImageDraw.Draw(clock)

        
        ################   for clock img
        bg=Image.open("image/clock_img.jfif")
        bg=bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        

        origin=200, 200
        ###################    For hour line img
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="black", width=4)

        ###################    For minute line img
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="blue", width=3)

        ###################    For second line img
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="green", width=4)


        draw.ellipse((195, 195, 210, 210),fill="black")
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        #print(h, m, s)
        #print(hr, min_, sec_)
        self.clock_image(hr, min_, sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)
        




root=Tk()
obj=Login_window(root)
root.mainloop()
