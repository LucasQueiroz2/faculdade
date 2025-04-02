
from tkinter import*
i=Tk()
'''questao 1
def verificar_numero():
    numero=float(entry_numero.get())
    if numero>0:
     resultado='positivo'    
    elif numero<0:
       resultado='negativo'
    else:
       resultado='nao existe'
    resultado_label.config(text=f"Numero:{resultado}")

label_numero=Label(i,text='Numero')
label_numero.grid(row=0, column=0, padx=10, pady=10) 
entry_numero=Entry(i, font=("Arial", 12))
entry_numero.grid(row=0, column=1, padx=10, pady=10)
resultado_label=Label(i)
resultado_label.grid(row=2, column=0, columnspan=2, pady=20)

btn=Button(i,text='?',command=verificar_numero)
btn.grid(row=3, column=0, columnspan=2, pady=20)
'''
'''
def lista_comp():
         lista_numeros = [float(num.strip()) for num in entry_lista.get().split(',') if num.strip()]
         limite = float(entry_limite.get())
         for i, num in enumerate(lista_numeros):
            if num > limite:
                indice = num
                
         indice_label.config(text=f'{indice}')
                
                
         
label_lista=Label(i,text='digite numeros para uma lista')
label_lista.grid(row=0,column=0)
entry_lista=Entry(i)
entry_lista.grid(row=1,column=0)

label_limite=Label(i,text='limite')
label_limite.grid(row=2,column=0)
entry_limite=Entry(i)
entry_limite.grid(row=3,column=0)

indice_label=Label(i)
indice_label.grid(row=4,column=0)

btn=Button(i, text="Verificar", command=lista_comp)
btn.grid(row=7,column=0)
'''
'''
label_ano=Label(i,text='ano')
label_ano.grid(row=0,column=0)
entry_ano=Entry(i)
entry_ano.grid(row=1,column=0)

def verificar_bissexto():
    ano=float(entry_ano.get())
    if ano%4==0 and ano%100!=0 or ano%400==0:
       resultado='ano bissexto'
    else:
        resultado='nao é bissexto'
    resultado_label.config(text=f'{resultado}')

btn=Button(i,command=verificar_bissexto)
btn.grid(row=2 ,column=0)
resultado_label=Label(i)
resultado_label.grid(row=3,column=0)'
'''
'''
label_num=Label(i,text='num1')
label_num.grid(row=0,column=0)
entry_num=Entry(i)
entry_num.grid(row=1,column=0)

label_num1=Label(i,text='num2')
label_num1.grid(row=2,column=0)
entry_num1=Entry(i)
entry_num1.grid(row=3,column=0)
def calcular():
    num1=float(entry_num.get())
    num2=float(entry_num1.get())
    soma=num1+num2
    sub=num1-num2
    mult=num1*num2
    divi=num1/num2
    resultado_label1.config(text=f'soma={soma}')
    resultado_label2.config(text=f'sub={sub}')
    resultado_label3.config(text=f'mult={mult}')
    resultado_label4.config(text=f'divi={divi}')

btn=Button(i,command=calcular)
btn.grid(row=4,column=0)

resultado_label1=Label(i)
resultado_label1.grid(row=5,column=0)

resultado_label2=Label(i)
resultado_label2.grid(row=6,column=0)

resultado_label3=Label(i)
resultado_label3.grid(row=7,column=0)

resultado_label4=Label(i)
resultado_label4.grid(row=8,column=0)'''

label_num1=Label(i,text='num1')
label_num1.grid(row=0,column=0)
entry_num1=Entry(i)
entry_num1.grid(row=1,column=0)

label_num2=Label(i,text='num1')
label_num2.grid(row=0,column=0)
entry_num2=Entry(i)
entry_num2.grid(row=1,column=0)

label_num3=Label(i,text='num1')
label_num3.grid(row=0,column=0)
entry_num3=Entry(i)
entry_num3.grid(row=1,column=0)

label_num4=Label(i,text='num1')
label_num4.grid(row=0,column=0)
entry_num4=Entry(i)
entry_num4.grid(row=1,column=0)


i.mainloop()
'''
5. Criar uma interface Tkinter que permita ler quatro valores pelo teclado e
guarde-os em uma lista.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares. enunciado para tkinter'''