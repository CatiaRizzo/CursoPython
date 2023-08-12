import tkinter as tk

root = tk.Tk()

# Cria um widget de texto
text = tk.Text(root,bg="#ffff9e")
text.pack()

# Define a fonte em negrito
bold_font = ('Arial', 12, 'bold')
text.tag_configure('bold', font=bold_font)

# Insere texto em negrito no widget de texto
text.insert('1.0', 'Este texto é em negrito', 'bold')

root.mainloop()