# -*- coding: utf8 -*-

def get_zero_matrix(size):
    # '''
    # Input:
    #   - size : 정수형 값
    # Output:
    #   - size * size 크기의 two dimensional list를 반환함
    #   - list내 모든 값은 다 0으로 입력되어 있음
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.get_zero_matrix(3)
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # >>> ms.get_zero_matrix(4)
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # >>> base_matrix = ms.get_zero_matrix(4)
    # >>> base_matrix[0][0] = 1
    # >>> base_matrix
    # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # >>> base_matrix = ms.get_zero_matrix(7)
    # >>> base_matrix
    # [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0,
    # 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    # '''

    base_matrix = []
    # ===Modify codes below=============

    # ==================================
    return base_matrix

def is_validate_number(user_input):
    # '''
    # Input:
    #   - user_input : 문자열
    # Output:
    #   - 입력된 문자열이 정수형 문자열이며, 3보다 크고 20보다 작을 경우는 True
    #     그렇지 않을 경우에는 False를 반환함
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.is_validate_number("10")
    # True
    # >>> ms.is_validate_number("abc")
    # False
    # >>> ms.is_validate_number("1111")
    # False
    # >>> ms.is_validate_number("10.5")
    # False
    # >>> ms.is_validate_number("3")
    # True
    # >>> ms.is_validate_number("2")
    # False
    # >>> ms.is_validate_number("1")
    # False
    # '''

    result = None
    # ===Modify codes below=============

    # =================================
    return result

def is_4even_number(size):
    # '''
    # Input:
    #   - size : 정수값
    # Output:
    #   - size가 4의 배수일 경우 True
    #     그렇지 않을 경우에는 False를 반환함
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.is_4even_number(16)
    # True
    # >>> ms.is_4even_number(32)
    # True
    # >>> ms.is_4even_number(4)
    # True
    # >>> ms.is_4even_number(8)
    # True
    # >>> ms.is_4even_number(10)
    # False
    # >>> ms.is_4even_number(12)
    # True
    # >>> ms.is_4even_number(3)
    # False
    # >>> ms.is_4even_number(7)
    # False
    # '''

    result = None
    #  ===Modify codes below=============

    # ===================================
    return result

def is_odd_number(size):
    # '''
    # Input:
    #   - size : 정수값
    # Output:
    #   - size가 홀수 일 경우 True
    #     그렇지 않을 경우에는 False를 반환함
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.is_odd_number(3)
    # True
    # >>> ms.is_odd_number(4)
    # False
    # >>> ms.is_odd_number(5)
    # True
    # >>> ms.is_odd_number(7)
    # True
    # >>> ms.is_odd_number(8)
    # False
    # >>> ms.is_odd_number(19)
    # True
    # >>> ms.is_odd_number(10)
    # False
    # '''

    result = None
    #  ===Modify codes below=============

    # ===================================
    return result

def get_4even_magic_square(user_input):
    # '''
    # Input:
    #   - user_input : 4의 배수인 정수형 문자열
    # Output:
    #   - user_input * user_input 크기의 마방진 list를 배열함
    #     ※ 출력되는 값은 반드시 아래와 같을 필요가 없음
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.get_4even_magic_square(4)
    # [[1, 15, 14, 4], [12, 6, 7, 9], [8, 10, 11, 5], [13, 3, 2, 16]]
    # >>> ms.get_4even_magic_square(12)
    # [[1, 2, 3, 141, 140, 139, 138, 137, 136, 10, 11, 12], [13, 14, 15, 129, 128, 127
    # , 126, 125, 124, 22, 23, 24], [25, 26, 27, 117, 116, 115, 114, 113, 112, 34, 35,
    #  36], [108, 107, 106, 40, 41, 42, 43, 44, 45, 99, 98, 97], [96, 95, 94, 52, 53,
    # 54, 55, 56, 57, 87, 86, 85], [84, 83, 82, 64, 65, 66, 67, 68, 69, 75, 74, 73], [
    # 72, 71, 70, 76, 77, 78, 79, 80, 81, 63, 62, 61], [60, 59, 58, 88, 89, 90, 91, 92
    # , 93, 51, 50, 49], [48, 47, 46, 100, 101, 102, 103, 104, 105, 39, 38, 37], [109,
    #  110, 111, 33, 32, 31, 30, 29, 28, 118, 119, 120], [121, 122, 123, 21, 20, 19, 1
    # 8, 17, 16, 130, 131, 132], [133, 134, 135, 9, 8, 7, 6, 5, 4, 142, 143, 144]]
    # >>> ms.get_4even_magic_square(8)
    # [[1, 2, 62, 61, 60, 59, 7, 8], [9, 10, 54, 53, 52, 51, 15, 16], [48, 47, 19, 20,
    #  21, 22, 42, 41], [40, 39, 27, 28, 29, 30, 34, 33], [32, 31, 35, 36, 37, 38, 26,
    #  25], [24, 23, 43, 44, 45, 46, 18, 17], [49, 50, 14, 13, 12, 11, 55, 56], [57, 5
    # 8, 6, 5, 4, 3, 63, 64]]
    # '''
    magic_sqaure_matrix = []

    #  ===Modify codes below=============


    #  ===================================
    return magic_sqaure_matrix

