import os
import barcode
from barcode.writer import ImageWriter
import pandas as pd
from funcs import validation


def get_sheet_name(path):
    sheet = input("Digite o nome da planilha a ser utilizada( 'Planilha1' por padrão): ")
    try:
        pd.read_excel(path, sheet_name=sheet)
    except Exception as erro:
        print("Ooops, algo deu errado\n"
              f"{erro}")
    return sheet


# - Programa para ler 1 coluna do excel e transformar em codigo de barras o conteúdo dela.
file_name = validation.get_file_name()

plan = input("Nome da planilha: ").strip()
if len(plan) == 0:
    plan = "Sucatas"
if not file_name:
    file_name = "sample.xlsx"

df = pd.read_excel(f"{file_name}", sheet_name=plan)  # Open excel and read the data
dici = df.to_dict()
lis = list()
for i in dici["Serial"].values():
    lis.append(i)
# for key, values in dici["Ano"].items():
#     if str(values).startswith("0"):
#         alt = f"20" + str(values)[0:]
#         dici["Ano"][key] = alt
#     else:
#         alt = [str(values)].insert(0, "19")
#         dici["Ano"][key] = str(alt)
    # else:
    #     dici["Ano"][key] = f'{dici["Ano"][key]}'[0:4]

ean = barcode.get_barcode_class("code128")
for ind, i in enumerate(lis):
    mycode = ean(str(i), writer=ImageWriter)
    mycode.save(filename=f"codigo{ind}", text=f' {dici["Tipo"][ind]}\n{(dici["Ano"][ind])}\n{i}\nNULL')

head = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Codigo de barras</title>
    <link rel="stylesheet" href="style.css">
</head>
<body><h1>{plan}</h1>"""
mid = ''
body = """
<br>
<footer><center>Joao Pedro Oliveira &copy;</center></footer>
</body>
</html>"""

with open(f"Conversor_Barcode_{plan}.html", "w") as arq:
    arq.write(head)
    for ind, i in enumerate(lis):
        mid = f'<img src="codigo{ind}.svg">'
        arq.write(mid)
    arq.write(body)
print("\033[32mSucesso!")
print(dici["Ano"])
