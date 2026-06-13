import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 경계 조건
# ---------------------------
T = 10.0

s0 = 0.0
v0 = 20.0
a0 = 0.0

sT = 100.0
vT = 0.0
aT = 0.0



# ---------------------------
# 5차 다항식 계수 계산
# s(t)=a0+a1 t+a2 t^2+a3 t^3+a4 t^4+a5 t^5
# ---------------------------

A = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [1, T, T**2, T**3, T**4, T**5],
    [0, 1, 2*T, 3*T**2, 4*T**3, 5*T**4],
    [0, 0, 2, 6*T, 12*T**2, 20*T**3]
])

b = np.array([s0, v0, a0, sT, vT, aT])

coeff = np.linalg.solve(A, b)

a0_c, a1_c, a2_c, a3_c, a4_c, a5_c = coeff

print("Quintic coefficients")
print(coeff)

# ---------------------------
# 시간 생성
# ---------------------------
t = np.linspace(0, T, 200)

# 위치
s = a0_c + a1_c*t + a2_c*t**2 + a3_c*t**3 + a4_c*t**4 + a5_c*t**5

# 속도 (미분)
v = a1_c + 2*a2_c*t + 3*a3_c*t**2 + 4*a4_c*t**3 + 5*a5_c*t**4

# 가속도 (2차 미분)
a = 2*a2_c + 6*a3_c*t + 12*a4_c*t**2 + 20*a5_c*t**3

# ---------------------------
# 그래프
# ---------------------------

plt.figure()
plt.plot(t, v)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("v-t graph using Quintic Trajectory")
plt.grid(True)
plt.show()