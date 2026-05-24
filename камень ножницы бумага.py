import random
import os
import time

def show_logo():
    print("""разработчики:
██╗░░██╗███████╗████████╗░░░░░░░░░██╗░░██╗░█████╗░████████╗
██║░██╔╝██╔════╝╚══██╔══╝░░░░░░░░░██║░██╔╝██╔══██╗╚══██╔══╝
█████╔╝░█████╗░░░░░██║░░░░░░░░░░░░█████╔╝░███████║░░░██║░░░
██╔═██╗░██╔══╝░░░░░██║░░░░░░░░░░░░██╔═██╗░██╔══██║░░░██║░░░
██║░░██╗███████╗░░░██║░░░███████╗░██║░░██╗██║░░██║░░░██║░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
""")

def clear_screen_with_logo():
    os.system("cls")  
    show_logo()



show_logo() 

while True:
    print("\rЗапуск программы...", end="")
    time.sleep(0.3)
    
    print("\rЗапуск программы.. ", end="") 
    time.sleep(0.5)
    
    print("\rЗапуск программы.  ", end="")
    time.sleep(1)
    
    print("\rКонец запуска программы")
    time.sleep(0.5)
    
    clear_screen_with_logo() 
    break

count = 0

i = {
"камень": "ножницы",
"ножницы": "бумага",  
"бумага": "камень"    
}

max = 2**32

while True:
    print("""
это игра Камень Ножницы Бумага
выберите до скольки играем?
0 = ∞
""")
    try:
        player_menu = int(input("/// "))
    except ValueError:
        print("вводите числами")
        continue
    if player_menu == 0:
        player_menu += max

    while count < player_menu:
        player = input("Камень ножницы бумага 1. 2.. 3...  ").lower().strip()
        
        if player not in i:
            print("Ошибка! Вводите четко: камень, ножницы или бумага")
            continue
            
        player_2 = random.choice(["камень", "ножницы", "бумага"])
        
        if player == player_2:
            print("Ничья")
            print(f"Очков: {count}")
        elif i[player] == player_2:
            print("Выйграл игрок")
            print(f"Я выбрал: {player_2}")
            count += 1
            print(f"Очков: {count}")
            
        else:
            print("Выйграл компьютер")
            print(f"Я выбрал: {player_2}")
            count -= 1
            if count == -1:
                count += 1
            print(f"Очков: {count}")

    print("ты выиграл")
    break