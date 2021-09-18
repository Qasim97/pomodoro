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
cycle = 0
timer_record = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global cycle
    window.after_cancel(timer_record)
    canvas.itemconfig(text_time, text="00:00")
    timer_label.config(text="Timer")
    mark_label.config(text="")
    cycle = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global cycle
    cycle += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if cycle == 8:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif cycle % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_record
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds <= 9:
        count_seconds = "0" + str(count_seconds)

    updated_text = str(count_min) + ":" + str(count_seconds)
    canvas.itemconfig(text_time, text=updated_text)
    if count > 0:
        timer_record = window.after(1000, count_down, count - 1)
    else:
        timer()
        marks = ""
        working_session = math.floor(cycle / 2)
        for _ in range(working_session):
            marks += "✔"
        mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=img_tomato)
text_time = canvas.create_text(103, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

mark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
mark_label.grid(column=2, row=4)
window.mainloop()
