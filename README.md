# Resolvendo CAPTCHA com rede neural convolucional

## 1 - Instalando as bibliotecas necessárias

* ~# sudo apt install python3-pip tesseract-ocr libtesseract-dev
* ~# pip3 install selenium Selenium-Screenshot pytesseract tesseract numpy imutils sklearn tensorflow keras opencv-python opencv-contrib-python

## 2 - Instalando webDriver firefox para utilizar no selenium

Acessar a URL https://github.com/mozilla/geckodriver/releases baixar a pasta geckodriver-v0.26.0-linux64.tar.gz, extrair e mover/copiar geckodriver para /usr/bin

## 3 - Montando o Dataset

Execute o script getCAptcha.py para montar o dataset com 1000 exemplos de CAPTCHA.

  ~# python3 getCAptcha.py

  Script Criado por Igor Balbino
  
## 4 - Melhorar o Dataset

  ~# python3 separarletras.py
  
Script Criado por Adrian e modificado por Igor Balbino

Utilize o script separarletras.py para criar um novo Dataset com apenas letras e números

## 5 - Treinar o modelo com rede neural convolucional 

Execute o script train_model.py para treinar o modelo com base no dataset criado.

  ~# python3 train_model.py
  
  Script Criado por Adam Geitgey e modificado por Igor Balbino

## 6 - Testar o modelo.

Para testar o modelo utilize o script testarModelo1000.py, esse script irá resolver todos os CAPTCHAs utilizando o modelo criado acima.

~# python3 testarModelo1000.py

Script Criado por Adrian e modificado por Igor Balbino

### Referência

ROSEBROCK, Dr. Adrian. DEEP LEARNING FOR COMPUTER VIS ION WITH PYTHON. In: ROSEBROCK, Dr. Adrian. DEEP LEARNING FOR COMPUTER VISION WITH PYTHON. Philadelphia: Pyimagesearch, 2017. Cap. 21. p. 287 - 306.
