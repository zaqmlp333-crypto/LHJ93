# =============================================================================
#  8일차 연습문제 ― 정답  (08장 모듈과 파일 입출력)
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
# =============================================================================

import os
import csv


print("[1]")
import math
print(math.sqrt(100))              # → 10.0
print(math.ceil(7.1))              # → 8


print("[2]")
from math import sqrt, floor
print(sqrt(144))                   # → 12.0   (모듈명 없이)
print(floor(4.9))                  # → 4      (내림)


print("[3]")
import random
print(random.randint(1, 6))        # → 1~6 사이 (매번 다름)


print("[4]")
path = os.path.join("data", "temp.csv")
print(path)                        # → data\temp.csv (윈도우) 또는 data/temp.csv


print("[5]")
files = ["a.csv", "b.txt", "c.csv", "d.log"]
count = 0
for name in files:
    if name.endswith(".csv"):
        count += 1
print(count)                       # → 2   (a.csv, c.csv)


print("[6]")
with open("_q_memo.txt", "w", encoding="utf-8") as f:
    f.write("오늘 점검 완료\n")
    f.write("특이사항 없음\n")
with open("_q_memo.txt", "r", encoding="utf-8") as f:
    print(f.read())                # → 오늘 점검 완료 / 특이사항 없음


print("[7]")
with open("_q_test.txt", "w", encoding="utf-8") as f:
    f.write("첫 번째\n")
with open("_q_test.txt", "w", encoding="utf-8") as f:   # w는 기존 내용 삭제!
    f.write("두 번째\n")
with open("_q_test.txt", "r", encoding="utf-8") as f:
    print(f.read())                # → 두 번째   (첫 번째는 사라짐!)
# w 모드로 다시 열면 기존 내용이 지워진다. 이어 붙이려면 a 모드.


print("[8]")
with open("_q_log.txt", "w", encoding="utf-8") as f:
    f.write("1차 점검\n")
with open("_q_log.txt", "a", encoding="utf-8") as f:    # a = 이어 쓰기
    f.write("2차 점검\n")
with open("_q_log.txt", "r", encoding="utf-8") as f:
    print(f.read())                # → 1차 점검 / 2차 점검


print("[9]")
with open("_q_sensor.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["센서", "값"])
    w.writerow(["온도", 91])
    w.writerow(["압력", 85])
    w.writerow(["진동", 93])
with open("_q_sensor.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# → ['센서', '값'] / ['온도', '91'] / ['압력', '85'] / ['진동', '93']


print("[10]")
with open("_q_num.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["값", 50])
with open("_q_num.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row[1])              # → 50
        print(type(row[1]))        # → <class 'str'>   (숫자를 넣었어도 읽으면 글자!)
# CSV에서 읽은 값은 항상 문자열. 계산하려면 int()/float()로 변환.


print("[11]")
result = []
with open("_q_sensor.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                   # 헤더 건너뛰기
    for row in reader:
        if float(row[1]) > 90:     # 값(글자)을 float로 변환해 비교
            result.append(row[0])  # 이름만 담기
print(result)                      # → ['온도', '진동']   (91, 93)


print()
print("========== [도전] 측정 로그 저장과 분석 ==========")

sensors = [("온도", 95), ("압력", 88), ("진동", 92), ("유량", 60)]

# (1) 판정을 붙여 CSV로 저장
with open("_q_report.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["센서", "값", "판정"])
    for name, value in sensors:            # 튜플 리스트 언패킹
        if value > 90:
            status = "경고"
        else:
            status = "정상"
        writer.writerow([name, value, status])
print("저장 완료")

# (2) 다시 읽어 경고 개수 세기
warning = 0
with open("_q_report.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                           # 헤더 건너뛰기
    for row in reader:
        if row[2] == "경고":               # row[2] = 판정
            warning += 1
print("경고 센서 수:", warning)            # → 경고 센서 수: 2   (온도 95, 진동 92)
# [파일 쓰기 + 조건 판정 + 파일 읽기 + 카운트 = 데이터 처리 파이프라인]


# =============================================================================
#  연습 파일 정리
# =============================================================================
for fn in ["_q_memo.txt", "_q_test.txt", "_q_log.txt", "_q_sensor.csv",
           "_q_num.csv", "_q_report.csv"]:
    if os.path.exists(fn):
        os.remove(fn)

print()
print("정답 확인 완료 - 틀린 문제는 복습 파일을 다시 보세요")
