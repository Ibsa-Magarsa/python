from tkinter import *
from tkinter import messagebox
def is_leap(year):
    if year % 4 == 0:
        if year %100 ==0:
            if year ==0:
                # print("Leap Year. ")
                return True 
            else:
                # print("Not Leao Year. ")
                return False
        else:
            # print("Leap Year. ")
            return True 
    else:
        # print("Not Leap Year. ")
        return False 
def days_in_month(year, month):
    if month > 12 or (month) < 1:
        messagebox.showerror(title="Oops", message="Invalid argument")
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for x in month_days:
        if is_leap(year) and month == 2:
            messagebox.showinfo(title="Month", message= 29)
            return 29
            
    messagebox.showinfo(title="Month", message= f"{month_days[month -1]}")

    # return month_days[month -1]

window = Tk()
window.title("Leap Year")

year_label = Label(text="Year:", bg="yellow", font=("Arial", 10, "bold"))
year_label.grid(column=1, row=1)
month_label = Label(text="Month:", bg="yellow", font=("Arial", 10, "bold"))
month_label.grid(column=1, row=2)

year_entry = Entry(width=30, bd=4, font=("Arial", 10, "bold"))
# year_entry.insert(END, 0)
year_entry.focus()
year_entry.grid(column=2, row=1)
month_entry = Entry(width=30, bd=4, font=("Arial", 10, "bold"))
# month_entry.insert(END, 0)
month_entry.grid(column=2, row=2)

search_button = Button(window, text="Search",width=14, command=lambda:days_in_month(year= (int(year_entry.get())),month = int(month_entry.get())))
search_button.grid(column=2, row=3)

window.mainloop()
