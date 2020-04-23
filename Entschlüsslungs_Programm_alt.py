# Das hier ist die Ursprüngliche Version ohne die Umsetzung von Buchstaben

from tkinter import *
import tkinter as tk
import math

root = tk.Tk()
Height = 600
Width = 800
root.title("EnkryptenAPP")

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()


def close():
    root.destroy()


def open():
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame_site_titel = tk.Frame(root, bg="white", bd=2)
    frame_site_titel.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame_site_primzahl = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_primzahl2 = tk.Frame(root, bg="white", bd=2)
    frame_site_primzahl2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.1, anchor="n")

    frame_site_startpunkt = tk.Frame(root, bg="white", bd=2)
    frame_site_startpunkt.place(relx=0.5, rely=0.7, relwidth=0.5, relheight=0.1, anchor="n")

    frame_button_weiter = tk.Frame(root, bg="white", bd=2)
    frame_button_weiter.place(relx=0.5, rely=0.85, relwidth=0.3, relheight=0.1, anchor="n")

    label_seite2 = tk.Label(frame_site_titel, text="Geben sie nun 2 Primzahlen und 1 Startpunkt ein", bg="#00001a",
                            fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=1, relheight=1)

    label_seite2 = tk.Label(frame_site_primzahl, text="Primzahl 1:", bg="#00001a", fg="white",
                            font=("Alegra", 28))
    label_seite2.place(relwidth=0.4, relheight=1)

    label_seite2_primzahl1 = tk.Label(frame_site_primzahl2, text="Primzahl 2:", bg="#00001a", fg="white",
                                      font=("Alegra", 28))
    label_seite2_primzahl1.place(relwidth=0.4, relheight=1)

    label_seite2_startpunkt = tk.Label(frame_site_startpunkt, text="Startzahl :", bg="#00001a", fg="white",
                                       font=("Alegra", 28))
    label_seite2_startpunkt.place(relwidth=0.4, relheight=1)

    global eingabe_seite2_primzahl1
    eingabe_seite2_primzahl1 = StringVar()
    entry = tk.Entry(frame_site_primzahl, bg="#00001a", font=("Alegra", 30), fg="white",
                     textvariable=eingabe_seite2_primzahl1)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    global eingabe_seite2_primzahl2
    eingabe_seite2_primzahl2 = StringVar()
    entry = tk.Entry(frame_site_primzahl2, bg="#00001a", font=("Alegra", 30), fg="white", textvariable=eingabe_seite2_primzahl2)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    global eingabe_seite2_startpunkt
    eingabe_seite2_startpunkt = StringVar()
    entry = tk.Entry(frame_site_startpunkt, bg="#00001a", font=("Alegra", 30), fg="white",
                     textvariable=eingabe_seite2_startpunkt)
    entry.place(relx=0.4, relwidth=0.6, relheight=1)

    button_weiter = tk.Button(frame_button_weiter, text="Weiter", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,
                              command=open1)
    button_weiter.place(relwidth=1, relheight=1)

    mainloop()


def open1():
    menue_pic = PhotoImage(file="menue.png")
    canvas.pack()
    background_image = tk.PhotoImage(file="Sunset.png")
    background_label_huch = tk.Label(root, image=background_image)
    background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, bg="white", bd=2)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

    frame1 = tk.Frame(root, bg="white", bd=2)
    frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

    frame2 = tk.Frame(root, bg="white", bd=2)
    frame2.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1, anchor="n")

    frame3 = tk.Frame(root, bg="white", bd=2)
    frame3.place(relx=0.65, rely=0.35, relwidth=0.3, relheight=0.1, anchor="n")

    frame4 = tk.Frame(root, bg="white", bd=2)
    frame4.place(relx=0.125, rely=0.5, relwidth=0.75, relheight=0.4)

    frame5 = tk.Frame(root, bg="white", bd=2)
    frame5.place(relx=0.92, rely=0.9, relwidth=0.08, relheight=0.1)

    label2 = tk.Label(frame, bg="#00001a", fg="white", font=("Alegra", 30), text="Geben sie hier ihre Nachricht ein")
    label2.place(relwidth=1, relheight=1)

    global eingabe_nachricht
    eingabe_nachricht = StringVar()
    entry_seite_3 = tk.Entry(frame1, textvariable=eingabe_nachricht, bg="#00001a", fg="white", font=("Alegra", 30))
    entry_seite_3.place(relwidth=1, relheight=1)

    button_weiter = tk.Button(frame2, text="Verschlüsseln", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,command=Verschlüsseln)
    button_weiter.place(relwidth=1, relheight=1)

    button_weiter = tk.Button(frame3, text="Entschlüsseln", bg="#00001a", fg="white", font=("Alegra", 30), bd=1,command=Entschlüsseln)
    button_weiter.place(relwidth=1, relheight=1)

    global label_nachrichten
    label_nachrichten = tk.Text(frame4, fg="white", bg="#00001a", font=("Alegra", 25), bd=3)
    label_nachrichten.place(relwidth=1, relheight=1)

    button_menue = tk.Button(frame5, image=menue_pic, bg="#00001a", fg="white", font=("Alegra", 30), bd=1, command=open)
    button_menue.place(relwidth=1, relheight=1)

    mainloop()


