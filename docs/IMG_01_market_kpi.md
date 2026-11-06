# 1편 「시장을 세고, 트래픽을 매출로」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 01_market_kpi.html (시리즈 「매출이 없어도 기업가치는 만들 수 있다」 1/3) |
| 분야 / 주 앵커 | 4 회계학(주) + 5 경영학(보조) / D 생활: 밤의 연구실 옥상 묘목 밭 |
| 대결 | 2021→2022 매출을 가장 크게 끌어올린 레버 → 결과 **R** (접속률 +0.48억 vs 단가 +2.48억) |
| 새로 그릴 그림 | P1 1장(표지) · P2 3장 |
| 재사용 | 캐릭터 팩 1.3 표정 22종 (96px, 페이지에 base64로 들어 있음) |
| 그림이 없을 때 | 픽셀 묘목 캔버스와 표정 그림으로 이미 완성 상태 |

장소·고정 외형·금지 구절은 캐릭터 팩 18-3·18-4와 같다. 생물 앵커가 아니므로 현미경·해부 소품을 넣지 않고, 장부는 비유가 아닌 배경 소품으로만 둔다(회계 팩 P3). 실제 회사·통신사 로고와 사례 B의 회사 이름은 그리지 않는다.

## 필요한 그림

| 키 | 판 | 크기 | 상태 | 우선 | 내용 |
|---|---|---|---|---|---|
| cover_01 | L | 1920×1080 | 새로 (COVER_PROMPTS_valuation_series.md) | P1 | 맨 위 글 표지 |
| cut_01_kpi | G | 960×540 | 새로 | P2 | ② KPI: 100개의 작은 묘목 중 일부만 빛나고(접속), 빛나는 묘목마다 금빛 반짝임(클릭)이 맺힌다 |
| sc_01_outro | E | 1200×800 | 새로 | P2 | 아웃트로(결과 R): 저울 오른쪽 단가 카드 더미가 더 높고, 주판봇이 두 팔을 들고 초파리는 커피를 든 채 인정 |
| thumb_01 | I | 600×400 | cover_01 3:2 자르기 | P2 | 목차 카드 |
| bg_01 | F | 1920×720 | cover_01 8:3 자르기 | P3 | 히어로 배경 |
| 표정 | A~D | 96 | 재사용 | — | 히어로·말풍선·대결 (대결 후 표정은 캐릭터 팩 5-8의 R 행) |

## 새로 그릴 그림 프롬프트

### `cut_01_kpi`
- 대체 글: 조수가 일부만 빛나는 작은 묘목 100그루와 그 위의 금빛 반짝임을 세는 컷
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 16:9 illustration panel, a rooftop garden of the same night laboratory, rows of young saplings in wooden planters with no fruit yet, a few tiny golden buds, purple lab light spilling from the rooftop door, a ten by ten grid of tiny potted saplings where only some glow (visitors) and each glowing sapling has a few golden sparkles around it (clicks), girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, crouching and counting the glowing saplings on a blank clipboard, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### `sc_01_outro`
- 대체 글: 밤의 연구실 묘목 밭에서 저울 오른쪽 카드 더미가 더 높은 것을 네 캐릭터가 바라보는 장면
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a rooftop garden of the same night laboratory, rows of young saplings in wooden planters with no fruit yet, a few tiny golden buds, purple lab light spilling from the rooftop door, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center behind a brass balance scale whose right pan holds a taller pile of blank cards, pointing at it; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, raising both arms happily; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, holding a coffee cup with a small accepting nod; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, proud smile holding a clipboard, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 넘겨받은 뒤
`build_character_pack.py --ingest ./받은그림 --plates cut_01_kpi=G,sc_01_outro=E --out received_01` → 나온 조각을 페이지 `SPRITE`에 넣고, 아웃트로 캔버스 `#cOut` 자리를 `<img data-img="sc_01_outro">`로 바꾼다. 페이지 그림 합계 600 KB 이하.

## 체크리스트 (SKILL 18-13)
- [x] HTML의 `data-img` 키와 명세서 키 일치 · [x] 결과 전 그림에 승패 암시 없음 · [x] 고정 외형·금지 구절 포함 · [x] 그림 안 글자·실존 로고 없음 · [x] 장면마다 대체 글

## 매니페스트
```json
{
 "page": "01_market_kpi",
 "anchor": "D:rooftop-sapling-garden",
 "domain": [
  "acct",
  "biz"
 ],
 "duel": {
  "result": "R"
 },
 "images": [
  {
   "key": "cover_01",
   "plate": "L",
   "size": [
    1920,
    1080
   ],
   "status": "new",
   "priority": "P1",
   "slot": "cover",
   "fallback": "css-pixel-four",
   "alt": "밤의 연구실 옥상 묘목 밭에서 네 캐릭터가 줄자와 돋보기로 묘목 줄을 재는 표지"
  },
  {
   "key": "cut_01_kpi",
   "plate": "G",
   "size": [
    960,
    540
   ],
   "status": "new",
   "priority": "P2",
   "alt": "조수가 일부만 빛나는 작은 묘목 100그루와 그 위의 금빛 반짝임을 세는 컷"
  },
  {
   "key": "sc_01_outro",
   "plate": "E",
   "size": [
    1200,
    800
   ],
   "status": "new",
   "priority": "P2",
   "alt": "밤의 연구실 묘목 밭에서 저울 오른쪽 카드 더미가 더 높은 것을 네 캐릭터가 바라보는 장면"
  },
  {
   "key": "thumb_01",
   "plate": "I",
   "size": [
    600,
    400
   ],
   "status": "new (cover crop)",
   "priority": "P2"
  }
 ]
}
```
