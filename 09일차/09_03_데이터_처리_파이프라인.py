# =============================================================================
#  09_03  데이터 처리 파이프라인  ―  복습용
# -----------------------------------------------------------------------------
#  배운 것 : 지금까지 배운 문법(파일·딕셔너리·함수·예외)을 모아
#            5단계 파이프라인 완성 (읽기 → 분류 → 통계 → 방어 → 저장)
#  ※ 이 파일은 실행 중 임시 CSV/리포트를 만들었다가 맨 끝에서 정리합니다.
#  사용법  : 각 단계가 앞 단계의 결과를 어떻게 이어받는지 흐름을 따라가기
# =============================================================================

import csv
import os

# 데모용 센서 CSV 생성 (설비, 온도, 상태) — ERR·999 같은 불량이 일부러 섞여 있음
with open("_sensor.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["설비", "온도", "상태"])
    for row in [["M01", "70", "normal"], ["M01", "72", "normal"],
                ["M02", "ERR", "warning"], ["M02", "999", "warning"],
                ["M03", "65", "normal"], ["M01", "68", "normal"]]:
        w.writerow(row)


print("========== 1단계: 읽기 (파일 없을 때 대비) ==========")

# ---------------------------------------------------------------------------
# 파일이 없어도 프로그램이 죽지 않도록 FileNotFoundError를 잡고 빈 결과 반환.
# (08장 파일 + 09장 예외 결합)
# ---------------------------------------------------------------------------

def read_csv(name):
    try:
        with open(name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)          # 첫 줄 = 헤더
            rows = list(reader)            # 나머지 = 데이터
        return header, rows
    except FileNotFoundError:
        print("파일 없음:", name)
        return [], []                      # 빈 결과 (흐름이 안 끊김)

header, rows = read_csv("_sensor.csv")
print("데이터 행:", len(rows))             # → 데이터 행: 6


print()
print("========== 2단계: 분류 (설비별 딕셔너리) ==========")

# ---------------------------------------------------------------------------
# 설비 이름을 키로, 그 설비의 행들을 리스트로 모은다.
# 처음 보는 키는 빈 리스트를 먼저 만들어야 KeyError가 안 난다. (06장 딕셔너리)
# ---------------------------------------------------------------------------

by_machine = {}
for row in rows:
    m = row[0]                             # 설비 이름
    if m not in by_machine:                # 처음 보는 설비면
        by_machine[m] = []                 # 빈 리스트 먼저
    by_machine[m].append(row)
print("설비 수:", len(by_machine))         # → 설비 수: 3


print()
print("========== 3단계: 통계 함수 (0 나누기 방지) ==========")

# 값이 없으면 None을 돌려줘 0으로 나누는 사고를 막는다 (07장 함수 + 방어)
def calc_mean(values):
    if not values:                         # 빈 리스트면
        return None
    return sum(values) / len(values)


print("========== 4단계: 방어 (불량 거르기 + 범위 밖 raise) ==========")

# ---------------------------------------------------------------------------
# try로 숫자 변환 실패(ERR)를 거르고, raise로 범위 밖(999)을 차단한다.
# 불량 줄은 번호와 이유를 기록해 나중에 확인할 수 있게 한다.
# ---------------------------------------------------------------------------

def defend(rows, lo=-50, hi=200):
    valid = []
    bad = []
    for i, row in enumerate(rows):
        try:
            v = float(row[1])              # "ERR"이면 ValueError
            if v < lo or v > hi:
                raise ValueError("범위 밖")  # 999 같은 값 차단
            valid.append(v)
        except ValueError as e:
            bad.append((i, str(e)))        # 불량 줄 번호 + 이유
    return valid, bad

valid, bad = defend(rows)
print("정상:", len(valid), "불량:", len(bad))   # → 정상: 4 불량: 2
mean = calc_mean(valid)
print("평균:", round(mean, 1))             # → 평균: 68.8


print()
print("========== 5단계: 저장 (리포트를 파일로) ==========")

# 리포트 줄들을 리스트에 모아 한 번에 파일로 저장 (join으로 줄 연결)
lines = []
lines.append("=== 센서 데이터 분석 리포트 ===")
lines.append(f"전체 {len(rows)}행 · 정상 {len(valid)}개 · 불량 {len(bad)}개")
lines.append("-" * 30)
lines.append(f"온도 평균 — {round(mean, 1)}도")

with open("_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("리포트 저장 완료")

# 저장한 리포트를 다시 읽어 확인
with open("_report.txt", "r", encoding="utf-8") as f:
    print(f.read())


# =============================================================================
#  파이프라인 정리
# -----------------------------------------------------------------------------
#   1단계 읽기  : 파일 → 헤더+행 (FileNotFoundError 방어)
#   2단계 분류  : 행 → 설비별 딕셔너리
#   3단계 통계  : 함수로 평균 (0 나누기 방지)
#   4단계 방어  : try로 불량 거르고 raise로 범위 밖 차단
#   5단계 저장  : 리포트를 파일로
#
#   → 이것이 08~09장까지 배운 '파일·딕셔너리·함수·예외'의 결합.
#     10장부터 배울 numpy·pandas가 이 과정을 훨씬 짧게 만들어 준다.
# =============================================================================

# 임시 파일 정리
for fn in ["_sensor.csv", "_report.txt"]:
    if os.path.exists(fn):
        os.remove(fn)

print()
print("09_03 복습 완료")
