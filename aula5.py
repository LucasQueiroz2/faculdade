from tkinter import*

i = Tk()
i.title('Primeira Janela')
i.geometry('600x300')
#i.resizable(False,False)
#i.state('zoomed')
#i.state('iconic')
#i.maxsize(900,500)
#i.minsize(300,150)
#i['bg'] = 'black'
#i.wm_iconbitmap('nome da imagem')
#Entry() - cria entrada de dados
'''
e  = Entry(i)
e.pack()
'''
#Button() inserir botao na janela
#btn=Button(i,text='Inserir',font='Arial 12 bold').pack()

#Label() - rotulo
'''
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
'''
#Sistema  grid(linha e coluna)-------------------------
'''x1=Label(i,text='Teste1',bg='red')
x2=Label(i,text='Teste2',bg='blue')
x3=Label(i,text='Teste3',bg='green')
x1.grid(row=0,column=0)
x2.grid(row=0,column=1)
x3.grid(row=0,column=2)'''
#--------------------------------------------------
'''
label_nome = Label(i,text='Nome:')
label_nome.grid(row=0,column=0,padx=10,pady=10)

entry_nome=Entry(i)
entry_nome.grid(row=0,column=1,padx=10,pady=10)

label_idade = Label(i,text='Idade:')
label_idade.grid(row=1,column=0,padx=10,pady=10)

entry_idade=Entry(i)
entry_idade.grid(row=1,column=1,padx=10,pady=10)


def informacoes():
    nome= entry_nome.get()
    idade = entry_idade.get()
    r_Label.config(text=f'nome{nome} \n idade:{idade}')
btn2=Button(i,text='cadastrar',command=informacoes)
btn2.grid(row=2,column=0,pady=20,columnspan=2)

r_Label = Label(i,bg='blue')
r_Label.grid(row=3,column=0,columnspan=2)'''

#Checkbutton()-seleção multipla
'''
def seleciona():
    selecionados=[]
    if fut_var.get():
        selecionados.append('futebol')
    if vol.get():
        selecionados.append('volei')
    if bas.get():
        selecionados.append('basquete')
    if nat.get():
        selecionados.append('natação')
    if surf.get():
        selecionados.append('surf')
    r_label.config(text='esporte selecionado:'+'☻'.join(selecionados))
fut_var=IntVar()
vol=IntVar()
bas=IntVar()
nat=IntVar()
surf=IntVar()

t=Label(i,text='qual o seu esporte favorito')
#t.grid(row=0,column=0,padx=10,pady=10)
a1=Checkbutton(i,text='futebol',variable=fut_var)
a2=Checkbutton(i,text='volei',variable=vol)
a3=Checkbutton(i,text='basquete',variable=bas)
a4=Checkbutton(i,text='natação',variable=nat)
a5=Checkbutton(i,text='surf',variable=surf)

a1.grid(row=1,column=0,padx=10,pady=10)
a2.grid(row=2,column=0,padx=10,pady=10)
a3.grid(row=3,column=0,padx=10,pady=10)
a4.grid(row=4,column=0,padx=10,pady=10)
a5.grid(row=5,column=0,padx=10,pady=10)
t.place(x=10,y=10)
a1.place(x=10,y=40)
a2.place(x=10,y=80)
a3.place(x=10,y=120)
a4.place(x=10,y=160)
a5.place(x=10,y=200)

bnt3=Button(i,text='envie',command=seleciona)
bnt3.place(x=10,y=240)

r_label=Label(i,text='Nenhum esporte selecionado')
r_label.place(x=0,y=280)
'''
#Radiobutton()-seleção simples----------------------
'''
valor=IntVar()

r1= Radiobutton(i,text='opção1',variable=valor,value=1)
r2= Radiobutton(i,text='opção2',variable=valor,value=1)
r3= Radiobutton(i,text='opção3',variable=valor,value=1)

r1.place(x=10,y=10)
r2.place(x=10,y=40)
r3.place(x=10,y=80)
'''
#Listbox()-cria uma lista

lista=Listbox(i,selectmode=MULTIPLE)
lista.insert(0,'AC')
lista.insert(1,'RJ')
lista.insert(2,'MG')
lista.insert(3,'AL')
lista.insert(4,'SP')
lista.insert(5,'AM')
lista.insert(END,'ES')
lista.pack()

estado=['a','b','c','d','e']

for O in estado:
    lista.insert(END,O)

i.mainloop()