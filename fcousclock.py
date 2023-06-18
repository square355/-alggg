import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("时间到！专注时间结束。")

if __name__ == "__main__":
    focus_minutes = int(input("请输入专注时间（分钟）："))
    focus_timer(focus_minutes)
