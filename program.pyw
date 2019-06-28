from user import *
from metroframework import *
import os
import ctypes
from language import language as language

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('python-sunshinenursery')

if __name__ == "__main__":
    try:
        from Tkinter import Tk
        from tkMessageBox import showinfo
    except ImportError:
        from tkinter import Tk
        from tkinter.messagebox import showinfo

print(Users())

User("James")
User("Chris")


print(Users())

root = Tk()

initialize_font()

page = Container(root, bg="white", bd=1, padx=10, pady=10)
page.pack()
root.title(language["PROGRAM_NAME"])

root.iconbitmap(os.path.dirname(os.path.realpath(__file__))+r'\program-icon.ico')

row = Frame(page)
row.pack()

# N A V I G A T I O N START

pixel = tk.PhotoImage(width=1, height=1)
metro_labelframe = Metro_LabelFrame(row, title="User Commands")
metro_labelframe.configure(width=120)

#Log In#
def loginbuttonpressed():
	showinfo("search command", "searching")
Button_SignIn = Metro_Button(metro_labelframe, language["SIGN_IN"], "#60a917")
Button_SignIn.pack( padx=0,pady=2)
Button_SignIn.configure(width=120, image=pixel,compound="c",command=loginbuttonpressed)



Button_Help = Metro_Button(metro_labelframe, language["HELP"], "#ff0099")
Button_Help.pack( padx=0,pady=2)
Button_Help.configure(width=120, image=pixel,compound="c")


metro_labelframe.grid( padx=10, pady=10)

# N A V I G A T I O N END
metro_panel = Primary_Panel(row, language["MESSAGE"], width=400)
metro_panel.grid(row=0,column=1)
Label(metro_panel.body, text=language["SPLAHMESSAGEOFTHEDAY"]).pack(anchor=W)

#LoginPage#
metro_panel = Info_Panel(row, language["MESSAGE"], width=400)
metro_panel.grid(row=0,column=1)
Label(metro_panel.body, text=language["SPLAHMESSAGEOFTHEDAY"]).pack(anchor=W)
Username_input = Search_Box(metro_panel,  placeholder="Username", entry_highlightthickness=0,drawButton=False)
Username_input.pack(anchor=CENTER,pady=2)
Password_input = Search_Box(metro_panel,  placeholder="Password", entry_highlightthickness=0,drawButton=False)
Password_input.pack(anchor=CENTER,pady=2)
Password_input.entry._entry.configure(show="*")
PASSWORD_INVALID_LOGIN = None




AttemptsPasswords = 5
STRING_AttemptsPasswords = StringVar()
def password_failed():
	global page
	global PASSWORD_INVALID_LOGIN
	global AttemptsPasswords
	global STRING_AttemptsPasswords
	AttemptsPasswords -= 1
	if (AttemptsPasswords == 0):
		page.destroy()
		showinfo("Program Locked", "Contact your admin to restore\nyour rights to acess to the program.")
	if (PASSWORD_INVALID_LOGIN is None):
		PASSWORD_INVALID_LOGIN=Label(metro_panel, textvariable=STRING_AttemptsPasswords,fg="red")
		PASSWORD_INVALID_LOGIN.pack(anchor=S)
	STRING_AttemptsPasswords.set(language["loginfailed"].replace("(0)",str(AttemptsPasswords)))

def loginbuttonpressed():
	usnme=Users(Username_input.entry.get())
	if (usnme != 0):
		print(usnme._password)
		state = (usnme.authPassword(Password_input.entry.get(),0))
		if (state):
			print("user logged in")
		else:
			password_failed()
		return
	password_failed()
	
Log_Button_SignIn = Metro_Button(metro_panel, language["SIGN_IN"], "#60a917")
Log_Button_SignIn.pack( padx=0,pady=2)
Log_Button_SignIn.configure(width=120, image=pixel,compound="c",command=loginbuttonpressed)

row = Frame(page)
row.pack(pady=4, fill=X)



root.mainloop()
