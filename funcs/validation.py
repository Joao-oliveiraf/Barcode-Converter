import os
import pandas as pd


def index_dici(dici, kwargs):
    if type(dici) != dict:
        return False
    else:
        rt_array = []
        keys = [k for k in dici.keys()]
        values = [v for v in dici.values()]
        if kwargs in values:
            for count, i in enumerate(values):
                if i == kwargs:
                    rt_array.append(count)
            return rt_array
        else:
            return False


def get_file_name(text):
    arq = []
    if not os.path.isfile(text):
        return False
    else:
        for ind, char in enumerate(text[::-1]):
            arq.append(char)
            if not char.isalpha():
                if char in ".,_-" or char == " ":
                    continue
                elif char == "\\":
                    arq.pop()
                    break

        return "".join(reversed(arq))


def get_sheet_name(path):
    sheet = input("Digite o nome da planilha a ser utilizada( 'Planilha1' por padrão): ")
    try:
        pd.read_excel(path, sheet_name=sheet)
    except Exception as erro:
        print("Ooops, algo deu errado\n"
              f"{erro}")
        exit(1)
    return sheet


def get_full_path(string):
    if os.path.isfile(string):
        return string
    else:
        return False


def criar_estilo():
    with open("style.css", "w") as css:
        css.write("""
            img{
        margin-right: 5px;
        padding: 1.5%;
        width: 140px;
        height: 150px;

    }
    .chapa{
        padding-top: 5%;
        align-items: center;
        height: 150px;
        width: 120px;    
    }
    h1{
        color: rgb(0, 0, 0);
        font-size: xx-large;
    }""")
