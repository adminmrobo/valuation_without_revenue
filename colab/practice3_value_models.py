import numpy as np, pandas as pd

# 1) 예시 회사 (부채 0, FCF를 모두 배당, 모자라면 증자) — 세 모형 비교
def three_models(r=0.10, I1=800, C=400, bv0=1000):
    A, rows = [bv0], []
    Cs = [0.4 * C, 0.7 * C, 0.9 * C, C, C]
    Is = [I1, 100, 100, 100, 100]
    for t in range(5):
        dep = 0.1 * A[t]                        # 감가상각 = 기초 자산의 10%
        X = Cs[t] - dep                         # 회계이익
        A.append(A[t] + Is[t] - dep)            # 장부가치 (깨끗한 잉여 관계)
        rows.append(dict(year=t + 1, C=Cs[t], I=Is[t], X=X, BV=A[t + 1],
                         FCF=Cs[t] - Is[t], RI=X - r * A[t]))
    X6 = C - 0.1 * A[5]                         # 6년 이후: 투자 = 감가상각
    df = pd.DataFrame(rows)
    disc = (1 + r) ** df['year']
    tv_fcf = X6 / r / (1 + r) ** 5
    tv_ri = (X6 - r * A[5]) / r / (1 + r) ** 5
    ddm = (df['FCF'] / disc).sum() + tv_fcf     # 배당 = FCF
    dcf = ddm                                   # 순재무부채 0
    rim = bv0 + (df['RI'] / disc).sum() + tv_ri
    return df, ddm, dcf, rim, tv_fcf / dcf, tv_ri / rim
df, ddm, dcf, rim, w_dcf, w_rim = three_models()
print(df.round(1))
print(f'DDM {ddm:,.1f} | DCF {dcf:,.1f} | RIM {rim:,.1f}')
print(f'terminal-value share: DCF {w_dcf:.0%}, RIM {w_rim:.0%}')

# 2) 축약 Ohlson 모형 + 부수적 정보 (가상 표본 80곳, 시드 고정)
rng = np.random.default_rng(22)
n = 80
bps = rng.uniform(5000, 25000, n)                 # 주당 순자산
xa = 300 + rng.normal(0, 600, n)                  # 주당 초과이익
rnd = rng.uniform(0, 2000, n)                     # 주당 연구개발비 (부수적 정보)
price = 1500 + 0.5 * bps + 3 * xa + 5 * rnd + rng.normal(0, 2500, n)
data = pd.DataFrame(dict(price=price, xa=xa, bps=bps, rnd=rnd))

import statsmodels.formula.api as smf
m1 = smf.ols('price ~ xa + bps', data).fit()          # 식 2-6
m2 = smf.ols('price ~ xa + bps + rnd', data).fit()    # 식 3-1
print(m1.params.round(2).to_dict(), 'R2 =', round(m1.rsquared, 3))
print(m2.params.round(2).to_dict(), 'R2 =', round(m2.rsquared, 3))
