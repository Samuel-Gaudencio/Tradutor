import requests
from tkinter import *
from playsound import playsound
from gtts import *
import os
from key import key


def margem(altura):
    tela = Canvas(root, width=500, height=altura, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
    tela.pack()


def tradutor():

    url = "https://text-translator2.p.rapidapi.com/translate"

    texto = text.get()
    payload = {
            "source_language": "pt",
            "target_language": "en",
            "text": texto
    }

    headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    text_traduzido.configure(text=(response.json()['data']['translatedText']))
    text_traduzido.pack()
    button_play.pack()


def texto_em_fala():
    margem(10)
    button_resete.pack()
    texto_inserido = text.get()
    fala = gTTS(texto_inserido, lang='en', slow=False, tld='com.br')
    fala.save('fala.mp3')
    playsound('fala.mp3')


def resetar():
    text.delete(0, 'end')
    os.remove('fala.mp3')


root = Tk()
root.title('Tradutor')
root.geometry('400x400')
root.configure(bg='#1d1d1d')

vol = PhotoImage(file='volume.png')

margem(35)
title = Label(root, text='Informe um texto para traduzir', bg='#1d1d1d', fg='#fff', font=('Montserrat', 16, 'bold'), pady=8)
title.pack()

text = Entry(root, width=35, bd=0, bg='#2d2d2d', font='Montserrat', fg='#fff', relief=FLAT, justify=CENTER, borderwidth=4)
text.pack()

margem(10)
button = Button(root, text='Traduzir', bg='#C69749', fg='#fff', font=('Montserrat', 12, 'bold'), relief=FLAT,
                activebackground='#C69749', activeforeground="#fff", padx=10, pady=2, command=tradutor)
button.pack()

text_traduzido = Label(root, text='', bg='#1d1d1d', fg='#fff', font=('Montserrat', 16, 'bold'), pady=8, wraplength=400)

margem(10)
button_play = Button(root, image=vol, bg='#C69749', activebackground='#C69749', command=texto_em_fala)

button_resete = Button(root, text='Resetar', bg='#C69749', fg="#FFF", font=('Montserrat', 12, 'bold'), relief=FLAT,
                       activebackground='#C69749', activeforeground="#fff", command=resetar)

# Olá meu nome e samuel, meu sonho e ser analista de dados
root.mainloop()
