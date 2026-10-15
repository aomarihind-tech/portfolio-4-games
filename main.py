import random

def hajar_waraqa_mi9as():
    print("\n=== حجرة ورقة مقص ===")
    options = ["حجرة", "ورقة", "مقص"]
    while True:
        user = input("اختاري حجرة/ورقة/مقص (كتبي خروج باش تخرجي): ").strip()
        if user == "خروج":
            break
        if user not in options:
            print("كتبي غير حجرة ولا ورقة ولا مقص")
            continue
        comp = random.choice(options)
        print(f"الكومبيوتر دار: {comp}")
        if user == comp:
            print("تعادل!")
        elif (user=="حجرة" and comp=="مقص") or (user=="مقص" and comp=="ورقة") or (user=="ورقة" and comp=="حجرة"):
            print("ربحتي! برافو!")
        else:
            print("خسرتي!")

def guess_number():
    print("\n=== خمن الرقم ===")
    num = random.randint(1, 100)
    tries = 0
    while True:
        try:
            g = int(input("خمن رقم من 1 ل 100: "))
            tries += 1
            if g < num: print("زايد شوية لفوق ⬆️")
            elif g > num: print("نقص شوية لتحت ⬇️")
            else:
                print(f"برافو لقيتيه! درتي {tries} محاولات")
                break
        except:
            print("كتبي رقم!")

def hangman():
    print("\n=== Hangman - لعبة الحروف ===")
    words = ["مغرب", "حاسوب", "مدرسة", "كتاب"]
    word = random.choice(words)
    guessed = ["_"]*len(word)
    lives = 6
    used = []
    while lives > 0 and "_" in guessed:
        print(" ".join(guessed), f"| باقي {lives} | استعملتي: {used}")
        c = input("كتبي حرف: ").strip()
        if c in used: continue
        used.append(c)
        if c in word:
            for i,ch in enumerate(word):
                if ch==c: guessed[i]=c
        else:
            lives -= 1
    if "_" not in guessed: print("ربحتي!")
    else: print(f"خسرتي! الكلمة كانت: {word}")

def xo():
    print("\n=== X O ===")
    board = [" "] * 9
    def show():
        print(f"{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")
    def win(p):
        return any(board[a]==board[b]==board[c]==p for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])
    turn = "X"
    for _ in range(9):
        show()
        try:
            m = int(input(f"دور {turn} (1-9): "))-1
            if board[m]!=" ": continue
            board[m]=turn
            if win(turn):
                show()
                print(f"اللاعب {turn} ربح!")
                return
            turn="O" if turn=="X" else "X"
        except: continue
    show()
    print("تعادل!")

while True:
    print("\n--- بورتفوليو الألعاب - نادية ---")
    print("1) حجرة ورقة مقص")
    print("2) خمن الرقم")
    print("3) Hangman")
    print("4) X O")
    print("0) خروج")
    c = input("اختاري رقم: ")
    if c=="1": hajar_waraqa_mi9as()
    elif c=="2": guess_number()
    elif c=="3": hangman()
    elif c=="4": xo()
    elif c=="0": break
