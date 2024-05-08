from tkinter import *
from tkinter import Tk, ttk
import dates
from tkinter import messagebox

screen = Tk()
screen.title(dates.TITULO)
screen.geometry(dates.JANELA)
screen.configure(background=dates.PRETO)
screen.resizable(width=FALSE, height=FALSE)

#FRAMES
frame_up = Frame(screen, width=310, height=0, bg=dates.BRANCO, relief='flat')
frame_up.grid(row=0, column=0,pady=1, padx=0, sticky=NSEW)

frame_down = Frame(screen,width=310, height=300,bg=dates.BRANCO, relief="flat")
frame_down.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

#CONFIG FRAME UP
l_nome = Label(frame_down, text="LOGIN", height=1,anchor=NE, font=('Ivy 25 '), bg=dates.BRANCO, fg=dates.LETRA)
l_nome.place(x=105, y=5)

l_linha = Label(frame_up,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=dates.VERDE)
l_linha.place(x=10, y=45)
#FRAM DOWM
# configurando frame_baixo ---------------------------

l_nome = Label(frame_down, text="Nome *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=dates.BRANCO, fg=dates.LETRA)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_down, width=25, justify='left',font=("", 15), highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_down, text="Senha *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=dates.BRANCO, fg=dates.LETRA)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_down,show='*',width=25, justify='left',font=("",15),highlightthickness=1,relief="solid")
e_pass.place(x=15, y=130)
credenciais = [' admin', 'admin']
def nova_janela():
    l_nome = Label(frame_up, text="Usuario: " + credenciais[0], height=1,anchor=NE, font=('Ivy 20 '), bg=dates.BRANCO, fg=dates.LETRA)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_up,width=275, text="", height=1,anchor=NW, font=('Ivy 1 '), bg=dates.VERDE)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_down, text="Seja bem vindo " + credenciais[0], height=1,anchor=NE, font=('Ivy 15 '), bg=dates.BRANCO, fg=dates.LETRA)
    l_nome.place(x=5, y=105)
def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())

    if nome=='admin' and senha=='admin':
        messagebox.showinfo('Login',' Seja bem vindo Admin !!!')

    # verificando os dados para permitir o login do usuario
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login',' Seja bem vindo de volta '+credenciais[0])

        # apagar o que tiver no frame baixo e cima
        for widget in frame_down.winfo_children():
            widget.destroy()

        for widget in frame_up.winfo_children():
            widget.destroy()

        # chamr nova janela
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuario ou a senha digitada')

botao_confirmar = Button(frame_down, command=verificar_senha, text="Entrar", width=39, height=2, bg=dates.VERDE, fg=dates.BRANCO, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- estetic

# engines


screen.mainloop()