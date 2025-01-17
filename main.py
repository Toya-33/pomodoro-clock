import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_start = None

# ---------------------------- TIMER RESET ----------------------------- #
def timer_reset():
    window.after_cancel(timer_start)
    canvas.itemconfig(timer_txt, text="00:00")
    timer.config(text="Timer")
    global reps
    reps = 0
    tick.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    window.wm_deiconify()
    window.lift()
    window.attributes('-topmost', True)
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="L Break")
        reps = 0
    elif reps % 2 != 0:
        count_down(work_sec)
        timer.config(text="Work")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="S Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    elif count_second < 10:
        count_second = f"0{count_second}"
    if count_minute == 0:
        count_minute = "00"
    canvas.itemconfig(timer_txt, text=f"{count_minute}:{count_second}")
    global timer_start
    if count > 0:
        timer_start = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start = Button(text="Start", font=FONT_NAME, bg="white", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", font=FONT_NAME, bg="white", highlightthickness=0, command=timer_reset)
reset.grid(row=2, column=2)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
tick.grid(row=3, column=1)
window.mainloop()
