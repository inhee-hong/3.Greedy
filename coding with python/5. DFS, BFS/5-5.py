# 재귀 함수를 이용하는 대표적인 예제로는 팩토리얼 문제가 있다.
# 수학적으로 0!와 1!의 값은 1로 같다는 성질을 이용하여 팩토리얼 함수는 n이 1이하가 되었을 때 함수를 종료하는 재귀 함수의 형태로 구현 가능


# 팩토리얼을 반복적으로 구현한 방식과 재귀적으로 구현한 방식


# 반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n + 1):
    result *= i
  return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1:                      # n이 1이하인 경우 1을 반환
    return 1
  return n * factorial_recursive(n - 1)   # n! = n * (n-1)!를 그대로 코드로 작성하기

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))



# result
반복적으로 구현: 120
재귀적으로 구현: 120
  
  
# 반복문 대신에 재귀 함수를 사용했을 때 얻을 수 있는 장점 
# --> 수학의 점화식을 소스코드로 옮겼기 때문
# n이 0 혹은 1 일 때 : factorial(n) = 1
# n이 1 보다 클 때 : factorial(n) = n * factorial(n-1)
