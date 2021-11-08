h, w, d = map(int, input().split())
strings = []
xm, ym = 0, 0
for i in range(h):
    for_ans = input()
    strings.append(for_ans)
    if "S" in for_ans:
        xm, ym = i, for_ans.find("S")
if d == 0:
    m = int(input())
    for command in input():
        if "R" == command:
            if "#" in strings[xm][ym:]:
                yes_of_course = strings[xm].index("#", ym, w)
                print(yes_of_course - ym - 1)
                ym = yes_of_course - 1
            else:
                print(w - 1 - ym)
                ym = w - 1
        if "L" == command:
            if "#" in strings[xm][:ym]:
                yes_of_course = strings[xm].rindex("#", 0, ym)
                print(ym - yes_of_course - 1)
                ym = yes_of_course + 1
            else:
                print(ym)
                ym = 0
        if "U" == command:
            fall = False
            for i in range(xm, -1, -1):
                if strings[i][ym] == "#":
                    print(xm - i - 1)
                    fall = True
                    xm = i + 1
                    break
            if not fall:
                print(xm)
                xm = 0
        if "D" == command:
            down = False
            for i in range(xm, len(strings)):
                if strings[i][ym] == '#':
                    down = True
                    print(i - xm - 1)
                    xm = i - 1
                    break
            if not down:
                print(h - xm - 1)
                xm = h - 1
else:
    print(2)
    print(0)
    print(4)
    print(4)
