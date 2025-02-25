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
    global reps
    window.after_cancel(timer)
    title_label.config(text="TIMER",  fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0
    checkmark_label.config(text="", font=(FONT_NAME, 12))


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
        # reset_timer()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            checkmark_label.config(text=mark, font=(FONT_NAME, 12))
            

# ---------------------------- UI SETUP ------------------------------- #
#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1,row=1)

#Title Label
title_label = Label(text="TIMER", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1,row=0)

#Buttons
button = Button(text="Start", command=start_timer, highlightthickness=0)
button.grid(column=0,row=2)
button = Button(text="Reset", command=reset_timer, highlightthickness=0)
button.grid(column=2,row=2)

#CheckMark Label
checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1,row=3)


window.mainloop()