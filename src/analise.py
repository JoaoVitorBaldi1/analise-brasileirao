import pandas as pd

def carregar_dados(caminho):
    try:
        return pd.read_csv(caminho)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None
    
def mostrar_informacoes(dados, time):
    print("=" * 40)
    print(f"ESTATÍSTICAS: {time}")
    print("=" * 40)
    print(f"Total de jogos:  {quantidade_jogos_time_especifico(dados, time)}")
    print(f"Vitórias:        {vitorias_time_especifico(dados, time)}")
    print(f"Empates:         {empates_time_especifico(dados, time)}")
    print(f"Derrotas:        {derrotas_time_especifico(dados, time)}")
    print(
        f"Aproveitamento:  "
        f"{aproveitamento_time_especifico(dados, time):.2f}%"
    )
    print(f"Gols marcados:   {gols_marcados_time_especifico(dados, time)}")
    print(f"Gols sofridos:   {gols_sofridos_time_especifico(dados, time)}")
    print(f"Saldo de gols:   {saldo_de_gols_time_especifico(dados, time)}")
    print("=" * 40)

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
    aproveitamento = ((3*vitorias_time_especifico(dados,time)+empates_time_especifico(dados,time))/(3*quantidade_jogos_time_especifico(dados,time))) * 100 
    return aproveitamento

def gols_marcados_por_time(dados):
    gols_jogos_mandante = dados.groupby("mandante")["mandante_Placar"].sum()
    gols_jogos_visitante = dados.groupby("visitante")["visitante_Placar"].sum()
    gols_marcados = gols_jogos_mandante + gols_jogos_visitante
    return gols_marcados

def gols_sofridos_por_time(dados):
    gols_jogos_mandante = dados.groupby("mandante")["visitante_Placar"].sum()
    gols_jogos_visitante = dados.groupby("visitante")["mandante_Placar"].sum()
    gols_sofridos = gols_jogos_mandante + gols_jogos_visitante
    return gols_sofridos

def time_existe(dados, time):
    times = pd.concat(
        [dados["mandante"], dados["visitante"]]
    ).unique()

    return time in times

def gols_marcados_time_especifico(dados, time):
    gols_por_time = gols_marcados_por_time(dados)
    return gols_por_time[time]

def gols_sofridos_time_especifico(dados, time):
    gols_por_time = gols_sofridos_por_time(dados)
    return gols_por_time[time]

def saldo_de_gols_time_especifico(dados,time):
    return gols_marcados_time_especifico(dados,time) - gols_sofridos_time_especifico(dados,time)

def melhor_ataque_campeonato(dados):
    gols_marcados = gols_marcados_por_time(dados)
    return f"O melhor ataque do campeonato foi o do {gols_marcados.idxmax()} com {gols_marcados.max()} gols"

def melhor_defesa_campeonato(dados):
    gols_sofridos = gols_sofridos_por_time(dados)
    return f"A melhor defesa do campeonato foi a do {gols_sofridos.idxmin()} sofrendo apenas {gols_sofridos.min()} gols"

def ranking_ataques(dados):
    gols_marcados = gols_marcados_por_time(dados)
    return gols_marcados.sort_values(ascending=False).head(10)

def ranking_defesas(dados):
    gols_sofridos = gols_sofridos_por_time(dados)
    return gols_sofridos.sort_values().head(10)

def mostrar_menu():
    print("\n" + "=" * 45)
    print("        ANÁLISE DO BRASILEIRÃO")
    print("=" * 45)
    print("1 - Estatísticas de um time")
    print("2 - Melhor ataque do campeonato")
    print("3 - Melhor defesa do campeonato")
    print("4 - Ranking dos melhores ataques")
    print("5 - Ranking das melhores defesas")
    print("6 - Ranking de vitórias")
    print("0 - Sair")
    print("=" * 45)

def main():
    caminho = "data/brasileirao.csv"
    dados = carregar_dados(caminho)

    if dados is None:
        return
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            time_analisado = input("Sobre qual time gostarias de informações? ").strip()
            if time_existe(dados, time_analisado):
                mostrar_informacoes(dados, time_analisado)
            else:
                print("Time não encontrado no dataset.")

        elif opcao == "2":
            print("\n" + melhor_ataque_campeonato(dados))

        elif opcao == "3":
            print("\n" + melhor_defesa_campeonato(dados))

        elif opcao == "4":
            print("\nTop 10 melhores ataques:")
            print(ranking_ataques(dados))

        elif opcao == "5":
            print("\nTop 10 melhores defesas:")
            print(ranking_defesas(dados))

        elif opcao == "6":
            ranking_vitorias(dados)

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Digite um número do menu.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
    