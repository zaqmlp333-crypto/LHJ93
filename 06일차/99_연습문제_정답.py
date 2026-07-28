# =============================================================================
#  6일차 연습문제 ― 정답  (06_01 튜플과 셋 · 06_02 딕셔너리)
# -----------------------------------------------------------------------------
#  결과만 같으면 다른 방법으로 풀어도 맞습니다.
# =============================================================================


print("[1]")
s = ("베어링진동", 0.8)
print(s)                           # → ('베어링진동', 0.8)
print(s[0])                        # → 베어링진동
print(s[1])                        # → 0.8
# name, value = s  로 언패킹해서 출력해도 정답


print("[2]")
a = (100)                          # 쉼표 없음 → 그냥 숫자
b = (100,)                         # 쉼표 있음 → 튜플
print(type(a))                     # → <class 'int'>
print(type(b))                     # → <class 'tuple'>


print("[3]")
point = (7, 3)
x, y = point                       # 언패킹
print(f"x={x} y={y}")              # → x=7 y=3


print("[4]")
sensors = [("모터온도", 78), ("회전속도", 1750), ("펌프압력", 95)]
for name, value in sensors:        # 반복 + 언패킹
    if value > 100:
        print(name, value, "(초과)")
    else:
        print(name, value)
# → 모터온도 78 / 회전속도 1750 (초과) / 펌프압력 95


print("[5]")
logs = ["S01", "S02", "S01", "S03", "S02", "S01"]
unique = set(logs)                 # 중복 제거
print("종류 수:", len(unique))      # → 종류 수: 3
print(sorted(unique))              # → ['S01', 'S02', 'S03']


print("[6]")
box = {"A", "B"}
box.add("C")                       # 추가 → {A,B,C}
box.add("A")                       # 이미 있음 → 무시
box.add("B")                       # 이미 있음 → 무시
print(len(box))                    # → 3  (A,B,C 뿐)


print("[7]")
line_a = {"S01", "S02", "S03"}
line_b = {"S03", "S04", "S05"}
print("공통", sorted(line_a.intersection(line_b)))   # → ['S03']
print("A만", sorted(line_a.difference(line_b)))      # → ['S01', 'S02']
print("B만", sorted(line_b.difference(line_a)))      # → ['S04', 'S05']
# a & b, a - b, b - a 로 써도 같은 결과


print("[8]")
sensors = {"온도": 78, "진동": 0.5}
sensors["압력"] = 95               # 추가
sensors["온도"] = 80               # 수정 (같은 문법!)
print(sensors)                     # → {'온도': 80, '진동': 0.5, '압력': 95}


print("[9]")
d = {"온도": 78, "압력": 95}
print("온도" in d)                  # → True   (키 존재)
print(78 in d)                     # → False  (78은 값이라 False!)
print(d.get("유량", 0))            # → 0      (없으면 기본값)


print("[10]")
sensors = {"온도": 80, "진동": 55, "압력": 95, "유량": 0}
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))      # → 평균: 57.5   (230 / 4)


print("[11]")
sensors = {"온도": 80, "진동": 55, "압력": 95}
top = ""                           # 최댓값 센서 이름
hi = 0                             # 최댓값
for name, v in sensors.items():
    if v > hi:                     # 갱신 패턴
        hi = v
        top = name
print("최댓값 센서:", top, hi)      # → 최댓값 센서: 압력 95


print("[12]")
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 81, "압력": 95}
sensors.update(new_data)           # 모터온도 수정 + 압력 추가
del sensors["진동"]                # 삭제
print(sensors)                     # → {'모터온도': 81, '압력': 95}
print("센서 수:", len(sensors))     # → 센서 수: 2


print("[13]")
names = ["온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
print(sensors)                     # → {'온도': 78, '진동': 0.5, '압력': 95}
for name, value in sensors.items():
    print(f"{name}: {value}")
# → 온도: 78 / 진동: 0.5 / 압력: 95


print("[14]")
values = {"온도": 95, "진동": 0.5, "압력": 96}
limits = {"온도": 90, "진동": 1.0, "압력": 90}
warning = []
for name, value in values.items():
    if value > limits[name]:       # 같은 이름의 임계값과 비교
        warning.append(name)
print("경고 센서:", warning)        # → 경고 센서: ['온도', '압력']
# 온도 95>90 O, 진동 0.5<1.0 X, 압력 96>90 O


print()
print("========== [도전] 설비 관제 종합 ==========")

plant = {
    "1번모터": {"온도": 78, "상태": "정상"},
    "2번펌프": {"온도": 91, "상태": "경고"},
    "3번팬": {"온도": 77, "상태": "경고"},
}

# (1) 설비 수
count = len(plant)

# (2) 온도 평균 — 모든 설비의 온도를 누적
total = 0
for name, info in plant.items():
    total += info["온도"]           # 안쪽 딕셔너리의 "온도"
avg = total / count                # 246 / 3

# (3) 경고 설비를 셋에 모으기
danger = set()
for name, info in plant.items():
    if info["상태"] == "경고":
        danger.add(name)

# (4) 리포트
print("=" * 5 + " 관제 리포트 " + "=" * 5)
print(f"설비 수: {count}")
print(f"평균 온도: {avg:.1f}도")
print(f"경고 설비: {sorted(danger)}")
print("=" * 21)
# → ===== 관제 리포트 =====
# → 설비 수: 3
# → 평균 온도: 82.0도
# → 경고 설비: ['2번펌프', '3번팬']
# → =====================
# [중첩 딕셔너리 순회 + 누적 평균 + 셋 수집 + f-string 총동원]


print()
print("정답 확인 완료 - 틀린 문제는 복습 파일을 다시 보세요")
