import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注时钟已启动，将持续 {minutes} 分钟。")
    time.sleep(seconds)
    print("专注时钟结束，时间已用尽！")

if __name__ == "__main__":
    try:
        minutes = int(input("请输入专注时钟的分钟数: "))
        focus_timer(minutes)
    except ValueError:
        print("无效的输入。请输入一个整数值作为分钟数。")
