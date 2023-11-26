import numpy as np

w11 = [0.3, 0.3, 0]
w12 = [0.4, -0.5, 1]
weight1 = np.array([w11, w12])
print(weight1)
inside = np.dot(weight1, [1, 0, 1])

print("Значения сумм на нейронах скрытого слоя: ", inside)

def act(x):
    return 0 if x < 0.5 else 1
out_hidden = np.array([act(x) for x in inside])
print("Значения на выходах нейронов скрытого слоя: " + str(out_hidden))

weight2 = np.array([-1, 1])
sum_end = np.dot(weight2, out_hidden)
y = act(sum_end)

print("Выходное значение НС: " + str(y))