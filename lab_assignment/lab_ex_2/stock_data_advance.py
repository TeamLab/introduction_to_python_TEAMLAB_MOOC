# -*- coding: utf8 -*-

import urllib.request
import csv


def is_validate_url(url_address):
    """url_address로 Yahoo 서버에 요청하면 해당 url_address가 사용가능한지에 대해 확인하는 Helper Function
    Args:
        url_address (str): Yahoo 금융 서버에 주식 csv 데이터를 요청하는 URL 주소

    Returns:
        boolean: 데이터가 반환이 되는 주소일 경우 True, 그렇지 않으면 False

    Examples:
        >>> import stock_data_advance  as sdc
        >>> url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> sdc.is_validate_url(url)
        True
        >>> url = 'http://real-chart.finance.yahoo.com/table.csv?s=075930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> sdc.is_validate_url(url)
        False

    """
    r = urllib.request.urlopen(url_address)
    stock_data_string = r.read().decode("utf8")
    result = None

    try:
        urllib.request.urlopen(url_address)
        return True
    except urllib.error.URLError as e:
        return False


def is_validate_date(date_str):
    """ 문자열로 yyyy/mm/dd의 형태로된 날짜 정보를 입력받아 아래의 조건에 맞는 경우 True, 그렇지 않을경우 False를 반환
        1) 입력된 데이터를 "/"를 구분자로 나눴을 경우, 길이가 3이어야 함
        2) yyyy: 년도는 2001년 부터 2015년까지 입력됨
        3) mm: 월(month)정보는 1월 부터 12월까지 입력됨
        4) dd: 일(day)는 1일 부터 31일까지 입력됨(월에 상관없음)

    Args:
        date_str (str): yyyy/mm/dd의 형태로된 날짜 정보

    Returns:
        boolean: 상단 조건에 맞을 경우 True, 그렇지 않으면 False를 반환

    Examples:
        >>> import stock_data_advance  as sdc
        >>> date_str = "1992/1/12"
        >>> sdc.is_validate_date(date_str)
        False
        >>> sdc.is_validate_date("2001/12/13")
        True
        >>> sdc.is_validate_date("2014/12/13")
        True
        >>> sdc.is_validate_date("2014/15/13")
        False
    """

    result = None
    # ===Modify codes below=============

    # ==================================
    return result

def is_validate_command(command_str, header_data):
    """ 사용자의 입력값과 stock_data의 header 값을 입력받아 사용자의 입력값이 처리가능할 경우 True,
    그렇지 않을 경우 False를 반환함

    Note:
        1) 유저의 입력값은 "-"으로 나눠짐
        2) 유저의 입력값의 예제는 아래와 같으며 각각 다음과 같은 의미를 가짐짐
            ALL-005930.KS-2014/12/01-2015/12/30
            명령어-주식코드-시작년/월/일-종료년/월/일
            ALL-005930.KS-2014/12/01-2015/12/30-example.csv
            명령어-주식코드-시작년/월/일-종료년/월/일-저장하고자 하는 파일명

        3) 입력 변수 command_str를 "-" 나눴을 경우 길이는 4 또는 5이여야 함
        4) command_str를 "-"으로 나눴을 경우, 0번째 Index의 값은 ALL또는 header_field에 있는 값 이어야 함
           또한 대소문자는 구분하지 않아야 함
        5) command_str를 "-"으로 나눴을 경우, 2,3번째 is_validate_date에 입력시 True를 반환해야 함
        6) command_str를 "-"으로 나눴을 경우, 1,2,3번째의 값으로 yahoo 금융서버에 접속하는 url을 생성한 후
           is_validate_url에 입력시 True를 반환해야 함

    Args:
        command_str (str): 유저가 입력한 명령어
        header_data (list): 다운로드한 Stock Data의 header field

    Returns:
        boolean: 상단 조건에 맞을 경우 True, 그렇지 않으면 False를 반환

    Examples:
        >>> import stock_data_advance  as sdc
        >>> command_str = "ALL-005930.KS-2014/12/01-2015/12/30"
        >>> header = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        >>> sdc.is_validate_command(command_str,header)
        True
        >>> command_str = "ALL-005931.KS-2014/12/01-2015/12/30"
        >>> sdc.is_validate_command(command_str,header)
        Not Found
        False
        >>> command_str = "ALL-005935.KS-2014/12/01-2015/12/30"
        >>> sdc.is_validate_command(command_str,header)
        True
        >>> command_str = "ALL-005935.KS-2014/13/01-2015/13/30"
        >>> sdc.is_validate_command(command_str,header)
        False
        >>> sdc.is_validate_command(command_str,header)
        False
        >>> command_str = "ALL-005935.KS-2001/1/1-2015/12/30"
        >>> sdc.is_validate_command(command_str,header)
        True
        >>>
    """

    result = None
    # ===Modify codes below=============

    # ==================================
    return result

