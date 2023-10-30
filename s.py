import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注时钟已启动，将持续 {minutes} 分钟。")
    time.sleep(seconds)
    print("专注时钟结束，时间已用尽！")

if __name__ == "__main__":
    while True:
        try:
            minutes = 30  # 设置每30分钟运行一次专注时钟
            focus_timer(minutes)
        except KeyboardInterrupt:
            print("专注时钟被中断。")
            break
