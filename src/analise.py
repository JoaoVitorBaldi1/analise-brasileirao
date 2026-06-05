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

def main():
    caminho = "data/brasileirao.csv"
    dados = carregar_dados(caminho)

    if dados is not None:
        mostrar_informacoes(dados)
        ranking_vitorias(dados)

if __name__ == "__main__":
    main()
    