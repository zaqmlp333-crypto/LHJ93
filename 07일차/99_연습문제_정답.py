# =============================================================================
#  7일차 연습문제 ― 정답  (07장 함수)
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
# =============================================================================


print("[1]")
def cheer():
    print("오늘도 안전!")
cheer()
cheer()
cheer()                            # → 오늘도 안전! (3줄)


print("[2]")
def a():
    print("A")
print("B")                         # 먼저 실행
a()                                # 여기서 A 출력
print("C")
# → B / A / C
# def a() 정의는 실행이 아니라 '만들어 두기'. 실제 A는 a() 호출 때 나온다.


print("[3]")
def intro():
    print("=== 설비 점검 ===")
    print("담당자를 확인하세요")
    print("기록을 준비하세요")
intro()


print("[4]")
# 왜 출력이 없나: 함수를 정의(def)만 하고 호출하지 않았기 때문.
# 함수는 이름 뒤에 ()를 붙여 호출해야 실행된다.
def hello():
    print("안녕")
hello()                            # → 안녕   (호출 추가!)


print("[5]")
def start(name):
    print(name + " 가동 시작")
start("모터")                      # → 모터 가동 시작
start("펌프")                      # → 펌프 가동 시작


print("[6]")
def report(name, temp):
    print(name + ": " + str(temp) + "도")
report("모터", 78)                 # → 모터: 78도   (위치 인자)
report(temp=92, name="펌프")       # → 펌프: 92도   (키워드 인자, 순서 무관)


print("[7]")
def add(a, b):
    return a + b
x = add(10, 20)                    # 30을 돌려받아 x에 담음
print(x)                           # → 30
print(x + 100)                     # → 130   (돌려받은 값을 이어 씀)


print("[8]")
def show(v):
    print(v)                       # print만 하고 return 없음
result = show("측정값")            # → 측정값 (출력은 됨)
print(result)                      # → None   (돌려준 값이 없어서!)


print("[9]")
def calc(a, b):
    return a + b, a - b            # 두 값을 튜플로 반환
s, d = calc(20, 10)                # 언패킹
print("합", s, "차", d)            # → 합 30 차 10


print("[10]")
temps = [78, 92, 65, 81]
def stats(v):
    return min(v), max(v), sum(v) / len(v)
lo, hi, avg = stats(temps)
print("최소", lo, "최대", hi, "평균", avg)   # → 최소 65 최대 92 평균 79.0


print("[11]")
def judge(temp, limit=90):
    if temp > limit:
        return "경고"
    else:
        return "정상"
print(judge(95))                   # → 경고   (95 > 90)
print(judge(70))                   # → 정상
print(judge(50, 40))              # → 경고   (50 > 40, 기본값 덮어쓰기)


print("[12]")
x = 100
def change():
    x = 200                        # 함수 안 x (지역변수, 바깥과 별개)
    print(x)                       # → 200
change()
print(x)                           # → 100   (바깥 x는 그대로!)


print("[13]")
scores = [88, 92, 79]
def get_avg(values):
    return sum(values) / len(values)
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    else:
        return "C"
avg = get_avg(scores)              # 86.333...
print(avg, grade(avg))             # → 86.333... B


print("[14]")
def celsius_to_f(c):
    """섭씨 온도를 화씨로 변환한다."""
    return c * 1.8 + 32
print(celsius_to_f(25))            # → 77.0
print(celsius_to_f.__doc__)        # → 섭씨 온도를 화씨로 변환한다.


print()
print("========== [도전] 설비 점검 함수 세트 ==========")

motor = [90, 85]
pump = [70, 75]

def get_average(values):
    return sum(values) / len(values)

def get_status(avg, limit=85):
    if avg > limit:
        return "점검필요"
    else:
        return "양호"

def make_report(name, values):
    avg = get_average(values)                  # 안에서 다른 함수 호출
    status = get_status(avg)
    return f"[{name}] 평균 {avg:.1f}도 → {status}"

print(make_report("모터", motor))   # → [모터] 평균 87.5도 → 점검필요
print(make_report("펌프", pump))    # → [펌프] 평균 72.5도 → 양호
# 작은 함수(평균·판정)를 조합해 큰 함수(리포트)를 만드는 설계 패턴


print()
print("정답 확인 완료 - 틀린 문제는 복습 파일을 다시 보세요")
