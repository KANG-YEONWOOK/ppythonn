i, hap = 0, 0                                 ##변수들의 초기값 지정
for i in range(0, 101, 2) :                   ##i가 0~100까지의 짝수 일때 
    hap = hap + i                             ##hap에 i값 누적
print("0에서 100까지의 짝수의 합 : %d" % hap) ##출력
