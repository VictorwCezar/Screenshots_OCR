from os import path, listdir, getlogin
import pathlib
import sys

import pyocr
import pyocr.builders as builders

import pyperclip as clip
from PIL import Image

login = getlogin() # Login do usuario.

imagem = path.join(f"C:\\Users\\{login}\\Pictures\\Screenshots") # Caminho em que a Screenshot é salva.

retorno = "ocr.txt"

tools = pyocr.get_available_tools() # Motor usado no projeto tesseract v5.5.0.20241111
tool = tools[0]

lang = "por" # Linguagem usada para realizar a leitura.

def main(caminho):

    # Selecionando a imagem mais recente.

    arquivo = sorted(
        listdir(caminho),
        key= lambda f: path.getmtime(path.join(caminho, f)),
        reverse=True
        )    

    # Pilow realiza a abertura da imagem e o motor realiza a leitura do conteudo.

    img = Image.open(path.join(caminho, arquivo[0]))

    txt = tool.image_to_string(
        img,
        lang=lang,
        builder=builders.TextBuilder()
    )

    clip.copy(txt) # Adiciona o conteudo à Clipboard.

    return txt



with open(retorno, "w", encoding="utf-8") as resultado:
    resultado.write(main(imagem))




