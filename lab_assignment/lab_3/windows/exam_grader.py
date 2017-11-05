# -*- coding: utf-8 -*-


# 총 과목 수를 Console를 통해 받기
def get_number_of_subjects():

    # """
    # Input:
    # 	- None
    # Output:
    # 	- number_of_subjects: Integer Type의 총 과목 수
    # Examples(python shell):
    # 	>>> import exam_grader as eg
    # 	>>> eg.get_number_of_subjects()
    #   과목수를 입력하세요: 10
    #   10
    # """
    #
    # ===Modify codes below=================
    number_of_subjects = None
    # ======================================
    return number_of_subjects


# Help Funtion - 수정하지 말 것
def sum_of_scores(number_of_subjects):

    total_score = 0
    for i in range(number_of_subjects):
        message = str(i + 1) + "번째 과목의 점수를 입력하세요 : "
        score = int(input(message))
        total_score = total_score + score
    return total_score


# Help Funtion - 수정하지 말 것
def print_exam_grader(average_score):
    grade = 'F'
    if average_score >= 90.0:
        grade = 'A'
    elif average_score >= 80.0:
        grade = 'B'
    elif average_score >= 70.0:
        grade = 'C'
    elif average_score >= 60.0:
        grade = 'D'
    else:
        grade = 'F'
    print("평균 점수: ", average_score)
    print("학     점: ", grade)


def main():
    print("Start of Exam Grader Program")
    print("============================")

    number_of_subjects = get_number_of_subjects()
    total_score = sum_of_scores(number_of_subjects)
    average_score = get_average_score(
        total_score=total_score, number_of_subjects=number_of_subjects)
    print_exam_grader(average_score)

    print("===========================")
    print("End of Exame Grader Program")

if __name__ == '__main__':
    main()
