import time


def p():
    time.sleep(2.5)


t0 = time.perf_counter()
p()
t1 = time.perf_counter()

print(t1 - t0)
