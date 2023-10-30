# 导入需要用到的库和模块
import tkinter as tk
import time
import winsound

# 定义一个类，用于创建专注时钟
class FocusClock:
    # 初始化函数
    def __init__(self):
        # 初始化变量
        self.focus_time = 25 * 60 # 专注时间为25分钟
        self.break_time = 5 * 60 # 休息时间为5分钟
        self.long_break_time = 15 * 60 # 长休息时间为15分钟
        self.focus_count = 0 # 专注次数计数器
        self.timer_running = False # 计时器是否运行的标志
        self.timer = None # 计时器对象

        # 创建窗口
        self.root = tk.Tk()

        # 创建一个标签，用于显示时间
        self.time_label = tk.Label(self.root, text=self.format_time(self.focus_time), font=("Arial", 40), fg="white", bg="black")
        self.time_label.pack()

        # 创建一个开始按钮，用于开始计时器
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT)

        # 创建一个停止按钮，用于停止计时器
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT)

    # 定义一个函数，用于格式化时间
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    # 定义一个函数，用于开始计时器
    def start_timer(self):
        if not self.timer_running: # 如果计时器没有运行
            self.timer_running = True # 设置计时器运行标志为真
            self.countdown() # 调用倒计时函数

    # 定义一个函数，用于停止计时器
    def stop_timer(self):
        if self.timer_running: # 如果计时器正在运行
            self.timer_running = False # 设置计时器运行标志为假
            if self.timer: # 如果计时器对象存在
                self.root.after_cancel(self.timer) # 取消计时器对象

    # 定义一个函数，用于倒计时
    def countdown(self):
        if self.focus_time > 0: # 如果专注时间大于0
            self.time_label.config(text=self.format_time(self.focus_time), bg="black") # 更新标签显示专注时间，并设置背景色为黑色
            self.focus_time -= 1 # 专注时间减1秒
            self.timer = self.root.after(1000, self.countdown) # 设置计时器对象为1秒后再次调用倒计时函数
        elif self.focus_count < 3: # 如果专注次数小于3次
            winsound.Beep(440, 1000) # 播放一声音
            self.focus_count += 1 # 专注次数加1
            self.focus_time = 25 * 60 # 重置专注时间为25分钟
            self.break_time -= 1 # 休息时间减1秒
            self.time_label.config(text=self.format_time(self.break_time), bg="green") # 更新标签显示休息时间，并设置背景色为绿色
            self.timer = self.root.after(1000, self.countdown) # 设置计时器对象为1秒后再次调用倒计时函数
        elif self.focus_count == 3: # 如果专注次数等于3次
            winsound.Beep(440, 1000) # 播放一声音
            self.focus_count = 0 # 重置专注次数为0
            self.focus_time = 25 * 60 # 重置专注时间为25分钟
            self.long_break_time -= 1 # 长休息时间减1秒
            self.time_label.config(text=self.format_time(self.long_break_time), bg="blue") # 更新标签显示长休息时间，并设置背景色为蓝色
            self.timer = self.root.after(1000, self.countdown) # 设置计时器对象为1秒后再次调用倒计时函数

# 定义一个函数，用于设置一丢丢风格
def main():
    # 创建一个专注时钟对象
    clock = FocusClock()
    # 设置窗口的标题，大小，背景色等
    clock.root.title("Focus Clock")
    clock.root.geometry("300x200")
    clock.root.configure(bg="white")
    # 进入主循环
    clock.root.mainloop()

# 如果是主模块，调用main函数
if __name__ == "__main__":
    main()
