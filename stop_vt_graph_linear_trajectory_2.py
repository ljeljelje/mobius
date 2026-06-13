import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 선형 조건
# ---------------------------

_v0 = 20.0      # 초기 속도 (m/s)
_vT =  0.0      # 마지막 속도 (m/s)
_sT = 100.0     # 이동 거리(m)

_a = (_vT**2 - _v0**2) / (2*_sT)
_T = (_vT - _v0) / _a

# ---------------------------
# 기본 조건
# ---------------------------
v0 = _v0
a_const = _a
T = _T

t = np.linspace(0, T, 200)

# ---------------------------
# 1️⃣ 등가속도 감속 (직선)
# ---------------------------
v_linear = v0 + a_const * t


# ---------------------------
# 2️⃣ Quintic Trajectory
# ---------------------------

s0 = 0.0
v0 = _v0
a0 = 0.0

sT = _sT
vT = _vT
aT = 0.0

A = np.array([
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,2,0,0,0],
    [1,T,T**2,T**3,T**4,T**5],
    [0,1,2*T,3*T**2,4*T**3,5*T**4],
    [0,0,2,6*T,12*T**2,20*T**3]
])

b = np.array([s0, v0, a0, sT, vT, aT])

coeff = np.linalg.solve(A, b)

a0_c, a1_c, a2_c, a3_c, a4_c, a5_c = coeff

v_quintic = (
    a1_c
    + 2*a2_c*t
    + 3*a3_c*t**2
    + 4*a4_c*t**3
    + 5*a5_c*t**4
)

# ---------------------------
# 그래프
# ---------------------------

plt.figure(figsize=(8,5))

plt.plot(t, v_linear, color='green', label='Linear Deceleration')
plt.plot(t, v_quintic, color='red', label='Quintic Trajectory')

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity-Time Comparison")

plt.legend()
plt.grid(True)

plt.show()
