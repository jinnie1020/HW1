# skeleton code
# 함수 끝의 pass 는 지우셔도 됩니다.
import json
import csv

class Summary:
    """
    data의 summary를 수행할 수 있는 클래스입니다.
    """
    def __init__(self,*args):
        # 클래스 생성자부분입니다.
        # class 선언을 위해 어떤 input 값을 받아야할까요?
        # 받아온 input을 class 내부적으로 사용하기 위해 어떻게 attribute으로 정의하면 될까요?
        # TODO
        pass

    def read_csv(self):
        # csv 를 읽어오는 method입니다.
        # TODO
        pass

    def compute_count(self):
        # 데이터 개수를 새는 method 입니다.
        # TODO
        pass

    def compute_mean(self):
        # 데이터 평균을 계산 method 입니다.
        # TODO
        pass

    def compute_std(self):
        # 데이터 표준편차를 계산 method 입니다.
        # TODO
        pass

    def compute_min(self):
        # 데이터 최소값을 계산 method 입니다.
        # TODO
        pass

    def compute_max(self):
        # 데이터 최대값을 계산 method 입니다.
        # TODO
        pass

    def get_unique_species(self):
        # 본 데이터 Species의 unique한 값만을 리턴합니다.
        # e.g, [1,4,6,3,2,3,2] 중 unique한 값은 [1,2,3,4,6]입니다.
        # e.g, ['a','b','b'] 의 unique한 값은 ['a','b'] 입니다.
        pass

## do_summary.py 를 실행시키면 input을 받습니다.
input_commands = input()
if input_commands == 'exit':
    # 입력된 input이 "exit" 일 경우 'no_summary.txt' 파일을 저장합니다.
    # 'no_summary.txt' 파일 안에는 'you entered exit'이 입력돼있어야합니다.
    # TODO : 텍스트 파일 생성
    pass

elif input_commands == 'do':
    # 입력된 input이 "do" 일 경우, 클래스와 함수를 사용해 아래의 정보를 담은 summary.json 으로 저장합니다.
    # results를 적절한 형태로 완성하면, 마지막에 딕셔너리를 json 으로 변환하는 코드를 사용해 summary.json 을 생성할 수 있습니다.

    results = None
    # results의 데이터 타입은 딕셔너리 형태입니다.
    # 딕셔너리의 키값은 SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species 입니다.
    # 각 키의 아이템값은 리스트입니다.

    # SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm의 아이템은 순서대로 count, mean, std, min, max 입니다.
    # count 데이터 타입은 int 이며, mean, std, min, max 의 타입은 float 입니다.
    # float의 값은 소수점 4째자리까지 표기합니다.(e.g, 3.7777)

    # Species 의 item은 unique한 종류 이름(string)과 그 개수를 담은 리스트입니다.

    # e.g, results = {'SepalLengthCm: [10, 2.5, 3.0, 1.0, 4.0] ,
    #                 'SepalWidthCm': [10, 2.5, 3.0, 1.0, 4.0] ,
    #                 'PetalLengthCm': [10, 2.5, 3.0, 1.0, 4.0] ,
    #                 'PetalWidthCm의': [10, 2.5, 3.0, 1.0, 4.0] ,
    #                 'Species': ['flower1', 'flower2', 'flower3', 3]
    #                 }


    # TODO : 각 method와 construction이 완성된 class를 선언

    # TODO: 정답들이 저장된 results dictionary 생성
    # 클래스의 동작을 조정하기 위한 추가 method, 함수 선언하셔도 됩니다.



    # 위의 results 값을 'summary.json' 형태로 저장합니다.
    with open('summary.json', 'w') as outfile:
        json.dump(results,outfile)

    pass




