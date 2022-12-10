# my answer
## 풀이 : sqrt는 런타임 에러 발생! integer인 경우에 사용 가능한 isqrt를 사용하자.
## 0.5를 제곱하는 방법 또한 런타임 에러 발생! 

import math
n = int(input())
print(math.isqrt(n))