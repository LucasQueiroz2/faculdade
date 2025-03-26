from tkinter import*

i = Tk()
i.title('Primeira Janela')
i.geometry('600x300')
#i.resizable(False,False)
#i.state('zoomed')
#i.state('iconic')
i.maxsize(900,500)
i.minsize(300,150)
i['bg'] = 'black'
#i.wm_iconbitmap('nome da imagem')
#Entry() - cria entrada de dados
e  = Entry(i)
e.pack()

#Button() inserir botao na janela
#btn=Button(i,text='Inserir',font='Arial 12 bold').pack()

#Label() - rotulo

def botao_clicado():
    label.config(text="calvo de cria")

btn1 =Button(i,
            text = 'com cabelo',
            font= 'Arial 10 italic',
            fg='white',
            bg='blue',
            relief='raised',
            bd= 5,
            padx=20,
            pady=10,
            activebackground='green',
            activeforeground='yellow',
            command=botao_clicado)
btn1.pack(pady=20)

label=Label(i,
            bg='red',fg='white',font='Arial 12 bold')
label.pack()
i.mainloop()