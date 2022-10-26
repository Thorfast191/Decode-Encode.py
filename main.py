from tkinter import *
import base64


window = Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title('Encode-Decode')


Heading = Label(window, text='Encode-Decode', font='arial 20 bold').pack()


msg = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

def Encode(key, massage):
    enc = []

    for i in range(len(massage)):
        key_c = key[i % len(key)]
        enc.append(chr(ord(massage[i])+ord(key_c) % 256))
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, massage):
    dec = []
    massage = base64.urlsafe_b64decode(massage).decode()

    for i in range(len(massage)):
        key_c = key[i % len(key)]
        dec.append(chr(ord(massage[i])-ord(key_c)) % 256)
        return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        result.set(Encode(private_key.get(), msg.get()))
    elif(mode.get() == 'd'):
        result.set(Decode(private_key.get(), msg.get()))
    else:
        result.set('Invalid Mode')

def Exit():
    window.destroy()

def Restart():
    msg.set = ' '
    private_key.set = ' '
    mode.set = ' '
    result.set = ' '

Label(window, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(window, font = 'arial 10', textvariable = msg, bg = 'ghost white', fg='black').place(x=290, y = 60)

Label(window, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(window, font = 'arial 10', textvariable = private_key , bg ='ghost white', fg='black').place(x=290, y = 90)

Label(window, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(window, font = 'arial 10', textvariable = mode , bg= 'ghost white', fg='black').place(x=290, y = 120)
Entry(window, font = 'arial 10 bold', textvariable = result, bg ='ghost white', fg='black').place(x=290, y = 150)

Button(window, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(window, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Restart,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(window, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

window.mainloop()