import random
def pilihan_computer():
    pilihan = ["batu","gunting","kertas"]
    return random.choice(pilihan)

def tentukan_pemenang(player, computer):
    if player == computer:
        return "seri"
    elif (player == "batu" and computer == "gunting"):
        return "menang"
    elif (player == "gunting"and computer == "kertas"):
        return "menang"
    elif (player == "kertas" and computer == "batu"):
        return "menang"
    else:
        return "kalah"


def main():
    skor_player = 0
    skor_computer = 0

    print("==============================")
    print("   BATU • GUNTING • KERTAS")
    print("==============================")

    for ronde in range(1, 4):

        print()
        print("====================")
        print("ROUND", ronde)
        print("====================")


        player = input("Pilih batu, gunting, atau kertas: ").lower()
        computer = pilihan_computer()
        hasil = tentukan_pemenang(player,computer)

        print()
        print("Kamu     :", player.upper())
        print("Computer :", computer.upper())

        if hasil == "menang":
            print("🔥 KAMU MENANG!")
            skor_player += 1
        elif hasil == "kalah":
            print("💀 COMPUTER MENANG!")
            skor_computer += 1
        else:
            print("🤝 SERI!")

        print()
        print("Score")
        print("Kamu     :", skor_player)
        print("Computer :", skor_computer)


    print()
    print("==============================")
    print("         FINAL SCORE")
    print("==============================")

    print("Kamu     :", skor_player)
    print("Computer :", skor_computer)

    if skor_player > skor_computer:
        print("🏆 YOU WIN!")
    elif skor_computer > skor_player:
        print("🤖 COMPUTER WINS!")
    else:
        print("🤝 DRAW!")
main()