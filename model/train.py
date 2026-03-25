import numpy as np
from data_gen.generation import add_cpu_spike, generate_normal, add_crash_loop,add_memory_leak,add_traffic_spike
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.07 )

cpu_train, mem_train, res_train, net_train = generate_normal(500)
cpu_add, mem_add, res_add, net_add = generate_normal(50)

X_train = np.array(list(zip(cpu_train, mem_train, res_train, net_train)))
mean_t = X_train.mean(axis=0)
std_t = X_train.std(axis=0)
std_t[std_t == 0] = 1
X_train_norm = (X_train - mean_t) / std_t # normalised training data



cpu_test, mem_test, res_test, net_test = generate_normal(50)
cpu_test = add_cpu_spike(cpu_test, duration=20)
mem_test = add_memory_leak(mem_test, duration=20)
res_test = add_crash_loop(res_test, duration=20)
net_test = add_traffic_spike(net_test, duration=20)

X_test = np.array(list(zip(cpu_test+cpu_add, mem_test+mem_add, res_test+res_add, net_test + net_add)))
X_test_norm = (X_test - mean_t)/ std_t # normalised test

model.fit(X_train_norm)

preds = model.predict(X_test_norm)

# for i, p in enumerate(preds):
#     if p == -1:
#         print(f"⚠️ Anomaly detected at timestep {i}")

scores = model.decision_function(X_test_norm)

# for i in range(len(scores)):
#     print(i, scores[i])

threshold = -0.08  # tune this

for i, s in enumerate(scores):
    if s < threshold:
        print(f"⚠️ Anomaly at timestep {i}")