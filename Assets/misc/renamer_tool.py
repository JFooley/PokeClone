import os

def substituir_palavra_no_nome(palavra_antiga, palavra_nova):
    # Listar arquivos no diretório
    arquivos = os.listdir()
    
    # Iterar sobre os arquivos no diretório
    for nome_arquivo in arquivos:
        # Verificar se o nome do arquivo contém a palavra antiga
        if palavra_antiga in nome_arquivo:
            # Substituir a palavra antiga pela palavra nova no nome do arquivo
            novo_nome_arquivo = nome_arquivo.replace(palavra_antiga, palavra_nova)
            
            # Construir o caminho completo dos arquivos antigo e novo
            caminho_antigo = nome_arquivo
            caminho_novo = novo_nome_arquivo
            
            # Renomear o arquivo
            os.rename(caminho_antigo, caminho_novo)
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome_arquivo}")

# Palavra antiga que deseja substituir
palavra_antiga = input("Insira a palavra que deseja substituir: ")
# Palavra nova que deseja inserir
palavra_nova = input("Insira a nova palavra: ")

# Chamar a função para substituir a palavra no nome dos arquivos
substituir_palavra_no_nome(palavra_antiga, palavra_nova)

