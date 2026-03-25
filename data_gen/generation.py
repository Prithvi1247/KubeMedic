import random

def generate_smooth_cpu(n=50):
    cpu = []
    val = random.randint(25, 30)

    for _ in range(n):
        val += random.randint(-2, 2)  # small fluctuation
        val = max(20, min(40, val))   # keep in range
        cpu.append(val)

    return cpu
def generate_smooth_memory(n=50):
    memory = []
    val = random.randint(220, 260)

    for _ in range(n):
        val += random.randint(-5, 5)
        val = max(200, min(300, val))
        memory.append(val)

    return memory
def generate_normal(n=50):
    cpu = generate_smooth_cpu(n)
    memory = generate_smooth_memory(n)
    restarts = [0 for _ in range(n)]
    restarts[3]=1
    restarts[33]=1

    network = [random.randint(100, 150) for _ in range(n)]
    
    return cpu, memory, restarts, network

def add_cpu_spike(cpu, duration=20):
    for i in range( duration):
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
        network.append(random.randint(200, 300))  # real spike
    return network





