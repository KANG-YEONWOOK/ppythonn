import time
president = input('당신이 싫어하는 대통령의 이름을 공백으로 구분해서 3명 적어주세요 \n')
a, b, c = president.split(' ')
d = '씨발련'
e = '최강연욱!!'

l1 = [a, b, c]                  # 리스트 만들기
if '강연욱' in l1:              # 만약 '강연욱'이 리스트 안에 있다면
    print(e)                    # 'e'를 프린트해라
    input()
else:
    print('{}병신 {}병신 {}병신 셋다 {}'.format(a,b,c,d))
    time.sleep(1)
    print('할말은 하는 멋진욕쟁이 최강연욱!!')
    input()
