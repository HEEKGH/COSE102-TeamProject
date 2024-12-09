
import matplotlib.pyplot as plt

def create_graph(df, subject):
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize = (20,6))

    # x축 값 :표준점수
    x = list(df['표준점수'])

    # 막대 너비
    bar_width = 0.4

    # 각 막대의 위치 계산
    x_indexes_male = [i - bar_width / 2 for i in range(len(x))]
    x_indexes_female = [i + bar_width / 2 for i in range(len(x))]

    #남학생 그래프
    plt.bar(x_indexes_male, df['남성 빈도수'], width=bar_width, label='남학생')

    #여학생 그래프
    plt.bar(x_indexes_female, df['여성 빈도수'], width=bar_width, label='여학생')

    #표준점수 분포에 따라 x축 설정
    plt.xticks(range(len(x)), x, rotation=90)


    plt.title(f'2024학년도 수능 {subject}과목 분포', fontsize=16)
    plt.xlabel('표준점수', fontsize=14)
    plt.ylabel('학생 수', fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return plt.gcf()
