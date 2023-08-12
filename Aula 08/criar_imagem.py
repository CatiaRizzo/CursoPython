import tkinter as tk
from PIL import Image, ImageTk #carregando  aimagem usando a biblioteca PIL (Python Image Library)

def main():
    janela = tk.Tk()
    janela.title("Exemplo de inserção de imagem")
    image = Image.open("A:\Prof. Cassio de Albuquerque\Curso_Python_Senai\Catia Rizzo\Aula 08\Imagens.py\Lui.jpg")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(janela, image=photo) # Criando rótulo para exibir a imangem
    label.pack()
    
    janela.mainloop()
if __name__ == "__main__":
    main()
