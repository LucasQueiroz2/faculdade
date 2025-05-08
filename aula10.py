from mysql import connector
import mysql
from tkinter import *
import tkinter.messagebox as MessageBox
conexao=mysql.connector.connect(host='LocalHost',use='root',password='',database='loja')
c=conexao.cursor()

#c.execute('create database loja')

#c.execute('use loja')

"""c.execute('''create table produto(
          codigo int primary key
          nome varchar(20) not null
          preco decimal(10,2)not null
          quantidade int not null)''')"""


tk=Tk()
tk.geometry('500x300')
tk.title('loja')
def inserir():
    codigo=e_codigo.get()
    nome=e_nome.get()
    preco=e_preco.get()
    quantidade=e_quantidade.get()
    
    if(codigo ==''or nome =='' or preco =='' or quantidade ==''):
        MessageBox.showerror('inserir','todos os campos sao obrigatorios')
    else:
        c.execute('insert into produto(codigo,nome,preco,quantidade)values(%s,%s,%s,%s)',(codigo,nome,preco,quantidade))
        conexao.commit()
        MessageBox.showinfo('insert','Produto cadastrado')
        
        e_codigo.delete(0,END)
        e_nome.delete(0,END)
        e_preco.delete(0,END)
        e_quantidade.delete(0,END)
        
def excluir():
    codigo=e_codigo.get()
    if(codigo ==''):
        MessageBox.showerror('excluir','todos os campos sao obrigatorios')
    else:
        c.execute('delete from produto where codigo=%s',(codigo,))
        conexao.commit()
        MessageBox.showinfo('excluir','produto excluido')
        e_codigo.delete(0,END)
def alterar():
    codigo=e_codigo.get()
    nome=e_nome.get()
    preco=e_preco.get()
    quantidade=e_quantidade.get()

    
    if(codigo ==''or nome =='' or preco =='' or quantidade ==''):
        MessageBox.showerror('inserir','todos os campos sao obrigatorios')
    else:
        c.execute('update produto set nome=%s,preco=%s,quantidade=%s where codigo=%s',(nome,preco,quantidade,codigo))
        conexao.commit()
        MessageBox.showinfo('insert','Produto alterado')
        
        e_codigo.delete(0,END)
        e_nome.delete(0,END)
        e_preco.delete(0,END)
        e_quantidade.delete(0,END)
def consultar():
    codigo=e_codigo.get()
    if(codigo ==''):
        MessageBox.showerror('inserir','todos os campos sao obrigatorios')
    else:
        c.execute('select * from produto where codigo=%s',(codigo,))
        r =c.fetchall()
        
        if r:
            for r1 in r:
                e_nome.delete(0,END)
                e_preco.delete(0,END)
                e_quantidade.delete(0,END)
            
            
                e_nome.insert(0,r1[1])
                e_preco.insert(0,r1[2])
                e_quantidade.insert(0,r1[3])
                MessageBox('consultar','consultado:'f'codigo:{r1[0]},nome:{r1[1]},preco:{r1[2]},quantidade:{r1[3]}')
        else:
            MessageBox('consultar','nao existe')
        
Label(tk,text='codigo').grid(row=0,column=0)
Label(tk,text='nome').grid(row=2,column=0)
Label(tk,text='preco').grid(row=4,column=0)
Label(tk,text='quantidade').grid(row=6,column=0)

e_codigo = Entry(tk).grid(row=1,column=0)
e_nome = Entry(tk).grid(row=3,column=0)
e_preco = Entry(tk).grid(row=5,column=0)
e_quantidade = Entry(tk).grid(row=7,column=0)

Button(tk,text='inserir',command=inserir).grid(row=8,column=0)
Button(tk,text='excluir',command=excluir).grid(row=8,column=1)
Button(tk,text='alterar',command=alterar).grid(row=8,column=2)
Button(tk,text='consultar',command=consultar).grid(row=8,column=3)


tk.mainloop()