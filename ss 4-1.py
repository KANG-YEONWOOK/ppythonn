money = int(input("지폐로 교환할 돈의 액수를 써주세요 : "))    ##지폐로 환산할 돈의 액수를 입력받는다

yellow = money//50000                                      ##5만원짜리 지폐의 개수를 나타내는 변수 yellow에
                                                               ##전체 돈의 액수를 50000으로 나눈 몫을 저장한다.
rest = money%50000                                             ##전체 돈의 액수를 50000으로 나눈 나머지를 변수 rest에 저장한다.
green = rest//10000                                        ##전체에서 50000원짜리를 제외하고 남은 돈의 액수를 10000으로 나눈
                                                               ##몫을 변수 green에 저장한다.
rest = rest%10000                                              ##위의 나머지값을 10000으로 나눈 나머지를 rest에 다시 저장한다.
gold = rest//5000                                          ##변수 gold에 rest를 5000으로 나눈 몫을 저장한다.
rest = rest%5000                                               ##변수 rest에 저장된값을 5000으로나눈 나머지를 rest에 다시 저장한다.
blue = rest//1000                                          ##변수 blue에 rest를 1000으로 나눈 몫을 저장한다.
rest = rest%1000                                               ##rest를 1000으로 나눈 나머지는 지폐로 환산할 수 없는 돈이다.

print("50000짜리 ===> ", yellow,"장")                          ##계산결과를 출력한다.
print("10000짜리 ===> ", green,"장")
print("5000짜리 ===> ", gold,"장")
print("1000짜리 ===> ", blue,"장")
print("지폐로 바꾸지 못한 돈 ===> ", rest,"원")
