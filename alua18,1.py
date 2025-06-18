import tkinter as tk
from PIL import ImageTk, Image


def cadsatrar():
    print('Cadastro de usuários')
    print(f'nome', {nome.get()})
    print(f'nome', {email.get()})
    print(f'nome', {celular.get()})


janela = tk.Tk()
janela.title('Cadastro de usuários')
janela.geometry('450x500')
janela.resizable(False,False)

frame_principal=Frame(janela,padx=20,pady=20)
frame_principal.pack(fill=BOTH,expand=True)
try:
    img= Image.open('C:/Users/Aluno/Downloads/Nova pasta/img.png')
    img=img.resize((150,150),Image.LANCZOS)
    tk_img=ImageTk.PhotoImage(img)
    label_imagem=label(frame_principal, Image=tk_img)
    label_imagem.imagem=tk_img
    label_imagem.pack(pady=10)
except:
    label_sem_imagem=label(frame_principal, text='LOGO',font=('arial',24))
    label_sem_imagem.pack(pady=20)
    frame_form=frame(frame_principal)
    frame_form.pack(fill= BOHT, expand=True,pady=20)
    Label(frame_form,font ('arial,12'))
    