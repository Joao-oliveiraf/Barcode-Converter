# Barcode-Converter
## PT-BR
# Conversor de código de barras para até duas informações de um arquivo .xlsx.

 O código de barras gerado em .svg podera conter de **1 até 5 descrições** (dados da linha).

No caso da conversão de duas informações em codigo de barras, a segunda ficará imediatamente depois da primeira (esquerda para a direita).

Ainda no tópico de duas conversões, somente **o primeiro código** gerado terá a quantidade de descrições total(1-5), sendo que o segundo terá apenas o valor **convertido** como descrição.

Output será em um arquivo .html. Para melhor comodidade, recomendo salvar com arquivo PDF.

Mude o arquivo style a sua escolha! Na ausência de um arquivo com o nome "style.css" o programa irá criar automaticamente.

## Exemplo do excel
Em destaque estão alguns parâmetros obrigatórios como: **Nome da coluna (Case sensitive), Nome da planilha(Case sensitive), Caminho COMPLETO do arquivo (C:\\User\\...)**

## Parâmetros do exemplo
### Nome da coluna 1 = SERIAL, Nome da coluna 2 = NUM, Nome da planilha = Sheet1

![Exemplo do arquivo excel](excel_example.png)

### Exemplo do arquivo final
![Exemplo do arquivo final](barcode_example.png)



