a = ord('A')                                  ##알파벳'A'를 아스키코드값으로 변환한 값을 변수 a에 저장한다.
mask = 0x0F                                   ##변수 mask에 16진수 0x0F값을 저장한다.

print("%x & %x = %x" % (a, mask, a & mask))   ##"a & mask값 = a와 mask값의 논리곱"형식으로 출력되도록한다.
print("%X & %X = %X" % (a, mask, a | mask))   ##"a & mask값 = a와 mask값의 논리합"형식으로 출력되도록한다.

mask = ord('a') - ord('A')                    ##변수 mask에 'a'의 아스키코드값과'A'의 아스키코드값 차이를 저장한다.

b = a ^ mask                                  ##변수 b에 a와 변수 mask값의 배타적 논리합을 저장한다.
print("%c ^ %d = %c" % (a, mask, b))          ##"a ^ mask값 = a와 mask값의 배타적 논리합"형식으로 출력되도록한다.
a = b ^ mask                                  ##변수 a에 b와 변수 mask값의 배타적 논리합을 저장한다.
print("%c ^ %d = %c" % (b, mask, a))          ##"b ^ mask값 = a값"형식으로 출력되도록한다.
