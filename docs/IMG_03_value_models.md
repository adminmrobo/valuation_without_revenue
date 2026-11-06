# 3편 「기업가치는 무엇으로 결정되는가」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 03_value_models.html (시리즈 「매출이 없어도 기업가치는 만들 수 있다」 3/3) |
| 분야 / 주 앵커 | 4 회계학(주) + 5 경영학(보조) / D 생활: 밤의 연구실 옥상 묘목 밭 |
| 대결 | 첫해 FCF −640인 회사의 가치 → 결과 **F** (가치 1,731 > 장부가치 1,000) |
| 새로 그릴 그림 | P1 1장(표지) · P2 3장 |
| 재사용 | 캐릭터 팩 1.3 표정 22종 (96px, 페이지에 base64로 들어 있음) |
| 그림이 없을 때 | 픽셀 묘목 캔버스와 표정 그림으로 이미 완성 상태 |

장소·고정 외형·금지 구절은 캐릭터 팩 18-3·18-4와 같다. 생물 앵커가 아니므로 현미경·해부 소품을 넣지 않고, 장부는 비유가 아닌 배경 소품으로만 둔다(회계 팩 P3). 실제 회사·통신사 로고와 사례 B의 회사 이름은 그리지 않는다.

## 필요한 그림

| 키 | 판 | 크기 | 상태 | 우선 | 내용 |
|---|---|---|---|---|---|
| cover_03 | L | 1920×1080 | 새로 (COVER_PROMPTS_valuation_series.md) | P1 | 맨 위 글 표지 |
| cut_03_ohlson | G | 960×540 | 새로 | P2 | ⑥ 부수적 정보: 같은 과일나무 옆에 장부에 없는 것 — 새 품종 씨앗 상자, 반짝이는 간판틀(글자 없음) — 을 주판봇이 놀라 바라본다 |
| sc_03_outro | E | 1200×800 | 새로 | P2 | 아웃트로(결과 F): 초파리 팔짱, 주판봇 한숨, 세 더미와 장부가치 팻말 |
| thumb_03 | I | 600×400 | cover_03 3:2 자르기 | P2 | 목차 카드 |
| bg_03 | F | 1920×720 | cover_03 8:3 자르기 | P3 | 히어로 배경 |
| 표정 | A~D | 96 | 재사용 | — | 히어로·말풍선·대결 (대결 후 표정은 캐릭터 팩 5-8의 F 행) |

## 새로 그릴 그림 프롬프트

### `cut_03_ohlson`
- 대체 글: 과일나무 옆 새 씨앗 상자와 빈 간판틀을 주판봇이 놀라 바라보는 컷
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 16:9 illustration panel, a rooftop garden of the same night laboratory, rows of young saplings in wooden planters with no fruit yet, a few tiny golden buds, purple lab light spilling from the rooftop door, beside a grown fruit tree stand a small crate of new seed packets with blank labels and an empty glowing signboard frame, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, facing left, surprised round eyes leaning back, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### `sc_03_outro`
- 대체 글: 밤의 연구실 과수원에서 네 캐릭터가 같은 높이의 세 더미와 낮은 장부가치 팻말을 바라보는 장면
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a rooftop garden of the same night laboratory, rows of young saplings in wooden planters with no fruit yet, a few tiny golden buds, purple lab light spilling from the rooftop door, a grown fruit tree with three equal-height piles beside it and a short blank wooden sign marking a lower level, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, arms crossed with confident eyes; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, half-closed eyes with a small sigh bubble, arms down; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the center pointing at the piles; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, proud smile holding a clipboard, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 넘겨받은 뒤
`build_character_pack.py --ingest ./받은그림 --plates cut_03_ohlson=G,sc_03_outro=E --out received_03` → 나온 조각을 페이지 `SPRITE`에 넣고, 아웃트로 캔버스 `#cOut` 자리를 `<img data-img="sc_03_outro">`로 바꾼다. 페이지 그림 합계 600 KB 이하.

## 체크리스트 (SKILL 18-13)
- [x] HTML의 `data-img` 키와 명세서 키 일치 · [x] 결과 전 그림에 승패 암시 없음 · [x] 고정 외형·금지 구절 포함 · [x] 그림 안 글자·실존 로고 없음 · [x] 장면마다 대체 글

## 매니페스트
```json
{
 "page": "03_value_models",
 "anchor": "D:rooftop-sapling-garden",
 "domain": [
  "acct",
  "biz"
 ],
 "duel": {
  "result": "F"
 },
 "images": [
  {
   "key": "cover_03",
   "plate": "L",
   "size": [
    1920,
    1080
   ],
   "status": "new",
   "priority": "P1",
   "slot": "cover",
   "fallback": "css-pixel-four",
   "alt": "밤의 연구실 옥상 과수원에서 네 캐릭터가 한 그루 과일나무 옆 바구니·수레·땅 세 더미의 높이를 비교하는 표지"
  },
  {
   "key": "cut_03_ohlson",
   "plate": "G",
   "size": [
    960,
    540
   ],
   "status": "new",
   "priority": "P2",
   "alt": "과일나무 옆 새 씨앗 상자와 빈 간판틀을 주판봇이 놀라 바라보는 컷"
  },
  {
   "key": "sc_03_outro",
   "plate": "E",
   "size": [
    1200,
    800
   ],
   "status": "new",
   "priority": "P2",
   "alt": "밤의 연구실 과수원에서 네 캐릭터가 같은 높이의 세 더미와 낮은 장부가치 팻말을 바라보는 장면"
  },
  {
   "key": "thumb_03",
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
