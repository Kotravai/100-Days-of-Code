from tkinter import *
import math

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    top_label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    ticker.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        top_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        top_label.config(text="Break", fg=PINK)
    else:
        count_down(work)
        top_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minute = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✅"



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO Timer")
# window.minsize(height=400, width=350)
window.config(padx=50, pady=50, bg=YELLOW)

check = "✓"

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))

top_label = Label()
top_label.config(text="Timer", font=(FONT_NAME, 30, "bold"), foreground=GREEN, bg=YELLOW)
top_label.grid(row=0, column=1)

ticker = Label(background=YELLOW, foreground=GREEN)
ticker.grid(row=3, column=1)

stop_button = Button(padx=5, pady=5, text="start")
stop_button.config(font=(FONT_NAME, 13, "bold"), highlightthickness=0, command=start_timer)
stop_button.grid(row=3, column=0)

reset_button = Button(padx=5, pady=5, text="reset")
reset_button.config(font=(FONT_NAME, 13, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=2)

window.mainloop()
