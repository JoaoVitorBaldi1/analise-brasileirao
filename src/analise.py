import pandas as pd

def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None
    
def mostrar_informacoes(dados):
    print("Primeiras linhas:")
    print(dados.head())

    print("\nColunas:")
    print(dados.columns)

    print("\nInformações gerais:")
    print(dados.info())

def ranking_vitorias(dados):
    ranking_vitorias = dados[dados["vencedor"] != "-"]["vencedor"].value_counts()
    print("\nTop 10 times com mais vitórias:")
    print(ranking_vitorias.head(10))

def vitorias_time_especifico(dados,time):
    num_vitorias = len(dados[dados["vencedor"] == time])
    print(f"O(a) {time} venceu: {num_vitorias} partidas")

def derrotas_time_especifico(dados,time):
    num_derrotas = len(dados[((dados["visitante"]==time)& (dados["vencedor"] == dados["mandante"])) | ((dados["mandante"]==time)& (dados["vencedor"] == dados["visitante"]))])
    print(f"O número de derrotas do {time} é: {num_derrotas}")

def empates_time_especifico(dados,time):
    num_empates = len(dados[(dados["vencedor"]=="-") & ((dados["visitante"]==time) | (dados["mandante"]== time))])
    print(f"A quantidade de empates do {time} é {num_empates}")

def quantidade_empates(dados):
    num_empaes_geral = len(dados[dados["vencedor"]== "-"])
    print(f"A quantidade de empates geral é: {num_empaes_geral}")



def main():
    caminho = "data/brasileirao.csv"
    dados = carregar_dados(caminho)

    if dados is not None:
        ranking_vitorias(dados)
        vitorias_time_especifico(dados, "Internacional")
        quantidade_empates(dados)
        empates_time_especifico(dados,"Internacional")
        derrotas_time_especifico(dados,"Internacional")

if __name__ == "__main__":
    main()
    