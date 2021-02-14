def add_num() :
    numf = input('띄어쓰기로 나눠서 숫자를 4개만 입력하세요! : ')
    ans = 0
    num = numf.split(' ')
    for i in range(0,4):
        ans += int(num[i])

    print(ans)

add_num()
