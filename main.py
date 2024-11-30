# main.py
# pandas, matplotlib.pyplot 외부 모듈 필요

import module_a
import module_b

data = module_a.read_sunung('20231231.csv')
main_subjects, sub_subjects = module_a.get_subjects(data)

# 과목명 선택 함수
def choose_subject(main_subjects, sub_subjects):

    # 영역 확인
    print('(확인 가능한 영역)')
    for i in main_subjects:
        print(i)
    main_choice = input('영역을 입력하세요 : ')

    # 유형 확인
    sub_choice = None
    if main_choice in ['사회탐구', '과학탐구', '직업탐구']:
        print('유형을 선택해주세요.')
        for i in sub_subjects[main_choice]:
            print(i)
        sub_choice = input('유형을 입력하세요 :')

    return main_choice, sub_choice

if __name__ == "__main__":
    print('<대학수학능력시험 표준점수 분포 그래프 생성 프로그램>')

    main_choice, sub_choice = choose_subject(main_subjects, sub_subjects)
    combined_data = module_a.process_subject_data(data, main_choice, sub_choice)
    module_b.create_graph(combined_data, sub_choice)