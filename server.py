import tkinter
import tkinter.font
from tkinter import *
from urllib.request import urlopen, URLError, HTTPError
def url_check():
    try:
        link=urlopen(str(url.get()))
    except HTTPError:
        r="Server Down"
    except URLError:
        r="Server Down"
    else:
        r="Server Found!"
    result.set(r)
root=Tk()
root.title("Server Status Checker.")
root.geometry("600x250")
root.configure(bg="black")
result=StringVar() 
name=Label(root, text="Enter the URL:",background="light green").place(x=30,y=50)
url=Entry(root,width=50, background="white")
url.place(x=150,y=50)
checker=Button(root, text="Check", command=url_check, width=6,height=2,background="light green")
checker.place(x=515,y=50)
status=Label(root, text="Status:",background="light green").place(x=80,y=100)
res=Label(root, text=" ",textvariable=result,background="light green").place(x=150,y=100)
footer=Label(root, text="Developed by Sujithra D, 2023", font="Times 10 italic",background="light green")
footer.place(x=10,y=230)
mainloop()
