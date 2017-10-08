def calculateRectangleArea(x, y):          # 사각형의 넓이를 구하는 함수
    print("함수가 실행중입니다.")
    return x * y

rectangle_x = 10
rectangle_y = 20
print("사각형 x의 길이: ", rectangle_x)
print("사각형 y의 길이: ", rectangle_y)
print("사각형의 넓이: ",
      calculateRectangleArea(rectangle_x, rectangle_y))  # 넓이를 구하는 함수 호출
