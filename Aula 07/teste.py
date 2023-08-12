from tkinter import Tk, Text, Button

def change_text_color():
    text_widget.config(fg='red')  # configura a cor do texto para vermelho

root = Tk()

text_widget = Text(root)
text_widget.pack()

button = Button(root, text="Mudar cor do texto", command=change_text_color)
button.pack()

root.mainloop()