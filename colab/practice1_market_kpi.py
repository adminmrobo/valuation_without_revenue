import pandas as pd

# 1) 출발 숫자와 비율 (강의 자료: 과기정통부 2019.08, 인구통계 2019.09)
A = 24_069_337                      # SKT 무선 가입자(법인 제외)
df = pd.DataFrame({
    'age':   ['10s', '20s', '30s'],
    'B_age': [0.097, 0.131, 0.137],  # 연령 비중
    'D_seoul': [0.166, 0.214, 0.213],  # 서울 비중
    'E_metro': [0.250, 0.256, 0.244],  # 광역시 비중
})
df['users'] = A * df['B_age']
df['SOM'] = df['users'] * df['D_seoul']
df['SAM'] = df['users'] * (df['D_seoul'] + df['E_metro'])
df['TAM'] = df['users']
print(df[['age', 'SOM', 'SAM', 'TAM']].round(0))
print('SOM / SAM / TAM =', *df[['SOM', 'SAM', 'TAM']].sum().round(0))

# 2) 트래픽 매출식: 사용자 x 접속률 x 클릭 x 단가 x 360일
kpi = {2020: dict(acc=[.30, .35, .30], clk=4, prc=.3),
       2021: dict(acc=[.45, .40, .35], clk=5, prc=.3),
       2022: dict(acc=[.50, .45, .40], clk=5, prc=.5)}
def revenue(year, acc_mul=1, clk_mul=1, prc_mul=1):
    k = kpi[year]
    acc = pd.Series(k['acc']) * acc_mul
    return float((df['SOM'] * acc * k['clk'] * clk_mul * k['prc'] * prc_mul * 360).sum())
for y in kpi:
    print(y, f'{revenue(y):,.0f}')

# 3) 민감도: 레버 하나만 +-20% 바꿨을 때 2020 매출
base = revenue(2020)
rows = []
for name, arg in [('access', 'acc_mul'), ('clicks', 'clk_mul'), ('price', 'prc_mul')]:
    lo, hi = revenue(2020, **{arg: 0.8}), revenue(2020, **{arg: 1.2})
    rows.append((name, lo - base, hi - base))
sens = pd.DataFrame(rows, columns=['lever', '-20%', '+20%'])
print(sens.round(0))

import matplotlib.pyplot as plt
ax = sens.set_index('lever').plot.barh(figsize=(6, 2.6))
ax.set_xlabel('change in 2020 revenue (KRW)')
plt.tight_layout(); plt.savefig('c1.png')
