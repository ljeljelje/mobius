import numpy as np
import matplotlib.pyplot as plt

# 1. 설정값 (설계 자료 기준) [cite: 137, 138, 140, 155]
v0 = 30.0    # 종방향 속도 (30m/s) [cite: 137]
sT = 300.0   # 종방향 목표 거리 (300m) [cite: 138]
yT = 3.5     # 횡방향 목표 거리 (차선 폭 3.5m) [cite: 138, 139]
T = 10.0     # 도달 시간 (sT / v0 = 10s) [cite: 140, 142]
L = 2.7      # 차량 축거 (Wheelbase, 예시값 2.7m) [cite: 154, 155]

# 2. 5차 다항식 계수 결정을 위한 행렬 구성 (y(0), y'(0), y''(0), y(T), y'(T), y''(T)) [cite: 133, 134, 144]
# 경계 조건: 시작과 끝의 속도와 가속도는 모두 0 
A = np.array([
    [1, 0, 0, 0, 0, 0],              # y(0)
    [0, 1, 0, 0, 0, 0],              # y'(0)
    [0, 0, 2, 0, 0, 0],              # y''(0)
    [1, T, T**2, T**3, T**4, T**5],  # y(T)
    [0, 1, 2*T, 3*T**2, 4*T**3, 5*T**4], # y'(T)
    [0, 0, 2, 6*T, 12*T**2, 20*T**3]     # y''(T)
])

B = np.array([0, 0, 0, yT, 0, 0])    # 목표 상태값 

# 3. np.linalg.solve를 이용한 계수(a0~a5) 추출 [cite: 95]
a = np.linalg.solve(A, B)

# 4. 시간축 설정 및 데이터 계산
t = np.linspace(0, T, 100)
y = a[0] + a[1]*t + a[2]*t**2 + a[3]*t**3 + a[4]*t**4 + a[5]*t**5 # 위치 [cite: 132]
y_ddot = 2*a[2] + 6*a[3]*t + 12*a[4]*t**2 + 20*a[5]*t**3           # 횡가속도 [cite: 37]

# 5. 곡률(kappa) 및 조향각(delta) 추출 [cite: 149, 154]
kappa = y_ddot / (v0**2)  # 곡률 근사식 [cite: 149]
delta = L * kappa         # 조향각 (Rad) 
delta_deg = np.degrees(delta) # 시각화를 위해 도(degree)로 변환

# 6. 결과 시각화
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, y, 'b', label='Lateral Position d(t)')
plt.ylabel('d (m)')
plt.title('Lane Change Trajectory (5th Order Polynomial)')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, kappa, 'g', label='Curvature kappa(t)')
plt.ylabel('Curvature (1/m)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, delta_deg, 'r', label='Steering Angle delta(t)')
plt.xlabel('Time (s)')
plt.ylabel('Steering Angle (deg)')
plt.grid(True)

plt.tight_layout()
plt.show()