def get_odd_magic_square(user_input):
    # '''
    # Input:
    #   - user_input : 홀수인 정수형 문자열
    # Output:
    #   - user_input * user_input 크기의 마방진 list를 배열함
    #     ※ 출력되는 값은 반드시 아래와 같을 필요가 없음
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.get_odd_magic_square(3)
    # [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    # >>> ms.get_odd_magic_square(5)
    # [[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3]
    # , [11, 18, 25, 2, 9]]
    # >>> ms.get_odd_magic_square(7)
    # [[30, 39, 48, 1, 10, 19, 28], [38, 47, 7, 9, 18, 27, 29], [46, 6, 8, 17, 26, 35,
    #  37], [5, 14, 16, 25, 34, 36, 45], [13, 15, 24, 33, 42, 44, 4], [21, 23, 32, 41,
    #  43, 3, 12], [22, 31, 40, 49, 2, 11, 20]]
    # >>> ms.get_odd_magic_square(13)
    # [[93, 108, 123, 138, 153, 168, 1, 16, 31, 46, 61, 76, 91], [107, 122, 137, 152,
    # 167, 13, 15, 30, 45, 60, 75, 90, 92], [121, 136, 151, 166, 12, 14, 29, 44, 59, 7
    # 4, 89, 104, 106], [135, 150, 165, 11, 26, 28, 43, 58, 73, 88, 103, 105, 120], [1
    # 49, 164, 10, 25, 27, 42, 57, 72, 87, 102, 117, 119, 134], [163, 9, 24, 39, 41, 5
    # 6, 71, 86, 101, 116, 118, 133, 148], [8, 23, 38, 40, 55, 70, 85, 100, 115, 130,
    # 132, 147, 162], [22, 37, 52, 54, 69, 84, 99, 114, 129, 131, 146, 161, 7], [36, 5
    # 1, 53, 68, 83, 98, 113, 128, 143, 145, 160, 6, 21], [50, 65, 67, 82, 97, 112, 12
    # 7, 142, 144, 159, 5, 20, 35], [64, 66, 81, 96, 111, 126, 141, 156, 158, 4, 19, 3
    # 4, 49], [78, 80, 95, 110, 125, 140, 155, 157, 3, 18, 33, 48, 63], [79, 94, 109,
    # 124, 139, 154, 169, 2, 17, 32, 47, 62, 77]]
    # '''
    magic_sqaure_matrix = []

    #  ===Modify codes below=============


    #  ===================================
    return magic_sqaure_matrix

def is_magic_sqaure(square):
    # '''
    # Input:
    #   - square : n by n 사이즈로 이루어진 two dimensional list
    # Output:
    #   - 만약 square가 완벽히 마방진 형태이면 True
    #     그렇지 않을 경우 False
    # Examples:
    # >>> import magic_square as ms
    # >>> ms.is_magic_sqaure([[1,2,3],[4,5,6],[7,8,9]])
    # False
    # >>> ms.is_magic_sqaure([[5,5,5],[4,5,6],[7,8,9]])
    # False
    # >>> ms.is_magic_sqaure([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    # True
    # '''
    result = None
    # ===Modify codes below=============

    # ================================
    return result

def main():
    user_input = 999
    print("Play Magic Square Game!!")
    # ===Modify codes below=============

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()