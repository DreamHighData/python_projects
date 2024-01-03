
# psutil : 컴퓨터 정보를 확인할 때, 사용하는 라이브러리
import psutil

# CPU 속도
cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"cpu 속도: {cpu_current_ghz} GHZ")

# CPU 물리코어 수
cpu_core = psutil.cpu_count(logical=False)
print(f"코어 : {cpu_core} 개")

# 메모리 정보 출력
memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print(f"메모리 : {memory_total} GB")

# 디스크 정보 출력
disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f"디스크 크기 : {disk_total} GB")
# print(disk)

# 네크워크를 통해 보내고 받는 데이터양 출력
# 보내고 받는 데이터는 누적 데이터 값입니다.
net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2,1)
recv = round(net.bytes_recv/1024**2,1)
print(f"보내기 : {sent} MB")
print(f"받기 : {recv} MB")
# print(net)
