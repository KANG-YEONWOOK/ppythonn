import time
nums = input('숫자 4개를 쉼표로 구분해서 타이핑해주세여~!^^\n')
a, b, c, d = nums.split(',')
e = int(a) + int(b) + int(c) + int(d)
print('{}, {}, {}, {}의 합은 {}입니다!!!\n계산천재 강연욱~^^\n못하는게 뭐야~~'.format(a, b, c, d, e))
time.sleep(1)
print("안녕~ㅎㅎ")
input()
