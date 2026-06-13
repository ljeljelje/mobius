import numpy as np
import matplotlib.pyplot as plt

# 초기 조건
v0 = 20      # 초기 속도 (m/s)
a = -2       # 가속도 (m/s^2)
T = 10       # 정지 시간 (s)

# 시간 배열
t = np.linspace(0, T, 100)

# 속도 계산
v = v0 + a * t

# 그래프
plt.figure()
plt.plot(t, v)

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time (Deceleration to Stop)")

plt.grid(True)
plt.show()