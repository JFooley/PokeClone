from PIL import Image

def extract_frames(nome_gif, nome_base_output):
    # Abre o GIF
    gif = Image.open(nome_gif + ".gif")

    # Loop através de cada frame do GIF
    for i in range(gif.n_frames):
        # Seleciona o frame
        gif.seek(i)
        
        # Cria um nome único para o arquivo PNG
        nome_output = f"{nome_base_output}-{i}.png"
        
        # Salva o frame atual como um arquivo PNG
        gif.save(nome_output)

    # Fecha o arquivo GIF
    gif.close()

# Exemplo de uso:
nome_gif = input("Digite o nome do arquivo GIF: ")  # Nome do arquivo GIF
nome_base_output = input("Digite o nome dos arquivos de saida: ")# Nome base para os arquivos PNG de saída
extract_frames(nome_gif, nome_base_output)
