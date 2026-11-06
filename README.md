# 매출이 없어도 기업가치는 만들 수 있다

> 연구실 해설 대시보드 · 회계학(주) + 경영학(보조) · 3편
> 글 · 안상선 ((주)M-Robo 대표)

페르미 추정 → 트래픽 KPI → 추정손익계산서 → VC 방법으로 **매출이 0인 회사의 가치**를 만들고, 배당할인·현금할인·초과이익·Ohlson 모형으로 **기업가치가 무엇으로 결정되는지**를 확인하는 인터랙티브 해설 시리즈입니다. 박사·조수(하루)·초파리 연구원·주판봇이 진행하고, 편마다 라이브 대시보드, 슬라이더 실험, 대결, 생성 AI(코랩) 실습, 확인 퀴즈가 들어 있습니다.

**바로 보기:** `https://adminmrobo.github.io/valuation_without_revenue/`
(저장소 이름을 다르게 만들면 이 주소의 마지막 부분만 바꾸면 됩니다.)

---

## 구성

| 편 | 파일 | 다루는 내용 | 라이브 대시보드 | 코랩 실습 | 대결 |
|---|---|---|---|---|---|
| 목차 | [`index.html`](index.html) | 시리즈 소개, 학습 지도, 실습 모음 | 편별 미리보기 | — | — |
| 1편 | [`01_market_kpi.html`](01_market_kpi.html) | ① 페르미 추정(TAM·SAM·SOM) ② 트래픽 KPI 매출식 | 사례 A 서비스의 하루 | 시장 규모·연도별 매출·레버 민감도 | 매출을 가장 크게 올린 레버 → 주판봇 승 |
| 2편 | [`02_proforma_vc.html`](02_proforma_vc.html) | ③ 추정손익계산서·영업 레버리지 ④ VC 방법(Post/Pre-money) | 36개월 손익 레이스 | 손익표·손익분기 단가·VC 열지도 | 매출 기준 106만 vs 176만 → 조건부 |
| 3편 | [`03_value_models.html`](03_value_models.html) | ⑤ DDM·DCF·RIM ⑥ Ohlson 모형과 부수적 정보 | 세 탱크와 주가 전광판 | 세 모형 동치 확인·Ohlson 회귀 | 첫해 FCF 음수 회사의 가치 → 초파리 승 |

사례 A는 편의점 폐기 직전 신선식품 알림 서비스, 사례 B는 공시 기반 로봇기자를 만드는 투자정보제공 스타트업입니다.

## 폴더

```
.
├── index.html                 시리즈 목차
├── 01_market_kpi.html         1편
├── 02_proforma_vc.html        2편
├── 03_value_models.html       3편
├── colab/                     코랩 실습 참고 코드 (페이지의 프롬프트와 같은 내용을 실행한 코드)
│   ├── practice1_market_kpi.py
│   ├── practice2_proforma_vc.py
│   └── practice3_value_models.py
├── docs/                      제작 문서
│   ├── COVER_PROMPTS_valuation_series.md   표지 그림 생성 지시문 3장
│   ├── IMG_01~03_*.md                      편별 이미지 제작 명세서
│   ├── KG_00_registry_additions_valuation.json   시리즈 등록부 추가분
│   └── cover_status_entry.json             표지 현황 사이트용 항목
├── assets/img/                표지 그림을 받으면 넣을 자리 (지금은 비어 있음)
└── .nojekyll
```

각 HTML은 **파일 하나로 완결**됩니다. 외부 라이브러리 없이 글꼴(Google Fonts)만 불러오고, 캐릭터 그림은 파일 안에 들어 있습니다. 더블클릭으로 열어도 됩니다.

## GitHub Pages로 공개하기

1. GitHub에서 새 저장소를 만든다 (예: `valuation_without_revenue`, Public).
2. 이 폴더의 파일을 모두 올린다. 터미널이라면:
   ```bash
   git init
   git add .
   git commit -m "매출이 없어도 기업가치는 만들 수 있다 — 3편과 목차"
   git branch -M main
   git remote add origin https://github.com/adminmrobo/valuation_without_revenue.git
   git push -u origin main
   ```
3. 저장소 **Settings → Pages**에서 Source를 `Deploy from a branch`, Branch를 `main` / `(root)`로 저장한다.
4. 1~2분 뒤 `https://adminmrobo.github.io/valuation_without_revenue/`에서 목차가 열린다.

## 코랩 실습

1. [colab.research.google.com](https://colab.research.google.com)에서 새 노트북을 연다.
2. 각 편의 **생성 AI(코랩)로 실습하기** 섹션에서 프롬프트를 복사해 생성 AI에 붙여 넣고 코드를 받는다.
3. 실행 결과를 페이지의 **기대 결과**표와 맞춘다. 다르면 `colab/` 폴더의 참고 코드와 비교한다.

| 실습 | 확인할 대표 값 |
|---|---|
| 1 | SOM·SAM·TAM 1,764,692 / 3,960,152 / 8,785,308명, 2020 매출 243,278,840원 |
| 2 | 2022 영업이익 298,533,962원, Post-money 8.85 / 1.35 / 72.69억 원 |
| 3 | DDM = DCF = RIM = 1,731.1, R² 0.437 → 0.749 (가상 표본) |

실습 3은 `statsmodels`가 필요합니다. 코랩에는 기본으로 설치되어 있습니다.

## 남은 일

- [ ] 표지 그림 3장(+목차 표지): `docs/COVER_PROMPTS_valuation_series.md`의 지시문으로 만든 뒤 `assets/img/`에 넣고 각 페이지의 `<!-- lab-cover -->` 자리에 반영
- [ ] 라이선스 정하기 (정하면 이 README와 각 페이지 `page-meta`의 `license`에 기입)
- [ ] 공개 주소가 정해지면 각 페이지 `page-meta`의 `url`에 기입
- [ ] 원 자료 인용 통계·문헌의 원문 확인 (각 편 바닥글과 꾸러미의 "확인 필요" 목록)

## 정확성과 이용 안내

- 사례의 숫자는 강의 자료의 추정·가정값이며, 공식 통계는 원 자료 기준일(2019년)의 값입니다. 실제 사업계획에는 최신 통계로 다시 계산해야 합니다.
- 노란 도장이 찍힌 그림, 라이브 대시보드의 시간대 분포·이벤트, 3편의 예시 회사와 가상 기업 데이터는 설명용 모형입니다.
- 이 시리즈는 교육용이며 **투자 자문이 아닙니다**. 회계 처리·세무 판단은 기준 체계와 기준일을 확인하고 전문가와 상의하세요.

## 출처

- 강의 자료 「매출이 없어도 기업가치는 만들 수 있다 — 페르미 추정 → 트래픽 KPI → 추정손익계산서 → 투자유치」 1부·2부 (2026)
- 원 자료 인용: 과학기술정보통신부 무선통신서비스 통계(2019.08), 인구통계(2019.09), 금융투자협회(2013), 한국거래소(2014)
- Ohlson, J. A. (1995). Earnings, Book Values, and Dividends in Equity Valuation. *Contemporary Accounting Research*.
- Feltham & Ohlson (1995), Preinreich (1938), Lev & Zarowin (1999) 등 — 원 자료의 선행연구 표에서 인용

각 페이지 맨 아래 **온톨로지·서지 꾸러미**에서 개념 지도(JSON-LD, Turtle, CSV)와 참고문헌(BibTeX, RIS, CSL-JSON)을 ZIP으로 내려받을 수 있습니다.
