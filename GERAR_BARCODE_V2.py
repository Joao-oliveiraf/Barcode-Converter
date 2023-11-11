import os.path

import barcode
from barcode.writer import ImageWriter
import pandas as pd
from funcs import validation


# - Program to convert, from excel column(s), data into barcode(s) and save .svg files into an HTML document
# - Workbook(excel) parameters
text = input("Digite o camiho para o arquivo\n"
             "Ex: C:\\Users\\João Pedro\\Desktop\\nome_do_arquivo.xlsx : ")
titulo = input("Unidade responsável: ")
obj = input("Objeto dos codigos de barra: ")
file_name = validation.get_file_name(text)
file_path = validation.get_full_path(text)
plan = input("Digite o nome da planilha: ").strip()
coluna = input("Nome da 1 coluna a ser convertida em Barcode: ")
coluna2 = input("Nome da 2 coluna [Aperte a tecla Enter se não for utilizar]: ")
if len(coluna2) == 0:
    coluna2 = False

# Default values, change if needed AND fix indent ---------->
#  if len(plan) == 0:
#     plan = "carros"
#  if not file_name:
#  file_name = "pelotas.xlsx"

# Getting the amount of description for each barcode, default is 4
qnt_desc = int(input("Quantidade de descrições: "))
if not qnt_desc:
    qnt_desc = 4
# Get the data
df = pd.read_excel(f"{file_path}", sheet_name=plan)
dici = df.to_dict()
# Save the data to be converted into barcode in separated lists
desc_list = []
for k in dici.keys():
    desc_list.append(k)
lis = list()
lis2 = list()
for i in dici[coluna].values():
    lis.append(i)
if coluna2:
    for j in dici[coluna2].values():
        lis2.append(j)
# Generate the barcodes based on the number of descriptions
ean = barcode.get_barcode_class("code128")
if qnt_desc == 1:
    for ind, i in enumerate(lis):
        mycode = ean(str(i), writer=ImageWriter)
        mycode.save(filename=f"codigo_{file_name}{ind}", text=f'{i}')
elif qnt_desc == 2:
    for ind, i in enumerate(lis):
        mycode = ean(str(i), writer=ImageWriter)
        mycode.save(filename=f"codigo_{file_name}{ind}", text=f'{i}'
                                                              f'\n{dici[desc_list[0]][ind]}'
                                                              f'\n NULL')
elif qnt_desc == 4:
    for ind, i in enumerate(lis):
        mycode = ean(str(i), writer=ImageWriter)
        mycode.save(filename=f"codigo_{file_name}{ind}", text=f' {dici[desc_list[0]][ind]}'
                                                              f'\n{(dici[desc_list[1]][ind])}'
                                                              f'\n{dici[desc_list[2]][ind]}'
                                                              f'\n{dici[desc_list[3]][ind]}'
                                                              f'\n\nNULL')
elif qnt_desc == 5:
    for ind, i in enumerate(lis):
        mycode = ean(str(i), writer=ImageWriter)
        mycode.save(filename=f"codigo_{file_name}{ind}", text=f'{dici[desc_list[0]][ind]}'
                                                              f'\n{dici[desc_list[1]][ind]}'
                                                              f'\n{dici[desc_list[2]][ind]}'
                                                              f'\n{dici[desc_list[3]][ind]}'
                                                              f'\n{dici[desc_list[4]][ind]}'
                                                              f'\n NULL'
                                                              f'\nNULL')
elif qnt_desc == 3:
    for ind, i in enumerate(lis):
        mycode = ean(str(i), writer=ImageWriter)
        mycode.save(filename=f"codigo_{file_name}{ind}", text=f' {dici[desc_list[0]][ind]}'
                                                              f'\n{(dici[desc_list[1]][ind])}'
                                                              f'\n{dici[desc_list[2]][ind]}'
                                                              f'\n\nNULL')
if len(lis2) != 0:
    for index, j in enumerate(lis2):
        mycode2 = ean(str(j), writer=ImageWriter)
        mycode2.save(filename=f"codigo_{file_name}{index}_chapa", text=f'\n{j}')
# Create HTML to receive the .svg files
if not os.path.exists("style.css"):
    validation.criar_estilo()
head = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Codigo de barras</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<h1>Arquivo:{file_name.title()}</h1>
<h2>{titulo} - {obj}</h2>"""
mid = ''
mid2 = ''
body = """
<br>
<footer><center>Joao Pedro Oliveira &copy;</center></footer>
</body>
</html>"""
# Create HTML with the .svg files
with open(f"Conversor_Barcode_{file_name}({plan}).html", "w") as arq:
    arq.write(head)
    for ind, i in enumerate(lis):
        if coluna2:
            mid = f'<img src="codigo_{file_name}{ind}.svg">\n' \
                  f'<img src="codigo_{file_name}{ind}_chapa.svg" class="chapa">\n'
            arq.write(mid)
        else:
            mid = f'<img src="codigo_{file_name}{ind}.svg">\n'
            arq.write(mid)
    arq.write(body)
print("\033[32mSucesso!")
