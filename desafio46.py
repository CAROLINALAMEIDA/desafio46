import random

def jogo():
    """
    Função que implementa o jogo Pedra, Papel e Tesoura.
    """
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias_usuario = 0
    derrotas_usuario = 0
    empates = 0

    while True:
        computador = random.choice(opcoes)

        usuario = input("Escolha uma opção (pedra, papel ou tesoura) ou 'sair' para sair do jogo: ").lower()

        if usuario == 'sair':
            break

        while usuario not in opcoes:
            print("Opção inválida. Por favor, escolha novamente.")
            usuario = input("Escolha uma opção (pedra, papel ou tesoura) ou 'sair' para sair do jogo: ").lower()

        print(f"\nVocê escolheu: {usuario}")
        print(f"Computador escolheu: {computador}\n")

        if usuario == computador:
            print("Empate!")
            empates += 1
        elif (usuario == "pedra" and computador == "tesoura") or \
             (usuario == "tesoura" and computador == "papel") or \
             (usuario == "papel" and computador == "pedra"):
            print("Você venceu!")
            vitorias_usuario += 1
        else:
            print("Computador venceu!")
            derrotas_usuario += 1

        print("\nEstatísticas do jogo:")
        print(f"Vitórias: {vitorias_usuario}")
        print(f"Derrotas: {derrotas_usuario}")
        print(f"Empates: {empates}")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

    print("Obrigado por jogar!")

jogo()