def make_stock_data_url(s=None, a=None, b=None, c=None, d=None, e=None, f=None, g="d"):

    """ yahoo finance의 csv 다운로드 입력 url를 입력된 7개의 변수를 바탕으로  생성함
    base_url은 "http://real-chart.finance.yahoo.com/table.csv?" 이며, 차례로 입력변수로 아래와 같은 주소를 만듦

    http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d

    각 변수별로 의미는 아래와 같음

    Args:
        s (str): 데이터를 받고자 하는 회사의 주식 코드, KOSPI에 상장된 회사는 끝에 .KS를 붙임 ex) 075930.KS
        a (int): 데이터를 받고자 하는 시작날짜의 월 정보를 입력함, 0 부터 시작됨
        b (int): 데이터를 받고자 하는 시작날짜의 일 정보를 입력함
        c (int): 데이터를 받고자 하는 시작날짜의 년도 정보을 입력함
        d (int): 데이터를 받고자 하는 마지막 날짜의 월 정보를 입력함, 0 부터 시작됨
        e (int): 데이터를 받고자 하는 마지막 날짜의 일 정보를 입력함
        f (int): 데이터를 받고자 하는 마지막 날짜의 년도 정보를 입력함
        g (str): 데이터를 받고자 하는 주기를 입력함, 기본 정보는 "day"를 의미하는 d로 설정


    Returns:
        str: 입력된 변수들을 yahoo 서버에 접근하는 url을 생성

    Examples:
        >>> import answer_stock_data_advance as sdc
        >>> sdc.make_stock_data_url(s="005930.KS", a=1, b=10, c=2014, d=12, e=10, f=2015)
        'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=10&c=2014&d=11&e=10&f=2015&g=d'
        >>> sdc.make_stock_data_url(s="005935.KS", a=11, b=1, c=2014, d=12, e=10, f=2015)
        'http://real-chart.finance.yahoo.com/table.csv?s=005935.KS&a=10&b=1&c=2014&d=11&e=10&f=2015&g=d'    
    """

    base_url = 'http://real-chart.finance.yahoo.com/table.csv'
    result = None
    # ===Modify codes below=============

    # ==================================
    return result


def get_stock_data(url_address):
    """url_address로 Yahoo 서버에 요청하면 해당 정보를 다운로드 받은후 Two Dimensional List 변환하여 반환함

    아래 코드를 활용하면 Yahoo 서버에서 데이터를 String Type으로 다운로드 받을 수 있음

        >>> url_address = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> r = urllib.request.urlopen(url_address)
        >>> stock_data_string = r.read().decode("utf8")    # String Type으로 다운로드 받은 데이터
        >>> stock_data_string[:100]
    'Date,Open,High,Low,Close,Volume,Adj Close\n2015-11-06,1343000.00,1348000.00,1330000.00,1338000.00,164'

    다운된 데이터는 String Type으로 각 줄은 "\n"으로 구분되며, 필드 데이터들은 ","으로 구분됨

    Args:
        url_address (str): Yahoo 금융 서버에 주식 csv 데이터를 요청하는 URL 주소

    Returns:
        list: Two Dimensioanl List 0번째 index에는 필드의 Header 정보를 포함하고 있으며,
        1번째 index부터 각 필드의 data를 가지고 있음

    Examples:
        >>> import stock_data_advance as sdc
        >>> url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> sdc.get_stock_data(url)[:3]
        [['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], ['2015-11-06',
         '1343000.00', '1348000.00', '1330000.00', '1338000.00', '164300', '1338000.00']
        , ['2015-11-05', '1330000.00', '1354000.00', '1330000.00', '1342000.00', '173000
        ', '1342000.00']]
    """
    r = urllib.request.urlopen(url_address)
    stock_data_string = r.read().decode("utf8")
    result = None
    # ===Modify codes below=============

    # ==================================
    return result


