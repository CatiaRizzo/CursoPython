def criar_arquivo():
    nome_arquivo = "exemplo.docx"

    with open(nome_arquivo,'w') as arquivo: # Abre o arquivo no modo escrita ('w')
        arquivo.write("Este é um exemplo de arquivo criado com Python.\n")
        arquivo.write("Você pode escrever várias linhas neste arquivo.\n")
    
if __name__ == '__main__':
    criar_arquivo()