import os
from PIL import Image

def redimensionar_imagens(novo_tamanho):
    for arquivo in os.listdir():
        if arquivo.lower().endswith('.png'):
            # Abre a imagem PNG
            imagem = Image.open(arquivo)
            
            # Redimensiona a imagem mantendo o conteúdo original centralizado
            largura_original, altura_original = imagem.size
            nova_largura, nova_altura = novo_tamanho
            
            esquerda = (nova_largura - largura_original) // 2
            topo = (nova_altura - altura_original) // 2
            direita = esquerda + largura_original
            baixo = topo + altura_original
            
            imagem_redimensionada = Image.new("RGBA", novo_tamanho, (255, 255, 255, 0))
            imagem_redimensionada.paste(imagem, (esquerda, topo, direita, baixo))
            
            # Salva a imagem redimensionada
            imagem_redimensionada.save(arquivo)

# Novo tamanho desejado (largura, altura)
largura = input("Largura: ")
altura = input("Altura: ")
novo_tamanho = (int(largura), int(altura))  # Por exemplo, 300x300 pixels

# Chamada da função para redimensionar as imagens
redimensionar_imagens(novo_tamanho)
