import pandas as pd

def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None
    
def mostrar_informacoes(dados,time):
    print(f"Printando informações sobre: {time}")
    print(f"Toal de jogos: {quantidade_jogos_time_especifico(dados,time)}")
    print(f"Vitórias: {vitorias_time_especifico(dados,time)}")
    print(f"Empates: {empates_time_especifico(dados,time)}")
    print(f"Derrotas: {derrotas_time_especifico(dados,time)}")
    print(f"Aproveitamento: {aproveitamento_time_especifico(dados,time)}%")

def ranking_vitorias(dados):
    ranking_vitorias = dados[dados["vencedor"] != "-"]["vencedor"].value_counts()
    print("\nTop 10 times com mais vitórias:")
    print(ranking_vitorias.head(10))

def vitorias_time_especifico(dados,time):
    num_vitorias = len(dados[dados["vencedor"] == time])
    return num_vitorias

def derrotas_time_especifico(dados,time):
    num_derrotas = len(dados[((dados["visitante"]==time)& (dados["vencedor"] == dados["mandante"])) | ((dados["mandante"]==time)& (dados["vencedor"] == dados["visitante"]))])
    return num_derrotas

def empates_time_especifico(dados,time):
    num_empates = len(dados[(dados["vencedor"]=="-") & ((dados["visitante"]==time) | (dados["mandante"]== time))])
    return num_empates

def quantidade_empates(dados):
    num_empates_geral = len(dados[dados["vencedor"]== "-"])
    return num_empates_geral

def quantidade_jogos_time_especifico(dados,time):
    qntd_jogos = len(dados[(dados["visitante"]==time)|(dados["mandante"]==time)])
    return qntd_jogos

def aproveitamento_time_especifico(dados,time):
    aproveiamento = ((3*vitorias_time_especifico(dados,time)+empates_time_especifico(dados,time))/(3*quantidade_jogos_time_especifico(dados,time))) * 100 
    return aproveiamento


def main():
    caminho = "data/brasileirao.csv"
    dados = carregar_dados(caminho)

    if dados is not None:
        time_analizado = input("Sobre qual time gostarias de informações?")
        mostrar_informacoes(dados,time_analizado)

if __name__ == "__main__":
    main()
    