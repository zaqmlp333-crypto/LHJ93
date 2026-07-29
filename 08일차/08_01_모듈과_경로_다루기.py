# =============================================================================
#  08_01  모듈과 경로 다루기  ―  복습용
# -----------------------------------------------------------------------------
#  배운 것 : import 세 방식(import / from import / as),
#            표준 라이브러리(math·random·datetime), os 경로 다루기
#  ※ 이 파일은 실행하면 예시 폴더 _demo_data/ 를 만들었다가 '맨 끝에서 정리'합니다.
#  사용법  : "→" 결과를 먼저 예상한 뒤 실행해서 맞춰보기 (random은 매번 다름)
# =============================================================================

print("========== 1. 모듈 가져오기 ― import 세 방식 ==========")

# ---------------------------------------------------------------------------
# 모듈 = 남이 만들어 둔 '도구 상자'. 가져와 쓰면 바퀴를 다시 만들 필요가 없다.
#
#   ① import 모듈           → 모듈.기능()  으로 사용
#   ② from 모듈 import 기능  → 모듈명 없이 기능()  바로 사용
#   ③ import 모듈 as 별칭    → 긴 이름에 짧은 별명
# ---------------------------------------------------------------------------

import math                        # ① 통째로
print(math.sqrt(16))              # → 4.0    (제곱근)
print(math.ceil(4.2))             # → 5      (올림)

from math import sqrt, ceil        # ② 일부만 → 모듈명 없이
print(sqrt(25), ceil(4.1))        # → 5.0 5

import math as m                   # ③ 별칭
print(m.sqrt(9))                  # → 3.0

# 실무 약속:  import numpy as np / import pandas as pd  (별칭이 관례 — 뒤에서 배움)


print()
print("========== 2. 표준 라이브러리 ― math · random · datetime ==========")

# 파이썬 설치 시 함께 깔리는 검증된 모듈들. import만 하면 바로 쓴다.

import random
import datetime

print(math.pi)                    # → 3.141592653589793
print(random.randint(1, 100))     # → (1~100 사이 매번 다른 값)
print(datetime.datetime.now())    # → (현재 시각, 실행할 때마다 다름)

# 활용: 센서값을 무작위로 만들어 테스트
value = random.randint(50, 100)
print("측정값:", value, "제곱근:", round(math.sqrt(value), 2))


print()
print("========== 3. os ― 경로와 폴더 다루기 ==========")

# ---------------------------------------------------------------------------
# 파일을 다루려면 '어디에 있는지(경로)'를 알아야 한다. os가 폴더·경로를 담당.
#   os.getcwd()            현재 작업 폴더 (절대경로)
#   os.makedirs(경로)       폴더 만들기
#   os.listdir(경로)        폴더 안 파일 목록
#   os.path.join(a, b)     경로 안전하게 잇기 (OS에 맞는 구분자 자동)
#   os.path.exists(경로)    존재 여부 (True/False)
# ---------------------------------------------------------------------------

import os

# 예시 폴더/파일 준비 (학습용 — 맨 끝에서 정리함)
os.makedirs("_demo_data", exist_ok=True)              # 폴더 만들기 (있어도 오류 없음)
for fn in ["sensor.csv", "log.csv", "readme.txt"]:
    with open(os.path.join("_demo_data", fn), "w", encoding="utf-8") as f:
        f.write("예시")

print("현재 폴더:", os.getcwd())                       # → (절대경로 문자열)
print("_demo_data 있나?", os.path.exists("_demo_data"))  # → True


print()
print("========== 4. 폴더 목록 훑고 csv만 골라내기 ==========")

# os.path.join 으로 경로를 안전하게 잇는다 (Windows는 \, Mac/Linux는 / — 자동 처리)
files = os.listdir("_demo_data")
print("전체 파일:", sorted(files))          # → ['log.csv', 'readme.txt', 'sensor.csv']

# csv 파일만 골라내기 (03_03 endswith 복습)
csvs = []
for name in files:
    if name.endswith(".csv"):
        csvs.append(name)
print("CSV 파일:", sorted(csvs))            # → ['log.csv', 'sensor.csv']

# 존재 확인 후 처리
path = os.path.join("_demo_data", "sensor.csv")
if os.path.exists(path):
    print("파일 있음:", path)
else:
    print("파일 없음")


print()
print("========== 5. 종합 : 파일 개수 + 점검 시각 기록 ==========")

files = os.listdir("_demo_data")
now = datetime.datetime.now()
print(f"파일 {len(files)}개, 점검 시각 {now}")   # → 파일 3개, 점검 시각 ...


# =============================================================================
#  예시 폴더 정리 (이 부분을 지우면 _demo_data 폴더가 남아 직접 열어볼 수 있음)
# =============================================================================
import shutil
shutil.rmtree("_demo_data", ignore_errors=True)     # 폴더 통째로 삭제


# =============================================================================
#  스스로 확인해보기 (실행 전에 답을 먼저 적어보기)
# -----------------------------------------------------------------------------
#  Q1.  import 세 방식의 차이는?
#       A. import 모듈(모듈.기능) / from 모듈 import 기능(바로 기능) /
#          import 모듈 as 별칭(짧은 이름).
#
#  Q2.  math.sqrt(16) 과 from math import sqrt 후 sqrt(16) 의 차이는?
#       A. 결과는 같다(4.0). 앞은 모듈명 필요, 뒤는 모듈명 없이 바로 호출.
#
#  Q3.  numpy·pandas 의 관례적 별칭은?
#       A. import numpy as np / import pandas as pd
#
#  Q4.  파일 경로를 "폴더" + "파일명" 으로 안전하게 잇는 방법은?
#       A. os.path.join("폴더", "파일명")  (OS에 맞는 구분자를 자동으로 넣어줌)
#
#  Q5.  파일을 열기 전에 있는지 확인하려면?
#       A. os.path.exists(경로)  → True/False
# =============================================================================

print()
print("08_01 복습 완료")
