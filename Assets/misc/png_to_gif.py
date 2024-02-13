import os
from PIL import Image

def merge_frames():
    # Obtém o diretório atual
    diretorio_raiz = os.getcwd()
    
    # Lista para armazenar as imagens em ordem de número no nome
    imagens_ordenadas = []
    
    # Loop através de todos os arquivos no diretório raiz
    for arquivo in os.listdir(diretorio_raiz):
        # Verifica se o arquivo é um arquivo PNG
        if arquivo.lower().endswith('.png'):
            # Extrai o número do final do nome do arquivo
            numero = int(arquivo.split('-')[-1].split('.')[0])
            
            # Adiciona a tupla (nome do arquivo, número) à lista
            imagens_ordenadas.append((arquivo, numero))
    
    # Ordena a lista de imagens com base no número
    imagens_ordenadas.sort(key=lambda x: x[1])
    
    # Lista para armazenar os objetos Image
    imagens = []
    
    # Loop através das imagens ordenadas
    for arquivo, _ in imagens_ordenadas:
        # Abre cada imagem PNG
        imagem = Image.open(arquivo)
        imagens.append(imagem)
    
    # Salva todas as imagens como um arquivo GIF
    imagens[0].save('result.gif', save_all=True, append_images=imagens[1:], loop=0, duration=100)

# Chamada da função para criar o GIF com base nos números no nome dos arquivos PNG
merge_frames()
