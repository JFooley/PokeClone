import os
from PIL import Image

def mirror_images():
    # Obtém o diretório atual
    diretorio_raiz = os.getcwd()

    # Loop através de todos os arquivos no diretório raiz
    for arquivo in os.listdir(diretorio_raiz):
        # Verifica se o arquivo é um arquivo PNG
        if arquivo.lower().endswith('.png'):
            # Abre o arquivo de imagem PNG
            imagem = Image.open(arquivo)
            
            # Espelha a imagem horizontalmente
            imagem_espelhada = imagem.transpose(Image.FLIP_LEFT_RIGHT)
            
            # Substitui a imagem original pela imagem espelhada
            imagem_espelhada.save(arquivo)
            
            # Fecha o arquivo de imagem
            imagem.close()

# Chamada da função para espelhar imagens PNG no diretório raiz
mirror_images()
