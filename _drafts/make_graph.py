import matplotlib.pyplot as plt

# 데이터
cores = [8, 16, 32, 64, 128, 256, 512, 1024]
naive_times = [391, 207, 127, 111, 151, 267, 517, 1026]
ours_times = [387, 196, 101, 54, 31, 20, 15, 13]

cores = [8, 16, 32, 64, 128, 256, 512, 1024]  # X축 값
naive_times = [391, 207, 127, 111, 151, 267, 517, 1026]
ours_times = [387, 196, 101, 54, 31, 20, 15, 13]

# 그래프 생성
plt.figure(figsize=(8, 5))
plt.plot(cores, naive_times, marker='o', linestyle='-', label="Naïve", color="blue")
plt.plot(cores, ours_times, marker='o', linestyle='-', label="Ours", color="red")

# X축을 8, 16, 32, 64, 128, ... 로 설정
plt.xscale("log", base=2)  # 로그 스케일 (밑을 2로 설정하여 8, 16, 32 간격 동일하게)
plt.xticks(cores, labels=[str(c) for c in cores])  # X축 값 설정 (문자열로 변환하여 정확히 표시)

# 레이블 추가
plt.xlabel("# of cores")
plt.ylabel("Processing time")
plt.legend()
plt.grid(True)

# 그래프 표시
plt.show()