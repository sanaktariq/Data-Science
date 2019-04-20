import numpy as np
import matplotlib.pyplot as plt

def circle_segment(res, i, radius):
    return np.array([np.cos(((2 * np.pi) / res) * i) * radius,
                     np.sin(((2 * np.pi) / res) * i) * radius])

def circle(radius, res=15):
    return np.array([circle_segment(res, i, radius) for i in range(0, res + 1)])

cir_result = circle(50, res=15)
#print(cir_result)
#print(cir_result[:, 0], cir_result[:, 1])

print(cir_result.tolist())
res1 = [[50.0, 0.0], [45.67727288213004, 20.336832153790006], [33.45653031794292, 37.15724127386971], [15.450849718747373, 47.552825814757675], [-5.226423163382667, 49.72609476841367], [-24.99999999999999, 43.30127018922194], [-40.450849718747364, 29.38926261462366], [-48.90738003669028, 10.395584540887986], [-48.907380036690284, -10.395584540887953], [-40.45084971874737, -29.38926261462365], [-25.00000000000002, -43.30127018922192], [-5.226423163382711, -49.72609476841367], [15.450849718747362, -47.55282581475768], [33.45653031794289, -37.15724127386974], [45.677272882130026, -20.336832153790045], [50.0, -1.2246467991473532e-14]]
print(cir_result.tolist() == res1)


#result = (cir_result[:, 0], cir_result[:, 1])
#print(result)

#plt.plot(cir_result[:, 0], cir_result[:, 1])
#print("cir_result[:, 0], cir_result[:, 1]")
#plt.show()
