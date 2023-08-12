def ler_arquivo():
    nome_arquivo = "exemplo.txt"

    with open(nome_arquivo,'r') as arquivo: # Abre o arquivo no modo leitura ('r')
        conteudo = arquivo.read() # Le o conteúdo do arquivo
        print (conteudo)    
    
if __name__ == '__main__':
    ler_arquivo()