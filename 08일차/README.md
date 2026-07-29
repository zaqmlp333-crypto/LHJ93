# 8일차 — 모듈과 파일 입출력 (08장)

설비 고장을 예측하는 AI 데이터 분석 — **바깥 세계와 연결**하는 날입니다.
남이 만든 도구(모듈)를 가져오고, 데이터를 파일로 읽고 씁니다. **CSV 처리**는 이후 pandas의 바탕이 됩니다.

---

## 1. 파일 목록

| 파일 | 배운 내용 | 강의자료 |
|---|---|---|
| `08_01_모듈과_경로_다루기.py` | `import` 세 방식, math·random·datetime, os 경로 | 08_01 |
| `08_02_파일_입출력.py` | `open`·모드(r/w/a), `with open`, csv.reader/writer | 08_02 |
| `99_연습문제.py` | **직접 풀어보는 문제 11개 + 도전** (출력 예측 3개) | 전체 |
| `99_연습문제_정답.py` | 정답 + 해설 | 전체 |

> 복습·연습 파일은 실행 중 임시 파일(`_demo_*`, `_q_*`)을 만들었다가 **맨 끝에서 스스로 정리**합니다. git에 남지 않습니다.

---

## 2. 치트시트

### 모듈 (08_01)

```python
import math                 # 모듈.기능()
math.sqrt(16)               # 4.0

from math import sqrt       # 모듈명 없이 바로
sqrt(16)                    # 4.0

import pandas as pd         # 별칭 (관례: numpy→np, pandas→pd)
```

| 모듈 | 용도 |
|---|---|
| `math` | `sqrt` `ceil` `floor` `pi` |
| `random` | `randint(1, 100)` 무작위 정수 |
| `datetime` | `datetime.datetime.now()` 현재 시각 |
| `os` | `getcwd` `listdir` `path.join` `path.exists` `makedirs` |

### 파일 입출력 (08_02)

```python
# ★실무 기본형★ with open (자동으로 닫힘)
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()             # 전체 한 문자열
    # lines = f.readlines()     # 줄 리스트

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("한 줄\n")           # w=새로쓰기, a=이어쓰기

# CSV
import csv
with open("s.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                # 헤더 건너뛰기
    for row in reader:          # 각 행이 리스트
        float(row[1])           # ★읽은 값은 글자! 변환 필요★

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["센서", "값"])   # 한 행 = 리스트
```

### 파일 모드

| 모드 | 뜻 | 주의 |
|---|---|---|
| `r` | 읽기 | 파일이 없으면 오류 |
| `w` | 새로 쓰기 | **기존 내용을 지우고** 처음부터! |
| `a` | 이어 쓰기 | 기존 뒤에 추가 |

---

## 3. 오늘의 함정 모음

| 함정 | 증상 | 예방 |
|---|---|---|
| `w`로 열어 기존 내용 사라짐 | 데이터 날아감 | 이어 붙일 땐 `a` 모드 |
| CSV 값을 그대로 비교 | `"95" > 90`이 이상하게 동작 | `float(row[1])`로 변환 |
| CSV 헤더까지 처리 | 첫 줄이 데이터로 섞임 | `next(reader)`로 건너뛰기 |
| `open` 후 `close` 안 함 | 파일이 안 닫힘 | `with open`을 쓰면 자동 |
| 한글 파일에 인코딩 누락 | 글자 깨짐 | `encoding="utf-8"` |
| 경로를 `+`로 이음 | OS별 구분자 문제 | `os.path.join` |

---

## 4. 스스로 점검

- [ ] `import` 세 방식의 차이를 안다
- [ ] `numpy→np`, `pandas→pd` 관례를 안다
- [ ] `os.path.join`으로 경로를 안전하게 만들 수 있다
- [ ] `with open`을 쓰는 이유(자동 닫힘)를 안다
- [ ] `r`/`w`/`a` 모드의 차이, 특히 `w`가 기존 내용을 지운다는 것을 안다
- [ ] `csv.reader`로 읽은 값이 글자라서 변환이 필요함을 안다
- [ ] `next(reader)`로 헤더를 건너뛸 수 있다
- [ ] CSV를 읽어 조건에 맞는 행만 새 파일로 저장할 수 있다
