import hashlib, uuid
from tkinter import*
from tkinter import messagebox
import tkinter
window = Tk()
window.title("Sunshine Nursery")
window.resizable(False, False)
##DEBUG PASSWORD GEN##
def gen(DEBUG_username="NULL",DEBUG_password="password"):
    DEBUG_hash = uuid.uuid4().hex
    print(DEBUG_username+","+hashlib.sha512(DEBUG_password.encode('utf-8') + DEBUG_hash.encode('utf-8')).hexdigest()+","+DEBUG_hash)
#gen("Evan")
#gen("Dylan","qwerty")
#gen("Kyle")
    
##DEBUG PASSWORD END##

## START USER PROCESSING ##
Users = {}
ERROR_Increament = {}
with open('userdb.dy', 'r') as f:
    x = f.readlines()
    for val in x :
        a,b,c = val.split(",")
        nme = a.lower()
        Users[nme]={}
        Users[nme]["Name"] = a
        Users[nme]["Salt"] = c 
        Users[nme]["Pass"] = b
        ERROR_Increament[nme] = 0
## END USER PROCESSING ##

#hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
#print(hashed_password)

LANGUAGE_COMINGSOON_ENGLISH = "Coming Soon"
LANGUAGE_HELP_PAGE_HEADER_ENGLISH = "Help Page"
LANGUAGE_LOGIN_PAGE_HEADER_ENGLISH = "Log In"




BG = '#2ab3f9'
img = PhotoImage(width=262, height=50)
img2 = PhotoImage(width=82, height=50)
pages = []
def button():
    print("ree")
def showElement(ele):
    global pages
    for w in pages:
        w.place_forget()
        for widget in w.winfo_children():
            if isinstance(widget, tkinter.Entry):
                widget.delete(0, "end")
    ele.place(x=270,y=0)
def CreateButton(c, t,img,cb=button):

    localbutton = Button(c, text=t,image=img,
                  bg="#2ab3f9",fg="white", font=("Seoge UI", 8)
                         ,command =cb,compound="c")
    return localbutton
def createPage(bgg="white"):
    global pages
    localPage = Frame(canvas,width=430, height=642, bg=bgg)
    pages.append(localPage)
    return localPage

bg_image = PhotoImage(file ="bg.png")


canvas = Canvas(width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)
canvas.create_image(0, 0, image = bg_image, anchor = NW)

Sidebar = Canvas(canvas,width = 200, height = 200, bg = '#2ab3f9',
                 highlightthickness=0)
Sidebar.place(x=0,y=150)
window.geometry("700x642")

##User Page##
userPage = createPage("")

##Login Page##
Login = createPage("")
messg = Label(Login, text="Password",width=50)
messg.grid(row=6,columnspan=2)
def destoryPage():
    global window
    window.destroy  ()
    messagebox.showinfo("Program Locked", "Contact your admin to restore your rights to acess to the program.")
def printMessage(txt = ""):
    global messg
    messg.configure(text=txt)
    messg.update()
def LoginCommand():
    global e1
    global e2
    global Users
    global ERROR_Increament
    print("Login Attempt")
    try:
        user = Users[e1.get().lower()]
        print(user)
        passwordgen = hashlib.sha512(e2.get().encode('utf-8') + user["Salt"].rstrip().encode('utf-8')).hexdigest()
 
        if passwordgen == user["Pass"]:
            printMessage("User in")
        else:
            error()
    except:
        try:
            user2 = e1.get().lower()
            ERROR_Increament[user2] = ERROR_Increament[user2] + 1
            print(ERROR_Increament[user2])
            printMessage(str(ERROR_Increament[user2]) + "/3 attempts remaining")
            if ERROR_Increament[user2] > 3:
                destoryPage()
        except:
             print("NULL")
e = Label(Login, bg="#f442c2",width=20,fg="black",text=LANGUAGE_LOGIN_PAGE_HEADER_ENGLISH,font=("Helvetica", 32))

e.grid(row=0,columnspan=3)
Label(Login, text="Username",width=15).grid(row=1)
Label(Login, text="Password",width=15).grid(row=2)
e1 = Entry(Login,width=35)
e2 = Entry(Login,show="*",width=35)
e1.grid(row=1, column=1,columnspan=1)
e2.grid(row=2, column=1,columnspan=1)
submitLogin = Button(Login, text="Login",image=img,
                  bg="#2ab3f9",fg="white", font=("Seoge UI", 8)
                         ,command =LoginCommand,compound="c")
submitLogin.grid(row=3,columnspan=2,padx=5, pady=5)

##Help Page##
helpPage = createPage("")
w = Label(helpPage, bg="#f442c2",fg="black",text=LANGUAGE_HELP_PAGE_HEADER_ENGLISH,font=("Helvetica", 32))
w.grid(row=0,columnspan=3)


##Coming Soon Page##
CommingSoonPage = createPage("")
w = Label(CommingSoonPage, bg="#8888ff",fg="black",text=LANGUAGE_COMINGSOON_ENGLISH,font=("Helvetica", 32))
w.grid(row=0,columnspan=3)


##ADMIN HEADER##
lbl = Label(Sidebar,text="Admin",bg = BG).grid(row=0, column=0,columnspan=3)
CreateButton(Sidebar,"Add User",img2,lambda: showElement(CommingSoonPage)).grid(row=1, column=0)
CreateButton(Sidebar,"Edit User",img2,lambda: showElement(CommingSoonPage)).grid(row=1, column=1)
CreateButton(Sidebar,"Remove User",img2,lambda: showElement(CommingSoonPage)).grid(row=1, column=2)
##OTHER BUTTONS##
CreateButton(Sidebar,"User",img,lambda: showElement(Login)).grid(row=2, column=0,columnspan=3)
CreateButton(Sidebar,"Help",img,lambda: showElement(helpPage)).grid(row=3, column=0,columnspan=3)


window.mainloop()