def primzahl(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    quadratzahl = int(math.sqrt(n)) + 1

    for teiler in range(3, quadratzahl, 2):
        if n % teiler == 0:
            return False
    return True


def Verschlüsseln():
    q = eingabe_seite2_primzahl1.get()
    p = eingabe_seite2_primzahl2.get()
    x = eingabe_seite2_startpunkt.get()
    m = eingabe_nachricht.get()
    q = int(q)
    p = int(p)
    x = int(x)
    m = int(m)
    if not primzahl(p) or not primzahl(q):
        label_nachrichten.insert(tk.INSERT, "Geben Sie bitte echte Primzahlen ein\n")
        raise(ValueError)
    if p<32 or q<32:
        label_nachrichten.insert(tk.INSERT, "Die Primzahlen müssen grösser als 31 sein.\n")
        raise(ValueError)
    if m>(q*p):
        label_nachrichten.insert(tk.INSERT, "Geben Sie dafür höhere Primzahlen ein.\n")
        raise(ValueError)
    if p==q:
        label_nachrichten.insert(tk.INSERT, "Geben Sie 2 unterschiedliche Primzahlen ein.\n")
        raise(ValueError)

    eq = (p - 1) * (q - 1) + 1

    y = 1

    xy = x * y

    while xy != eq:
        x += 1
        y = eq / x
        y = int(y)
        xy = x * y
    globaler_schlüssel = x
    zahl1 = m ** globaler_schlüssel
    m = (zahl1 % (p * q))
    label_nachrichten.insert(tk.INSERT, "Ihre Verschlüsselte Nachricht lautet: " + (str(m) + "\n"))


def Entschlüsseln():
    q = eingabe_seite2_primzahl1.get()
    p = eingabe_seite2_primzahl2.get()
    x = eingabe_seite2_startpunkt.get()
    m1 = eingabe_nachricht.get()
    q = int(q)
    p = int(p)
    x = int(x)
    m1 = int(m1)

    if not primzahl(p) or not primzahl(q):
        label_nachrichten.insert(tk.INSERT, "Geben Sie bitte echte Primzahlen ein\n")
        raise(ValueError)
    if p<32 or q<32:
        label_nachrichten.insert(tk.INSERT, "Die Primzahlen müssen grösser als 31 sein.\n")
        raise(ValueError)
    if m1>(q*p):
        label_nachrichten.insert(tk.INSERT, "Geben Sie dafür höhere Primzahlen ein.\n")
        raise(ValueError)
    if p==q:
        label_nachrichten.insert(tk.INSERT, "Geben Sie 2 unterschiedliche Primzahlen ein.\n")
        raise(ValueError)

    eq = (p - 1) * (q - 1) + 1  # Eulersche Phi-Funktion Primzahlen
    y = 1
    y = int(y)
    xy = x * y

    while xy != eq:
        x += 1
        y = eq / x
        y = int(y)
        xy = x * y

    privater_schlüssel = y
    zahl2 = m1 ** privater_schlüssel
    m1 = (zahl2 % (p * q))
    label_nachrichten.insert(tk.INSERT, "Ihre Entschlüsselte Nachricht lautet: " + (str(m1) + "\n"))


background_image = tk.PhotoImage(file="Sunset.png")
background_label_huch = tk.Label(root, image=background_image)
background_label_huch.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="white", bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

frame1 = tk.Frame(root, bg="white", bd=2)
frame1.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

frame_button_yes = tk.Frame(root, bg="white", bd=2)
frame_button_yes.place(relx=0.2, rely=0.6, relwidth=0.3, relheight=0.1)

frame_button_no = tk.Frame(root, bg="white", bd=2)
frame_button_no.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.1)

label2 = tk.Label(frame, text="Ich begrüsse Sie zu meiner Abschlussarbeit!", bg="#00001a", fg="white",font=("Alegra", 30))
label2.place(relwidth=1, relheight=1)

label3 = tk.Label(frame1, text="Wollen sie mit dem Verschlüsseln beginnen?", bg="#00001a", fg="white",font=("Alegra", 30))
label3.place(relwidth=1, relheight=1)

button = tk.Button(frame_button_yes, text="Ja", bg="#00001a", fg="white", font=("Alegra", 30), bd=2, command=open)
button.place(relwidth=1, relheight=1)

button_no = tk.Button(frame_button_no, text="Nein", bg="#00001a", fg="white", font=("Alegra", 30), bd=1, command=close)
button_no.place(relwidth=1, relheight=1)

root.mainloop()