def get_header_data(stock_data):
    """get_stock_data 함수의 Return 값에서 Header 값만 추출하여 list로 반환함

    Args:
        stock_data (list): get_stock_data 함수의 Return 값으로 나온 주식 정보 two dimensional list

    Returns:
        list: 입력된 stcok_data list 값 중 0번째 index에 있는 header 정보만 추출하여 반환함

    Examples:
        >>> import stock_data_advance as sdc
        >>> url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> stock_data = sdc.get_stock_data(url)
        >>> sdc.get_header_data(stock_data)
        ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    """
    result = None
    # ===Modify codes below=============

    # ==================================
    return result


def get_attribute_data(stock_data, attribue):
    """get_stock_data 함수의 Return 값,추출하고자 하는 Header의 이름을 입력받으면 해당 조건의 값만 추출하여 list로 반환함

    Args:
        stock_data (list): get_stock_data 함수의 Return 값으로 나온 주식 정보 two dimensional list
        attribue (str): 추출하고자 하는 필드의 Header 이름, 대소문자를 구분하지 않음

    Returns:
        list: 입력된 조건에 맞는 값을 header를 포함하여 list로 추출하여 반환함

    Examples:
        >>> import stock_data_advance as sdc
        >>> url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> stock_data = sdc.get_stock_data(url)
        >>> header = sdc.get_header_data(stock_data)
        >>> sdc.get_attribute_data(stock_data, "High")[:2]
        [['Date', 'High'], ['2015-11-17', '1290000.00']]
        >>> sdc.get_attribute_data(stock_data, "HIgh")[:2]
        [['Date', 'High'], ['2015-11-17', '1290000.00']]
        >>> sdc.get_attribute_data(stock_data, header[1])[:2]
        [['Date', 'Open'], ['2015-11-17', '1275000.00']]
        >>> sdc.get_attribute_data(stock_data, header[2])[:2]
        [['Date', 'High'], ['2015-11-17', '1290000.00']]
        >>> sdc.get_attribute_data(stock_data, "close")[:2]
        [['Date', 'Close'], ['2015-11-17', '1270000.00']]
    """

    result = None
    # ===Modify codes below=============

    # ==================================
    return result

def write_csv_file_by_result(stock_data, filename):
    """stock_data를 가지고 있는 two dimensional list 값을 csv 파일로 생성함

    Args:
        stock_data (list): 저장하고자 하는 주식 정보 two dimensional list
        filename (str): 데이터가 저장될 파일이름

    Examples:
        >>> import stock_data_advance as sdc
        >>> url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2015&g=d'
        >>> stock_data = sdc.get_stock_data(url)
        >>> high_data = sdc.get_attribute_data(stock_data, "High")
        >>> sdc.write_csv_file_by_result(stock_data,"example.csv")
        >>> f = open("example.csv", "r", encoding="utf8")
        >>> f.read()[:100]
        'Date,Open,High,Low,Close,Volume,Adj Close\n2015-11-17,1275000.00,1290000.00,1270000.00,1270000.00,186'
        >>> f.close()
    """
    result = None
    # ===Modify codes below=============

    # ==================================
    return result


def separate_user_query(user_input):
    """사용자의 입력 값을 "-" 기준으로 나눠 list로 반환하며 반드시 각 list에 값들은 빈칸이 제거된 후 저장되어야함

    Args:
        user_input (str): 사용자가 입력하는 데이터 ex)  ALL-005930.KS-2014/12/01-2015/12/30

    Returns:
        list: user_input을 "," 기준으로 분할하여 list 값으로 반환함, 단 각 list에 있는 값들은 양쪽 공백이 제거되어야 함

    Examples:
        >>> import stock_data_advance as sdc
        >>> sdc.separate_user_query(" ALL-005930.KS-2014/12/01-2015/12/30")
        ['ALL', '005930.KS', '2014/12/01', '2015/12/30']
        >>> sdc.separate_user_query("    ALL-005930.KS-2014/12/01-2015/12/30-example.csv
        ")
        ['ALL', '005930.KS', '2014/12/01', '2015/12/30', 'example.csv']
        >>> sdc.separate_user_query("  High - 005930.KS- 2014/12/01- 2015/12/30")
        ['High', '005930.KS', '2014/12/01', '2015/12/30']
    """
    result = None
    # ===Modify codes below=============

    # ==================================
    return result


def main():
    print("Stock Data Crawler Program!!")
    user_input = 999
    # ===Modify codes below=============

    # ==================================

if __name__=="__main__":
    main()