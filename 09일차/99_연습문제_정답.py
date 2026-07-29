# =============================================================================
#  9일차 연습문제 ― 정답  (09장 예외처리)
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
# =============================================================================


print("[1]")
try:
    n = int("abc")                 # ValueError
except ValueError:
    print("변환 실패")
print("프로그램 계속")             # → 변환 실패 / 프로그램 계속
# try-except 덕분에 멈추지 않고 계속 진행


print("[2]")
try:
    x = 10 / 0                     # ZeroDivisionError
except ValueError:
    print("값 오류")
except ZeroDivisionError:
    print("0으로 나눔")            # → 0으로 나눔   (해당하는 except로 감)


print("[3]")
def safe_get(lst, i):
    try:
        return lst[i]
    except IndexError:
        return "범위 밖"
print(safe_get([10, 20, 30], 1))   # → 20
print(safe_get([10, 20, 30], 9))   # → 범위 밖


print("[4]")
def to_float(text):
    try:
        return float(text)
    except ValueError:
        return 0.0
print(to_float("3.14"))            # → 3.14
print(to_float("온도"))            # → 0.0
print(to_float("88"))              # → 88.0


print("[5]")
d = {"온도": 78, "압력": 95}
try:
    print(d["유량"])               # KeyError
except KeyError:
    print("키 없음")               # → 키 없음
# (참고: d.get("유량", "없음") 으로도 안전하게 처리 가능 — 06장)


print("[6]")
def check(text):
    try:
        v = int(text)
    except ValueError:
        print("실패")
    else:
        print("성공", v)           # 예외 없을 때만
    finally:
        print("끝")                # 무조건
check("10")                        # → 성공 10 / 끝
check("십")                        # → 실패 / 끝


print("[7]")
data = ["70", "ERR", "80", "90"]
total = 0.0
count = 0
for x in data:
    try:
        total += float(x)          # "ERR"에서 ValueError
        count += 1
    except ValueError:
        continue                   # 불량은 건너뛰기
print("정상", count, "개")          # → 정상 3 개
print("평균:", round(total / count, 1))   # → 평균: 80.0   (70+80+90=240, /3)


print("[8]")
try:
    v = float("스물")
except ValueError as e:
    print("원인:", e)              # → 원인: could not convert string to float: '스물'


print("[9]")
def check_pressure(p):
    if p < 0 or p > 10:
        raise ValueError("범위 밖")
    return p
print(check_pressure(5))           # → 5
try:
    check_pressure(50)             # 규칙 위반 → raise
except ValueError as e:
    print("오류:", e)              # → 오류: 범위 밖


print("[10]")
data = ["10", "20", "ERR", "40"]
total = 0
try:
    for x in data:
        total += int(x)            # "ERR"에서 ValueError → 반복 전체 중단!
except ValueError:
    print("중단됨")
print("합계:", total)
# → 중단됨 / 합계: 30
# try가 반복문 '밖'이라 첫 불량(ERR)에서 반복이 통째로 끝난다.
# 40은 더해지지 못함! (합계 30 = 10+20까지만)
# → 불량만 건너뛰려면 [7]처럼 try를 반복문 '안'에 둬야 한다.


print()
print("========== [도전] 미니 센서 분석 파이프라인 ==========")

records = [("M01", "70"), ("M02", "90"), ("M01", "ERR"),
           ("M02", "999"), ("M03", "78"), ("M02", "82")]

# (1) 정상값만 모아 통계
def analyze(records):
    valid = []
    for name, value in records:
        try:
            v = float(value)               # "ERR"에서 ValueError
            if v < 0 or v > 200:
                raise ValueError("범위 밖")  # 999 차단
            valid.append(v)
        except ValueError:
            continue                       # 불량은 건너뛰기
    result = {"정상수": len(valid)}
    if valid:
        result["평균"] = round(sum(valid) / len(valid), 1)
    return result

print(analyze(records))                    # → {'정상수': 4, '평균': 80.0}
# 정상값 70,90,78,82 → 합 320, 평균 80.0 (ERR·999 제외)

# (2) 설비별로 모아 평균 80 초과 = 주의 설비
by_machine = {}
for name, value in records:
    try:
        v = float(value)
        if v < 0 or v > 200:
            raise ValueError
    except ValueError:
        continue
    by_machine.setdefault(name, []).append(v)   # 없으면 [] 먼저

risky = []
for name, temps in by_machine.items():
    avg = sum(temps) / len(temps)
    if avg > 80:
        risky.append(name)
print("주의 설비:", risky)                  # → 주의 설비: ['M02']
# M01: 70 (ERR 제외) → 70 / M02: 90,82 (999 제외) → 86.0 > 80 (주의) / M03: 78


print()
print("정답 확인 완료 - 틀린 문제는 복습 파일을 다시 보세요")
