from modle import play
print("So'z toqish o'yiniga xush kelibsiz !")
while True:
    ask = int(input("o'ynashni xohlaysimi: yes(1)/no(0)"))
    if ask:
        play()
    else:
        break

