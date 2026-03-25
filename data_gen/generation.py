import random

def generate_normal(n=50):
    cpu = [random.randint(20, 40) for _ in range(n)]
    memory = [random.randint(200, 300) for _ in range(n)]
    restarts = [0 for _ in range(n)]
    network = [random.randint(100, 200) for _ in range(n)]
    
    return cpu, memory, restarts, network

def add_cpu_spike(cpu, start=50, duration=20):
    for i in range(start, start + duration):
        cpu.append(random.randint(85, 100))  # spike
    return cpu

def add_memory_leak(memory, duration=20):
    last = memory[-1]
    for i in range(duration):
        last += random.randint(5, 10)  # gradual increase
        memory.append(last)
    return memory

def add_crash_loop(restarts, duration=20):
    count = 0
    for i in range(duration):
        count += 1
        restarts.append(count)
    return restarts

def add_traffic_spike(network, duration=20):
    for _ in range(duration):
        network.append(random.randint(500, 800))  # real spike
    return network





