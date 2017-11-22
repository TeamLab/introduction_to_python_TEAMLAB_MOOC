# -*- coding: utf-8 -*-


def sum_of_list(list_data):
    # '''
    # Input:
    #   - list_data: 숫자 값으로 구성된 list
    #     ex: list_data = [1, 2, 3, 4, 5]
    # Output:
    #   - list_data element의 합
    #
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> gwf.sum_of_list([1, 2, 3])
    #   6
    #   >>> gwf.sum_of_list([5, 5, 10])
    #   20
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def merge_and_sort(list_data_a, list_data_b):
    # '''
    # Input:
    #   - list_data_a: 숫자 값 또는 문자열로만 이루어진 list
    #   - list_data_b: 숫자 값 또는 문자열로만 이루어진 list
    #   ※ list_data_a와 list_data_b의 element들의 data type은 같음
    # Output:
    #   - list_data_a와 list_data_b 두 리스트가 합쳐진 후,
    #     정렬된 값을 반환
    #
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = [1, 2, 3, 10]
    #   >>> b = [5, 6, 7, 8]
    #   >>> gwf.merge_and_sort(a, b)
    #   [1, 2, 3, 5, 6, 7, 8, 10]
    #   >>> a = ['a', 'b', 'z']
    #   >>> b = ['c', 'd', 'f']
    #   >>> gwf.merge_and_sort(a, b)
    #   ['a', 'b', 'c', 'd', 'f', 'z']
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def delete_a_list_element(list_data, element_value):
    # '''
    # Input:
    #   - list_data: 숫자 또는 문자 값으로 이루어진 list
    #   - element_value: 숫자 또는 문자 값
    # Output:
    #   - 만약 list_data에 element_value가 속해 있다면
    #     해당 element_value만 삭제된 list를 반환해주고,
    #     만약 list_data에 element_value가 속해 있지 않다면,
    #     0을 반환해줌
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = [1, 2, 3, 10]
    #   >>> b = 1
    #   >>> gwf.delete_a_list_element(a, b)
    #   [2, 3, 10]
    #   >>> a = ['a', 'b', 'c', 'z']
    #   >>> b = 'd'
    #   >>> gwf.delete_a_list_element(a, b)
    #   0
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def comparison_list_size(list_data_a, list_data_b):
    # '''
    # Input:
    #   - list_data_a: 숫자 또는 문자 값으로 이루어진 list
    #   - list_data_b: 숫자 또는 문자 값으로 이루어진 list
    # Output:
    #   - list_data_a와 list_data_b 중 list의 길이가 긴 값이 반환됨
    #     길이가 같을 경우에는 둘 list_data_a의 값이 반환된다.
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = [1, 2, 3, 4, 5, 6]
    #   >>> b = [1, 2, 3]
    #   >>> gwf.comparison_list_size(a,b)
    #   [1, 2, 3, 4, 5, 6]
    #   >>> b = [1, 2, 3, 5, 7, 8, 9, 10]
    #   >>> gwf.comparison_list_size(a,b)
    #   [1, 2, 3, 5, 7, 8, 9, 10]
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def odd_even_check(a, b):
    # '''
    # Input:
    #   - a : 숫자형 값
    #   - b : 숫자형 값
    # Output:
    #   - a 와 b 합이 짝수이면 "Even" 홀수이면 "Odd"의 문자열 값 반환
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = 5
    #   >>> b = 6
    #   >>> gwf.odd_even_check(a,b)
    #   'Odd'
    #   >>> b = 5
    #   >>> gwf.odd_even_check(a,b)
    #   'Even'
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def discount_price(price):
    # '''
    # Input:
    #   - price : 숫자형 값
    # Output:
    #   - price의 값이 100,000 미만일 경우 10% 할인된 값이 반환,
    #     10만원 이상일 경우 20퍼센트 할인된 값이 반환됨
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> gwf.discount_price(40000)
    #   36000.0
    #   >>> gwf.discount_price(110000)
    #   880000.0
    # '''
    # pass
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def find_smallest_value(list_data):
    # '''
    # Input:
    #   - list_data : 숫자형 값으로 이루어진 list
    # Output:
    #   - list_data의 element중 가장 작은 값이 반환됨
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = [1, 2, 3, 4, 5]
    #   >>> gwf.find_smallest_value(a)
    #   1
    #   >>> a = [5, 4, 3, 0, 100, 200]
    #   >>> gwf.find_smallest_value(a)
    #   0
    # '''
    # pass
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def binary_converter(decimal_number):
    # '''
    # Input:
    #   - decimal_number : integer 형태의 값
    # Output:
    #   - decimal_number의 10진수를 2진수로 변환한 문자열 값
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> gwf.binary_converter(100)
    #   '1100100'
    #   >>> gwf.binary_converter(56)
    #   '111000'
    # '''
    # pass
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result.strip()


def number_of_cases(list_data):
    # '''
    # Input:
    #   - list_data : 숫자 또는 문자 값으로 이루어진 list
    # Output:
    #   - list_data 안에 있는 element 조합의 모든 경우의 수,
    #     ※ 반환되는 list에는 문자열 Type만 들어 있으며
    #        list_data 안에 숫자형 값이 있을 경우 문자열로 변환하여 처리
    #     ※ 중복되는 값은 삭제된 후 반환 되어야 함
    #     ※ 최종결과는 Sorting된 후에 반환되어야 함 
    # Examples:
    #   >>> import gowithflow as gwf
    #   >>> a = ['a', 'b', 'c']
    #   >>> gwf.number_of_cases(a)
    #   ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    #   >>> a = ['a', 'a']
    #   >>> gwf.number_of_cases(a)
    #   ['aa']
    #   >>> a = [1, 2, 3, 'a']
    #   >>> gwf.number_of_cases(a)
    #   ['11', '12', '13', '1a', '21', '22', '23', '2a', '31', '32', '33', '3a', 'a1', 'a2', 'a3', 'aa']
    # '''
    # ===Modify codes below=============
    # 한 줄 이상의 코드로 작성 가능하나,
    # 반드시 결과 값을 result 변수에 할당하여 반환

    result = None

    # ==================================
    return result


def main():
    # ===Test your functions=============
    # 아래 "pass" 부분을 삭제한 후 테스트하고
    # 싶은 코드를 자유롭게 작성하시오
    pass

    # ==================================

if __name__ == "__main__":
    main()
