def addition(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #   -두 값의 합
    # Examples:
    #   >>> addition(3,5)
    #   8
    #   >>> addition(3,2)
    #   5
    # '''
    # pass
    # ===Modify codes below=============

    result = None

    # ==================================

    return result


def minus(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #   -두 값의 차
    # Examples:
    #   >>> minus(3,5)
    #   -2
    #   >>> minus(3,2)
    #   1
    # '''
    # pass
    # ===Modify codes below=============

    result = None

    # ==================================

    return result


def multiplication(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #   -두 값의 곱
    # Examples:
    #   >>> multiplication(3,5.1)
    #   15.3
    #   >>> multiplication(3,2)
    #   6
    # '''
    # pass
    # ===Modify codes below=============

    result = None

    # ==================================

    return result


def division(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #   -a를 b로 나눈 값
    # Examples:
    #   >>> division(5,5)
    #   1
    #   >>> division(4,2)
    #   2
    # '''
    # pass
    # ===Modify codes below=============

    result = None

    # ==================================

    return result


def main():
    print ("Addition Test")
    print (addition(3,5)) # Expected Result: 8
    print (addition(10,5) == 15) # Expected Result: True
    print ("Addition Test Closed \n")


    print ("Minus Test")
    print (minus(3,5)) # Expected Result: -2
    print (minus(10,5) == 5) # Expected Result: True
    print (minus(10,15) == 5) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("Multiplication Test")
    print (multiplication(3,5)) # Expected Result: 15
    print (multiplication(10,5) == 50) # Expected Result: True
    print (multiplication(10,-3) == 20) # Expected Result: False
    print ("Addition Test Closed \n")

    print ("division Test")
    print (division(5,5)) # Expected Result: 1
    print (division(5,4)) # Expected Result: 1.25
    print (division(10,5) == 2) # Expected Result: True
    print (division(10,-3) == 0.33333) # Expected Result: False
    print ("division Test Closed \n")


if __name__ == "__main__":
    main()
