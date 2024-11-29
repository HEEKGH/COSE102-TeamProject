
import matplotlib.pyplot as plt

def create_graph(df, subject):
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize = (20,6))

    #남학생 그래프
    plt.plot(df['표준점수'], df['남성 빈도수'], label='남학생', linestyle='-', linewidth=2)

    #여학생 그래프
    plt.plot(df['표준점수'], df['여성 빈도수'], label='여학생', linestyle='-', linewidth=2)

    #표준점수 분포에 따라 x축 설정 / 10 단위로 표시
    plt.xticks(range(min(df['표준점수']), max(df['표준점수']) + 1, 10))


    plt.title(f'2024학년도 수능 {subject}과목 분포', fontsize=16)
    plt.xlabel('표준점수', fontsize=14)
    plt.ylabel('학생 수', fontsize=14)
    plt.legend()
    plt.tight_layout()

    return plt.gcf()
