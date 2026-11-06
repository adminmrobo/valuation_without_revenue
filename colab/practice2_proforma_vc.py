import pandas as pd, numpy as np

# 1) 사례 A 추정손익계산서 (강의 자료 가정)
rev = {2020: 243_278_840, 2021: 372_673_704, 2022: 700_533_962}
cost = pd.DataFrame({
    'labor':     [120e6, 150e6, 180e6],   # 인건비 (1인 3천만 x 4/5/6명)
    'marketing': [100e6, 150e6, 200e6],
    'rent':      [12e6] * 3,
    'utility':   [4e6] * 3,
    'pc':        [6e6] * 3,
}, index=[2020, 2021, 2022])
pl = pd.DataFrame({'revenue': pd.Series(rev)})
pl['cost'] = cost.sum(axis=1)
pl['op_profit'] = pl['revenue'] - pl['cost']
pl['margin'] = pl['op_profit'] / pl['revenue']
print(pl.round(3))

# 2) 영업 레버리지와 손익분기 광고 단가
lift = pl.loc[2020, 'revenue'] * 1.10 - pl.loc[2020, 'cost']
print(f'lever +10% -> 2020 op profit {lift:,.0f} ({lift / pl.loc[2020, "op_profit"]:.1f}x)')
print(f'break-even ad price {0.3 * pl.loc[2020, "cost"] / pl.loc[2020, "revenue"]:.3f} KRW')

# 3) VC 방법
def vc(profit, multiple=10, target=0.5, years=3, invest=3e8):
    post = profit * multiple / (1 + target) ** years
    return dict(post=post, pre=post - invest, stake=invest / post)
for name, p, n in [('A (1.76M users)', 298_533_962, 3), ('A (1.06M target)', 45_681_725, 3),
                   ('B (info startup)', 3_680e6, 4)]:
    r = vc(p, years=n)
    print(f"{name:18s} post {r['post']/1e8:6.2f} | pre {r['pre']/1e8:6.2f} | stake {r['stake']:.1%}")

# 4) 민감도 표: 배수 x 목표수익률 -> 사례 A Post-money (억 원)
mults, targets = [6, 8, 10, 12, 15], [0.3, 0.4, 0.5, 0.6]
grid = pd.DataFrame([[vc(298_533_962, m, t)['post'] / 1e8 for t in targets] for m in mults],
                    index=[f'x{m}' for m in mults], columns=[f'{t:.0%}' for t in targets])
print(grid.round(2))

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(5, 3.2))
im = ax.imshow(grid.values, cmap='viridis')
ax.set_xticks(range(len(targets)), grid.columns); ax.set_yticks(range(len(mults)), grid.index)
ax.set_xlabel('target return'); ax.set_ylabel('multiple'); fig.colorbar(im, label='post-money (100M KRW)')
plt.tight_layout(); plt.savefig('c2.png')
