money = int(input("지폐로 교환할 돈의 액수를 써주세요 : "))    ##지폐로 환산할 돈의 액수를 입력받는다

yellow = money//50000                                      ##5만원짜리 지폐의 개수를 나타내는 변수 yellow에
                                                               ##전체 돈의 액수를 50000으로 나눈 몫을 저장한다.
money = money%50000                                             ##전체 돈의 액수를 50000으로 나눈 나머지를 변수 money에 저장한다.
green = money//10000                                        ##전체에서 50000원짜리를 제외하고 남은 돈의 액수를 10000으로 나눈
                                                               ##몫을 변수 green에 저장한다.
money = money%10000                                              ##위의 나머지값을 10000으로 나눈 나머지를 money에 다시 저장한다.
gold = money//5000                                          ##변수 gold에 money를 5000으로 나눈 몫을 저장한다.
money = money%5000                                               ##변수 money에 저장된값을 5000으로나눈 나머지를 money에 다시 저장한다.
blue = money//1000                                          ##변수 blue에 money를 1000으로 나눈 몫을 저장한다.
money = money%1000
cccc = money//500                                           ## 바꿀 수 있는 500원짜리 동전의 개수를 구한다
money = money%500                                           ## money에 저장된 값을 500으로 나눈 나머지를 money에 다시 저장한다.
ccc = money//100                                            ## 바꿀 수 있는 100원짜리 동전의 개수를 구한다
money = money%100                                           ## money에 저장된 값을 100으로 나눈 나머지를 money에 다시 저장한다.
cc = money//50                                              ## 바꿀 수 있는 50원짜리 동전의 개수를 구한다
money = money%50                                            ## money에 저장된 값을 50으로 나눈 나머지를 money에 다시 저장한다.
c = money//10                                               ## 바꿀 수 있는 10원짜리 동전의 개수를 구한다
money = money%10                                               ##money를 10으로 나눈 나머지는 화폐로 환산할 수 없는 돈이다.

print("50000원 ===> ", yellow,"장")                          ##계산결과를 출력한다.
print("10000원 ===> ", green,"장")
print("5000원 ===> ", gold,"장")
print("1000원 ===> ", blue,"장")
print("500원 ===> ", cccc,"개")
print("100원 ===> ", ccc,"개")
print("50원 ===> ", cc,"개")
print("10원 ===> ", c,"개")
print("지폐로 바꾸지 못한 돈 ===> ", money,"원")
