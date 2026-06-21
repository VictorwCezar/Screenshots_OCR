# Screenshots_OCR
OCR de Screenshots via CLI.

Script Python que lê automaticamente o screenshot mais recente da pasta
Pictures/Screenshots do usuário, extrai o texto via OCR (Tesseract/pyocr)
e copia o resultado para a área de transferência.

## Dependências
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) instalado no sistema com suporte ao idioma português (`por`)
- `pyocr`, `Pillow`, `pyperclip`

## Como usar
1. Instale as dependências: `pip install pyocr Pillow pyperclip` ou `pip install -r requirements.txt`
2. Execute o script: `python ocr.py`
3. O texto do screenshot mais recente será copiado automaticamente para o clipboard e é salvo no arquivo txt.
