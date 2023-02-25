from tkinter import *
import math

# ---------------------------- CONSTANTS AND GLOBAL VARIABLES ------------ #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    if start_button["state"] == "disabled":
        start_button["state"] = "active"
    global reps
    reps = 0
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text = f"00:00")
    checkmark_label.config(text = "")
    timer_label.config(text = "TIMER")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    start_button["state"] = "disable"
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg = PINK)
    else:
        count_down(work_sec)        
        timer_label.config(text="WORK", fg = GREEN)
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text = marks)    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# import time       ///////////// it s not gonna run because of the event driven and mainloop

# count = 5
# while count>=0:
#     time.sleep(1)
#     count -= 1


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"    

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)   
    else:
        start_timer()   


# ---------------------------- UI SETUP ------------------------------- #

#window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

#for the title
timer_label = Label(text="TIMER", fg = GREEN, font=(FONT_NAME, 28, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

#background image and default timer
canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
programmer_img = PhotoImage(file="programmer.png")
canvas.create_image(100, 112, image = programmer_img)
timer_text = canvas.create_text(100, 150, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text= "Start", highlightthickness=0, command=start_timer)
start_button.grid(row= 3, column=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 26, "bold"))
checkmark_label.grid(row=4, column=1)

reset_button = Button(text= "Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row= 3, column=2)


window.mainloop()