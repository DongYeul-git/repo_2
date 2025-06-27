class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Add(Calculation):
    def result(self):
        return self.a + self.b

class Subtract(Calculation):
    def result(self):
        return self.a - self.b

class Multiply(Calculation):
    def result(self):
        return self.a * self.b

class Divide(Calculation):
    def result(self):
        if self.b == 0:
            return "0으로 나눌 수 없습니다."
        return self.a / self.b

# 예시 사용
if __name__ == "__main__":
    x = float(input("첫 번째 숫자를 입력하세요: "))
    y = float(input("두 번째 숫자를 입력하세요: "))
    print("덧셈:", Add(x, y).result())
    print("뺄셈:", Subtract(x, y).result())
    print("곱셈:", Multiply(x, y).result())
    print("나눗셈:", Divide(x, y).result())