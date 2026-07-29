# =============================================================================
#  08_02  파일 입출력  ―  복습용
# -----------------------------------------------------------------------------
#  배운 것 : open()·모드(r·w·a)·인코딩, read/readlines, with open(자동 닫힘),
#            txt 쓰기, csv.reader / csv.writer
#  ※ 이 파일은 실행하면 예시 파일들을 만들었다가 '맨 끝에서 정리'합니다.
#  사용법  : "→" 결과를 먼저 예상한 뒤 실행해서 맞춰보기
# =============================================================================

import csv
import os

print("========== 1. 파일 열기 ― open()·모드·인코딩 ==========")

# ---------------------------------------------------------------------------
# 형식:  open(파일명, 모드, encoding="utf-8")
#   모드:  r = 읽기 / w = 새로 쓰기(기존 내용 삭제) / a = 이어 쓰기
#   한글이 있으면 encoding="utf-8" 이 안전하다.
#   ★규칙★ 열면(open) 반드시 닫아야(close) 한다 → 그래서 with open을 쓴다(아래)
# ---------------------------------------------------------------------------

# 먼저 읽을 파일을 하나 만들어 두자 (w 모드 = 새로 쓰기)
with open("_demo_log.txt", "w", encoding="utf-8") as f:
    f.write("점검 시작\n")          # \n = 줄바꿈
    f.write("이상 없음\n")

# 옛날 방식 (open → 작업 → close). 닫기를 잊으면 문제가 생긴다.
f = open("_demo_log.txt", "r", encoding="utf-8")
print(f.read())                    # → 점검 시작 / 이상 없음   (전체를 한 문자열로)
f.close()                          # 반드시 닫기!


print("========== 2. ★실무 기본형★ with open ― 자동으로 닫힘 ==========")

# ---------------------------------------------------------------------------
# with open(...) as f:  블록이 끝나면 close()가 자동 → 닫기를 잊을 일이 없다.
# 오류가 나도 안전하게 닫힌다. 앞으로는 항상 이 형태를 쓴다.
# ---------------------------------------------------------------------------

# 읽기: read() 전체 / readlines() 줄 리스트
with open("_demo_log.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)                        # → 점검 시작 / 이상 없음

with open("_demo_log.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)                       # → ['점검 시작\n', '이상 없음\n']   (줄 리스트)


print()
print("========== 3. 파일에 쓰기 ― w 모드 ==========")

# w = 새로 쓰기 (기존 내용을 지우고 처음부터!)
with open("_demo_out.txt", "w", encoding="utf-8") as f:
    f.write("점검 시작\n")
    f.write("이상 없음\n")

with open("_demo_out.txt", "r", encoding="utf-8") as f:
    print(f.read())                # → 점검 시작 / 이상 없음


print()
print("========== 4. 이어 쓰기 ― a 모드 ==========")

# a = 이어 쓰기 (기존 내용 뒤에 추가, 지우지 않음)
with open("_demo_log2.txt", "w", encoding="utf-8") as f:
    f.write("기존 기록\n")

with open("_demo_log2.txt", "a", encoding="utf-8") as f:
    f.write("추가 기록\n")          # 뒤에 이어 붙음

with open("_demo_log2.txt", "r", encoding="utf-8") as f:
    print(f.read())                # → 기존 기록 / 추가 기록
# ★주의★ w로 열면 기존 내용이 사라진다! 이어 붙이려면 반드시 a


print()
print("========== 5. CSV 읽기 ― csv.reader ==========")

# ---------------------------------------------------------------------------
# CSV = 제조 데이터의 기본 형식. 행·열을 쉼표로 구분한 표.
# csv.reader 로 읽으면 각 행이 '리스트'로 나온다.
# ---------------------------------------------------------------------------

# 읽을 CSV를 만들어 두자
with open("_demo_sensor.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["센서", "값"])       # 헤더
    w.writerow(["온도", 95])
    w.writerow(["압력", 88])
    w.writerow(["진동", 92])

with open("_demo_sensor.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)                 # 각 행이 리스트
# → ['센서', '값'] / ['온도', '95'] / ['압력', '88'] / ['진동', '92']
# ★주의★ CSV에서 읽은 숫자는 '글자'다! ('95'는 문자열 → 계산하려면 float())


print()
print("========== 6. CSV 쓰기 ― csv.writer ==========")

with open("_demo_out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["센서", "값"])   # 한 행 = 리스트 하나
    writer.writerow(["온도", 78])
    writer.writerow(["압력", 95])

with open("_demo_out.csv", "r", encoding="utf-8") as f:
    print(f.read())
# → 센서,값 / 온도,78 / 압력,95   (쉼표로 구분되어 저장됨)
# 참고: newline="" 은 CSV 쓸 때 빈 줄이 끼는 것을 막는 관용구


print()
print("========== 7. 종합 : CSV 읽어 조건에 맞는 행만 저장 ==========")

# 90 초과인 센서만 골라 새 CSV로 저장 (읽기 → 필터 → 쓰기 파이프라인)
over = []
with open("_demo_sensor.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                   # 헤더 한 줄 건너뛰기
    for row in reader:
        if float(row[1]) > 90:     # row[1]은 값(글자) → float로 변환해 비교
            over.append(row)

with open("_demo_over.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["센서", "값"])
    for row in over:
        writer.writerow(row)

print("90 초과 센서:", over)        # → [['온도', '95'], ['진동', '92']]


# =============================================================================
#  예시 파일 정리 (이 부분을 지우면 _demo_*.txt/csv 파일들이 남아 직접 열어볼 수 있음)
# =============================================================================
for fn in ["_demo_log.txt", "_demo_out.txt", "_demo_log2.txt",
           "_demo_sensor.csv", "_demo_out.csv", "_demo_over.csv"]:
    if os.path.exists(fn):
        os.remove(fn)


# =============================================================================
#  스스로 확인해보기 (실행 전에 답을 먼저 적어보기)
# -----------------------------------------------------------------------------
#  Q1.  파일 모드 r · w · a 의 차이는?
#       A. r=읽기, w=새로 쓰기(기존 삭제!), a=이어 쓰기(뒤에 추가).
#
#  Q2.  with open(...) as f: 를 쓰는 이유는?
#       A. 블록이 끝나면 자동으로 닫혀서(close), 닫기를 잊거나 오류가 나도 안전.
#
#  Q3.  read() 와 readlines() 의 차이는?
#       A. read()는 전체를 한 문자열로, readlines()는 줄 단위 리스트로.
#
#  Q4.  기존 파일 내용을 유지하며 새 줄을 추가하려면 어떤 모드?
#       A. a (append). w로 열면 기존 내용이 지워진다.
#
#  Q5.  csv.reader로 읽은 "95"로 크기 비교를 하려면?
#       A. float("95")로 숫자 변환. CSV에서 읽은 값은 전부 글자다.
#
#  Q6.  CSV 첫 줄(헤더)을 건너뛰려면?
#       A. next(reader) 를 한 번 호출한 뒤 반복.
# =============================================================================

print()
print("08_02 복습 완료")
