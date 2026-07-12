import os

caminho = r"" # Local da pasta ou dir
arquivos = os.listdir(caminho) # Lista os arquivos

for arquivo in arquivos:
    nome_arquivo = f"{caminho}/{arquivo}"
    tamanho = os.path.getsize(nome_arquivo) / 1000000 # Transforma em MB
    if tamanho > 1000: # Se for maior que 1GB, exclui o arquivo
        os.remove(nome_arquivo)