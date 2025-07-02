#required modules
from tkinter import *
import speedtest
import textblob.download_corpora

root=Tk()
root.title("Internet-Speed text")
root.geometry("360x600")
root.resizable(False,False)
root.config(bg="#1a212d")


#Check

def Check():

    test=speedtest.Speedtest()
    uploading_speed=round(test.upload()/(1024*1024),2)
    upload.config(text=uploading_speed)

    downloading_speed=round(test.download()/(1024*1024),2)
    download.config(text=downloading_speed)
    Download.config(text=downloading_speed)

    servernames=[]
    test.get_servers(servernames)
    ping.config(text=test.results.ping)

#Icon
img_icon=PhotoImage(file="C:\\Users\\\Raj CH\\PycharmProjects\\Internet_Speed\\logo.png")
root.iconphoto(False,img_icon)

#Images
top=PhotoImage(file="C:\\Users\\Raj CH\\PycharmProjects\\Internet_Speed\\top (1).png")
Label(root,image=top,bg="#1a212d").pack()

Main=PhotoImage(file="C:\\Users\\Raj CH\\PycharmProjects\\Internet_Speed\\main.png")
Label(root,image=Main,bg="#1a212d").pack(pady=(40,0))


button=PhotoImage(file="C:\\Users\\Raj CH\\PycharmProjects\\Internet_Speed\\button.png")
Button=Button(root,image=button,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=Check)
Button.pack(pady=10)


#Label
Label(root,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
Label(root,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
Label(root,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)

Label(root,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)


Label(root,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=140,y=280)
Label(root,text="MBPS",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)


ping=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")

download=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")

upload=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
upload.place(x=290,y=60,anchor="center")

Download=Label(root,text="00",font="arial  40 bold",bg="#384056")
Download.place(x=185,y=350,anchor="center")





root.mainloop()


