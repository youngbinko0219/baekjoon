vowel = ["a","e","i","o","u","A","E","I","O","U"]
while True:
    cnt = 0
    a = input()
    if a == "#":
        break
    for i in a:
        if i in vowel:
            cnt += 1
    print(cnt)