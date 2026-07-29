# =============================================================================
#  09_04  종합 통합과 응용  ―  복습용
# -----------------------------------------------------------------------------
#  배운 것 : 5단계를 하나의 함수로 통합(파일명 → 결과 딕셔너리),
#            None 분기 처리, 인자만 바꿔 재사용, 주의 설비 탐지
#  ※ 이 파일은 실행 중 임시 CSV/로그를 만들었다가 맨 끝에서 정리합니다.
#  사용법  : 하나의 함수가 어떻게 재사용되는지에 주목하기
# =============================================================================

import csv
import os

# 데모용 CSV 생성 (설비, 온도, 압력)
def make_csv(name, rows):
    with open(name, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["설비", "온도", "압력"])
        for r in rows:
            w.writerow(r)

make_csv("_a.csv", [["M01", "70", "2.1"], ["M01", "72", "2.3"],
                    ["M02", "999", "2.0"], ["M02", "74", "2.2"],
                    ["M03", "66", "1.9"]])


print("========== 1. 통합 함수 ― 파일명만 넣으면 결과 딕셔너리 ==========")

# ---------------------------------------------------------------------------
# 09_03의 5단계를 하나의 함수로 묶었다.
# ★핵심★ col_idx·lo·hi를 '인자'로 빼두면 같은 함수로 온도·압력·진동을 모두 분석!
#   · 파일이 없으면 None 반환 (흐름이 안 끊김)
#   · 결과는 딕셔너리로 (total·valid·mean·max·min)
# ---------------------------------------------------------------------------

def analyze(name, col_idx=1, lo=-50, hi=200):
    try:
        with open(name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)                   # 헤더 건너뛰기
            rows = list(reader)
    except FileNotFoundError:
        print("파일 없음:", name)
        return None                        # 파일 없으면 None

    valid = []
    for row in rows:
        try:
            v = float(row[col_idx])
            if v < lo or v > hi:
                raise ValueError("범위 밖")
            valid.append(v)
        except ValueError:
            continue                       # 불량은 건너뜀

    result = {"total": len(rows), "valid": len(valid)}
    if valid:                              # 정상 값이 있을 때만 통계 추가
        result["mean"] = round(sum(valid) / len(valid), 1)
        result["max"] = max(valid)
        result["min"] = min(valid)
    return result

print(analyze("_a.csv"))
# → {'total': 5, 'valid': 4, 'mean': 70.5, 'max': 74.0, 'min': 66.0}
#   999는 범위 밖이라 제외 → 정상은 70,72,74,66


print()
print("========== 2. None 분기 처리 ― 여러 파일 차례로 ==========")

# 없는 파일은 None을 돌려주므로, if로 걸러 안전하게 처리
for name in ["_a.csv", "_없는파일.csv"]:
    result = analyze(name)
    if result:                             # None(없는 파일)이면 건너뜀
        print(name, "→ 정상", result["valid"], "개")
# → _a.csv → 정상 4 개
# → 파일 없음: _없는파일.csv
#   (_a.csv를 먼저 처리해 정상 출력, 그다음 없는 파일에서 "파일 없음")


print()
print("========== 3. ★재사용★ 인자만 바꿔 압력 분석 ==========")

# 같은 함수인데 col_idx=2(압력 칸), 범위만 바꾸면 압력 분석이 된다!
print("온도:", analyze("_a.csv"))                          # 기본 (온도, 1번 칸)
print("압력:", analyze("_a.csv", col_idx=2, lo=1.0, hi=3.0))  # 압력, 2번 칸
# → 압력: {'total': 5, 'valid': 5, 'mean': 2.1, 'max': 2.3, 'min': 1.9}
# 함수 하나로 온도든 압력이든 — 인자를 빼둔 설계의 힘 (07_03 기본값 인자)


print()
print("========== 4. 로그 남기기 ― 문제를 파일에 기록 ==========")

# 화면이 아니라 파일에 기록하면 나중에 다시 확인할 수 있다
with open("_log.txt", "w", encoding="utf-8") as f:
    f.write("[분석 완료] 통합 함수 실행\n")
print("로그 기록 완료")


print()
print("========== 5. 기능 확장 ― 주의 설비 탐지 ==========")

# ---------------------------------------------------------------------------
# 설비별로 온도를 모아 평균을 내고, 기준을 넘는 '주의 설비'만 골라낸다.
# (09_03의 설비별 분류 + 통계 + 조건 필터를 결합)
# setdefault(키, 기본값): 키가 없으면 기본값으로 만들고, 있으면 그대로 → 빈 리스트 준비를 한 줄로
# ---------------------------------------------------------------------------

def find_risky(name, threshold=70):
    by_machine = {}
    with open(name, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                v = float(row[1])
            except ValueError:
                continue
            if v < -50 or v > 200:         # 범위 밖(999 등) 제외
                continue
            by_machine.setdefault(row[0], []).append(v)   # 없으면 [] 먼저, 있으면 그대로

    risky = {}
    for m, temps in by_machine.items():
        avg = sum(temps) / len(temps)
        if avg > threshold:                # 기준 초과 설비만
            risky[m] = round(avg, 1)
    return risky

print("주의 설비:", find_risky("_a.csv"))
# → 주의 설비: {'M01': 71.0, 'M02': 74.0}
#   M01 (70+72)/2=71.0 > 70 (주의)
#   M02 999는 범위 밖이라 제외 → 74만 남아 평균 74 > 70 (주의)
#   M03 66 → 70 이하라 정상 (제외)


# =============================================================================
#  임시 파일 정리
# =============================================================================
for fn in ["_a.csv", "_log.txt"]:
    if os.path.exists(fn):
        os.remove(fn)


# =============================================================================
#  1~9장 마무리 ― '순수 파이썬'의 끝
# -----------------------------------------------------------------------------
#   변수·자료형·연산 → 문자열 → 리스트·조건·반복 → 자료구조 → 함수
#   → 모듈·파일 → 예외처리 → '데이터 처리 파이프라인'까지 왔다.
#
#   지금은 CSV 한 줄씩 직접 처리하지만,
#   10장부터 배울 numpy·pandas가 이 모든 과정을 몇 줄로 압축해 준다.
#   그 편리함을 제대로 느끼려면, 지금 이 '직접 처리'를 이해하는 게 중요하다.
# =============================================================================

print()
print("09_04 복습 완료")
