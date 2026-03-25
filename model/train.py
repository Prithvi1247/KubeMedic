import numpy as np
from data_gen.generation import add_cpu_spike, generate_normal, add_crash_loop,add_memory_leak,add_traffic_spike
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1)

cpu_train, mem_train, res_train, net_train = generate_normal(100)

X_train = np.array(list(zip(cpu_train, mem_train, res_train, net_train)))
cpu_n, mem_n, res_n, net_n = generate_normal(100)

cpu_test, mem_test, res_test, net_test = generate_normal(50)
cpu_test = add_cpu_spike(cpu_test, duration=20)
mem_test = add_memory_leak(mem_test, duration=20)
res_test = add_crash_loop(res_test, duration=20)
net_test = add_traffic_spike(net_test, duration=20)
X_test = np.array(list(zip(cpu_test, mem_test, res_test, net_test)))

model.fit(X_train)

preds = model.predict(X_test)

for i, p in enumerate(preds):
    if p == -1:
        print(f"⚠️ Anomaly detected at timestep {i}")