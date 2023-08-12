def ler_arquivo_linha_por_linha():
    nome_arquivo = "exemplo.txt"

    with open(nome_arquivo,'r') as arquivo: # Abre o arquivo no modo leitura ('r')
        for line in arquivo:
            print(line.strip()) # Remove os espaços em branco do inicio e fim da linha   
    
if __name__ == '__main__':
    ler_arquivo_linha_por_linha()