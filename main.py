from tkinter import *

cor1 = "#F683C2"
principal = Tk()
principal.title("Cadastro")
principal.configure(background=cor1)
principal.geometry("300x300+200+200")
principal.iconbitmap("icon.ico")

label1 = Label(principal, text="Nome de usuário: ", background = cor1)
label1.place(x=30,y=30)

entrada1 = Entry(principal)
entrada1.place(x=150,y=30)

botao1 = Button(principal, text="Salvar")
botao1.place(x=50,y=70)

botao1 = Button(principal, text="Limpar")
botao1.place(x=100,y=70)

principal.mainloop()
