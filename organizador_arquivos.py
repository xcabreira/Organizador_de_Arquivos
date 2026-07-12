import os

caminho = r"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia"
listar_arquivos = os.listdir(caminho)

def organizar_pdf():
    for arquivo in listar_arquivos:
      if ".pdf" in arquivo:
          os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/PDFs/{arquivo}")
          print("Arquivos transferidos!")

def organizar_word():
    for arquivo in listar_arquivos:
      if ".doc" in arquivo:
          os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Word/{arquivo}")
          print("Arquivos transferidos!")
      elif ".docx" in arquivo:
          os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Word/{arquivo}")
          print("Arquivos transferidos!")
      elif ".odt" in arquivo:
          os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Word/{arquivo}")
          print("Arquivos transferidos!")
      elif ".dotx" in arquivo:
          os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Word/{arquivo}")
          print("Arquivos transferidos!")


def organizar_fotos():
    for arquivo in listar_arquivos:
      if ".png" in arquivo:
        os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Fotos/{arquivo}")
        print("Arquivos transferidos!")
      elif ".jpeg" in arquivo:
         os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Fotos/{arquivo}")
         print("Arquivos transferidos!")
      elif ".jpg" in arquivo:
         os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Fotos/{arquivo}")
         print("Arquivos transferidos!")
      elif ".webp" in arquivo:
         os.rename(f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/{arquivo}", f"C:/Users/JOABD/OneDrive/Área de Trabalho/Organizador_de_Arquivos/Claudia/Fotos/{arquivo}")
         print("Arquivos transferidos!")


organizar_fotos()
organizar_pdf()
organizar_word()