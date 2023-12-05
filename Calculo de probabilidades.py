import pandas as pd

#Lê o CSV com todos os resultados da mega sena
data = pd.read_csv("Resultados mega sena.csv").to_dict('records')

#Lista todos os anos que constam neste dataset
possibleYears = sorted(list(set([field["Data"].split("/")[-1] for field in data])))

def calcularProbabilidade(dataArray, year=False):

    #Soma os resultados de todas as bolas
    bola1 = [resultado['bola 1'] for resultado in dataArray]
    bola2 = [resultado['bola 2'] for resultado in dataArray]
    bola3 = [resultado['bola 3'] for resultado in dataArray]
    bola4 = [resultado['bola 4'] for resultado in dataArray]
    bola5 = [resultado['bola 5'] for resultado in dataArray]
    bola6 = [resultado['bola 6'] for resultado in dataArray]
    todasAsBolas = bola1 + bola2 + bola3 + bola4 + bola5 + bola6

    probabilityArray = []

    #Calcula a probabilidade de cada um dos 60 números
    for number in range(1, 61):
        probabilityArray.append({
            "number": number,
            "allProbability": round((todasAsBolas.count(number) / len(todasAsBolas) * 100), 4)
        })

    #Ordena os números de acordo com a probabilidade
    probabilityArray.sort(key=lambda x: x["allProbability"], reverse=True)

    #Imprime os resultados
    for number in probabilityArray:
        print(f"O número {number['number']} tem a probabilidade de {number['allProbability']}% {f'no ano de {year}' if year else 'no periodo total'}.")

for year in possibleYears:
    #Calcula as probabilidades ano a ano
    filteredData = [field for field in data if year in field["Data"]]
    calcularProbabilidade(filteredData, year)

#Calcula a probabilidade geral
calcularProbabilidade(data)