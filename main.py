from tkinter import *
from PIL import Image, ImageTk
import socket
import mysql.connector
import datetime

class Login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("JUST READ")
        self.root.geometry('1354x750')

        load = Image.open("1.jpg")
        load = load.resize((1350, 720), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = Label(self.root, image=self.render)
        img.place(x=0, y=0)

##################################################################################################################################################################
        def new_label():
            db = mysql.connector.connect(host="localhost", user="root", password="", database="read", port="3307")
            cu = db.cursor()
            cg = c.get()
            dg = d.get()
            print(cg)
            print(dg)
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer IP Address is:" + IPAddr)
            date = datetime.datetime.now()
            print(date)
            age = int(dg)
            if age<10:
                sql = "insert into userdetails01 values(%s, %s, %s, %s)"
                values = (cg, dg, IPAddr, date)
                cu.execute(sql, values)
                db.commit()
                home1()
            else:
                sql = "insert into userdetails02 values(%s, %s, %s, %s)"
                values = (cg, dg, IPAddr, date)
                cu.execute(sql, values)
                db.commit()
                home2()

##################################################################################################################################################################
        def home1():
            self.root2 = Toplevel()
            self.root2.geometry('1080x608')
            self.root2.configure(bg="#016F35")
            self.bg = PhotoImage(file="home1.png")
            lbl_1 = Label(self.root2, image=self.bg)
            lbl_1.place(x=0, y=0)

            story1 = Button(self.root2, text="LAZY JOHN", command=Lazyjohn, font=('Montserrat', 17, "bold"),
                             bg="white", border=0, fg="black", cursor="hand2", activebackground="white",
                             activeforeground="white").place(x=180, y=100, width="700")
            story2 = Button(self.root2, text="THE DOG AND THE BONE", command=Tdtb, font=('Montserrat', 17, "bold"), bg="white",
                           border=0, fg="black", cursor="hand2", activebackground="white",
                           activeforeground="white").place(x=180, y=160, width="700")
            story3 = Button(self.root2, text="THE FOX AND THE GRAPES", command=Tftg, font=('Montserrat', 17, "bold"),
                           bg="white", border=0, fg="black", cursor="hand2", activebackground="white",
                           activeforeground="#F4E147").place(x=180, y=220, width="700")
            story4 = Button(self.root2, text="THE HARE AND THE TORTOISE", command=Thtt, font=('Montserrat', 17, "bold"),
                            bg="white", border=0, fg="black", cursor="hand2", activebackground="white",
                            activeforeground="#F4E147").place(x=180, y=280, width="700")
            story5 = Button(self.root2, text="THE THIRSTY CROW", command=Ttc, font=('Montserrat', 17, "bold"), bg="white",
                           border=0, fg="black", cursor="hand2", activebackground="#F4E147",
                           activeforeground="#F4E147").place(x=180, y=340, width="700")

##################################################################################################################################################################
        def home2():
            self.root2 = Toplevel()
            self.root2.geometry('1080x608')
            self.root2.configure(bg="#016F35")
            self.bg = PhotoImage(file="home2.png")
            lbl_1 = Label(self.root2, image=self.bg)
            lbl_1.place(x=0, y=0)
            # self.psl=Label(self.root2,text="WELCOME TO PSL INFO DSEK",font=('Montserrat bold',32),bg="#F4E147",border=0,fg="black",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=420,y=100)
            # self.psldash=Label(self.root2,text="WELCOME TO PSL INFO DSEK",font=('Montserrat bold',32),bg="#F4E147",border=0,fg="black",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=420,y=100)

            poem1 = Button(self.root2, text="The JESTER IN THE TRENCH", command=p1, font=('Montserrat', 17, "bold"),
                             bg="white", border=0, fg="black", cursor="hand2", activebackground="white",
                             activeforeground="white").place(x=180, y=100, width="700")
            poem2 = Button(self.root2, text="THE TRUE ENCOUNTER", command=p2, font=('Montserrat', 17, "bold"),
                           bg="white",
                           border=0, fg="black", cursor="hand2", activebackground="white",
                           activeforeground="white").place(x=180, y=160, width="700")
            poem3 = Button(self.root2, text="GHOST IN LOVE", command=p3, font=('Montserrat', 17, "bold"),
                           bg="white", border=0, fg="black", cursor="hand2", activebackground="white",
                           activeforeground="#F4E147").place(x=180, y=220, width="700")
            poem4 = Button(self.root2, text="RECONCILIATION", command=p4,
                            font=('Montserrat', 17, "bold"),
                            bg="white", border=0, fg="black", cursor="hand2", activebackground="white",
                            activeforeground="#F4E147").place(x=180, y=280, width="700")
            poem5 = Button(self.root2, text="A PRAYER", command=p5, font=('Montserrat', 17, "bold"),
                           bg="white",
                           border=0, fg="black", cursor="hand2", activebackground="#F4E147",
                           activeforeground="#F4E147").place(x=180, y=340, width="700")

##################################################################################################################################################################
        def Lazyjohn():
            self.root6 = Toplevel()
            self.root6.geometry("700x300+250+100")
            self.root6.configure(bg="orange")
            f1 = open("Lazy John.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="Lazy John", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=300, y=10)
            self.psl = Label(self.root6, text="-----------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=300, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=70, y=70)

##################################################################################################################################################################
        def Tdtb():
            self.root6 = Toplevel()
            self.root6.geometry("700x300+250+100")
            self.root6.configure(bg="orange")
            f1 = open("The Dog and the Bone.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="The Dog and The Bone", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=220, y=10)
            self.psl = Label(self.root6, text="--------------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=220, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=70, y=70)

##################################################################################################################################################################
        def Tftg():
            self.root6 = Toplevel()
            self.root6.geometry("700x300+250+100")
            self.root6.configure(bg="orange")
            f1 = open("The Fox and The Grapes.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="The Fox and The Grapes", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=210, y=10)
            self.psl = Label(self.root6, text="----------------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=210, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=70, y=70)

##################################################################################################################################################################
        def Thtt():
            self.root6 = Toplevel()
            self.root6.geometry("700x300+250+100")
            self.root6.configure(bg="orange")
            f1 = open("The Hare and the Tortoise.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="The Hare and Tho Tortoise", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=200, y=10)
            self.psl = Label(self.root6, text="---------------------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=200, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=70, y=70)

##################################################################################################################################################################
        def Ttc():
            self.root6 = Toplevel()
            self.root6.geometry("700x300+250+100")
            self.root6.configure(bg="orange")
            f1 = open("The Thirsty Crow.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="The Thirsty Crow", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=250, y=10)
            self.psl = Label(self.root6, text="-----------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=250, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=70, y=70)

##################################################################################################################################################################
        def p1():
            self.root6 = Toplevel()
            self.root6.geometry("600x400")
            self.root6.configure(bg="orange")
            f1 = open("The jester in the trench by Leon Gellert.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="Poet - Leon Gellert", font=('Britannic Bold', 20), bg="orange", border=0,fg="darkred").place(x=200, y=10)
            self.psl = Label(self.root6, text="-------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=200, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=90, y=70)

##################################################################################################################################################################
        def p2():
            self.root6 = Toplevel()
            self.root6.geometry("600x400")
            self.root6.configure(bg="orange")
            f1 = open("The true encounter by St. Vincent Millay.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="Poet - St. Vincent Millay", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=170, y=10)
            self.psl = Label(self.root6, text="---------------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=170, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=170, y=70)

##################################################################################################################################################################
        def p3():
            self.root6 = Toplevel()
            self.root6.geometry("600x400")
            self.root6.configure(bg="orange")
            f1 = open("Ghost in love by  Vachel Lindsay.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="Poet - Vachel Lindsay", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=180, y=10)
            self.psl = Label(self.root6, text="------------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=180, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=150, y=70)

##################################################################################################################################################################
        def p4():
            self.root6 = Toplevel()
            self.root6.geometry("600x400")
            self.root6.configure(bg="orange")
            f1 = open("Reconciliation by Walt Whitman.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="Poet - Walt Whitman", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=180, y=10)
            self.psl = Label(self.root6, text="----------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=180, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=30, y=70)

##################################################################################################################################################################
        def p5():
            self.root6 = Toplevel()
            self.root6.geometry("600x400")
            self.root6.configure(bg="orange")
            f1 = open("A Prayer by Claude McKay.txt", "r")
            c = f1.read()
            self.psl = Label(self.root6, text="Poet - Claude McKay", font=('Britannic Bold', 20), bg="orange", border=0, fg="darkred").place(x=180, y=10)
            self.psl = Label(self.root6, text="----------------------------------", font=('Script MT Bold', 15), bg="orange", border=0, fg="darkred").place(x=180, y=40)
            self.psl = Label(self.root6, text=c, font=('Montserrat', 15), bg="orange", border=0, fg="darkred",
                             cursor="hand2", activebackground="green", activeforeground="green").place(x=30, y=70)

##################################################################################################################################################################
        un = Label(self.root, text="NAME", font=('Mowntserrat Semibold', 12), bg="#1C170C", border=0,
                          fg="white", cursor="hand2", activebackground="#39065D", activeforeground="#39065D").place(x=400, y=575)

        pw = Label(self.root, text="AGE", font=('Montserrat Semibold', 12), bg="#1C170C", border=0,
                          fg="white", cursor="hand2", activebackground="#39065D", activeforeground="#39065D").place(x=850, y=575)

        c = Entry(root)
        c.place(x=400, y=600)
        c.focus()

        d = Entry(root)
        d.place(x=850, y=600)
        d.focus()

        login_1 = Button(self.root, text="ENTER", command=new_label, font=('Consolas', 13, "bold"), bg="#F4E147",
                         border=0, fg="black", cursor="hand2", activebackground="#F4E147",
                         activeforeground="#F4E147").place(x=600, y=700, width="150")

##################################################################################################################################################################
if __name__ == "__main__":
    root=Tk()
    app=Login_page(root)
    root.mainloop()