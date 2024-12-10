# module_a.py

import pandas as pd

#엑셀에서 데이터 불러오기
def read_sunung(file_path):
    data = pd.read_csv(file_path, encoding='euc-kr')
    return data

#과목 목록 반환
def get_subjects(data):
    main_subjects = data['영역'].drop_duplicates().tolist()
    sub_subjects = {
        subject: data[data['영역'] == subject]['유형'].drop_duplicates().tolist()
        for subject in main_subjects if subject in ['사회탐구', '과학탐구', '직업탐구']
    }
    return main_subjects, sub_subjects

#과목 필터링 및 남녀 데이터 병합
def process_subject_data(data, subject, subsubject=None):

    # 과목 필터링
    filtered_data = data[data['영역'] == subject]

    # 세부 과목이 지정된 경우 추가 필터링
    if subsubject:
        filtered_data = filtered_data[filtered_data['유형'] == subsubject]

    # 남녀 데이터 분리
    male_data = filtered_data[['표준점수', '남자']].rename(columns={'남자': '남성 빈도수'})
    female_data = filtered_data[['표준점수', '여자']].rename(columns={'여자': '여성 빈도수'})

    # 데이터 병합
    combined_data = pd.merge(male_data, female_data, on='표준점수', how='outer')

    return combined_data


# 실행 코드
if __name__ == "__main__":
    year = input("연도 선택(2020, 2021, 2022, 2023) : ")
    years ={"2020": "20201231.csv",
            "2021": "20211231.csv",
            "2022": "20221231.csv",
            "2023": "20231231.csv",}
    if year in years:
        file_path = years[year]
        data = read_sunung(file_path)

        if data is not None:
            main_subjects, sub_subjects = get_subjects(data)
            print("사용 가능한 과목:", main_subjects)

            subject = input("분석할 과목을 선택하세요: ")

            if subject in main_subjects:
                if subject in sub_subjects:
                    print(f"사용 가능한 세부 과목 ({subject}):", sub_subjects[subject])
                    subsubject = input("분석할 세부 과목을 선택하세요: ")

                    if subsubject in sub_subjects[subject]:
                        combined_data = process_subject_data(data, subject, subsubject)
                        print(f"\n[{subject} - {subsubject}] 데이터:\n", combined_data)
                    else:
                        print("잘못된 세부과목을 입력하셨습니다. 프로그램을 종료합니다.")
                else:
                    combined_data = process_subject_data(data, subject)
                    print(f"\n[{subject}] 데이터:\n", combined_data)
            else:
                print("잘못된 과목명을 입력하셨습니다. 프로그램을 종료합니다.")
    else:
        print("잘못된 연도를 입력하셨습니다. 프로그램을 종료합니다.")
