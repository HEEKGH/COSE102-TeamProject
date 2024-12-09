
import matplotlib.pyplot as plt

def create_graph(df, subject, year):
    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize = (20,6))

    plt.hist( #히스토그램 생성
        [df['표준점수'], df['표준점수']],  # 표준점수를 기준으로 두 데이터를 그룹화
        bins=range(min(df['표준점수']), max(df['표준점수']) + 1, 5),  # 간격 5로 설정
        weights=[df['남성 빈도수'], df['여성 빈도수']],
        label=['남학생', '여학생'],
        alpha=0.7,
        edgecolor='black',
        histtype='bar',
    )

    plt.title(f'{year}학년도 수능 {subject}과목 분포', fontsize=16)
    plt.xlabel('표준점수', fontsize=14)
    plt.ylabel('학생 수', fontsize=14)
    plt.xticks(range(min(df['표준점수']), max(df['표준점수']) + 1, 5)) #x축 눈금을 5단위로 표시
    plt.legend()
    plt.tight_layout()
    plt.show()

    return plt.gcf()
