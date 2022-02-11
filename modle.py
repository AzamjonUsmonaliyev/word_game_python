import random
from exchange import words_en , words_uz


def play():
    """ So'z topish o'yini boshlash uchun f-ya ! """
    list1 = []
    letters = []
    cheak = []
    num_count =0

    language = int(input("Englizcha o'ynaysizmi (1) , Yoki o'zbekcha (0) :"))

    if language:
        word = random.choice(words_en)
    else:
        word = random.choice(words_uz)


    for i in word[:]:
        letters.append(i.upper())
        list1.append("_")


    while letters != list1:
        num_count += 1 
        number=0
        print(list1)

        if cheak:
            for i in cheak:
                print(i.upper(),end=',')

            print("  siz bu harflarni kiritdingiz")

        intend = input("harif kiriting : ")

        if intend in cheak:
            print("Siz buni avval kiritgansiz ")
            continue
        cheak.append(intend)

        for i in letters:
            if i == intend.upper():
                list1[number] = (i.upper())
            number += 1

    print(list1)
    print(f" Tabriklaymiz siz {num_count} ta urinishda topdingiz !")