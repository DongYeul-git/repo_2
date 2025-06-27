def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

# 예시 사용
if __name__ == "__main__":
    x = float(input("첫 번째 숫자를 입력하세요: "))
    y = float(input("두 번째 숫자를 입력하세요: "))
    print("덧셈:", add(x, y))
    print("뺄셈:", subtract(x, y))
    print("곱셈:", multiply(x, y))
    print("나눗셈:", divide(x, y))