from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Registration Form")
root.geometry("780x400+320+80")
root.configure(background="#365899")
main_heading = Label(root,text="Registration Form", fg="black",bg="#365899", font=("Algerian", 26, "bold underline"))
main_heading.grid(row=0, columnspan=13, padx=200, pady=20)


def getdata():
    print(f"{name_var.get()}, {id_var.get()}, {email_var.get()}, {gender_var.get()}, {phone_var.get()}, {country_var.get()}")
    clear_widgets()

def clear_widgets():
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)



# All Variables
name_var = StringVar()
id_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
phone_var = StringVar()
country_var = StringVar()

# For Student Name
name_label = Label(root, text="Student Name", font=("times new roman", 20, "bold"),fg="#cedb18", bg="#365899")
name_label.grid(row=1, column=6, sticky="w")
name_entry = Entry(root, textvariable=name_var, width=26, font=("times new roman", 17, "bold"))
name_entry.grid(row=1,column=7)
name_entry.focus()

# For Student Id
id_label = Label(root, text="Student Id", fg="#cedb18",bg="#365899", font=("times new roman", 20, "bold"))
id_label.grid(row=2, column=6, sticky="w")
id_entry = Entry(root, textvariable=id_var, width=26, font=("times new roman", 17, "bold"))
id_entry.grid(row=2, column=7)

# For E-mail
email_label = Label(root, text="E-mail", fg="#cedb18", bg="#365899", font=("times new roman", 20, "bold"))
email_label.grid(row=3, column=6, sticky="w")
email_entry = Entry(root, textvariable=email_var, width=26, font=("times new roman", 17, "bold"))
email_entry.grid(row=3, column=7)

#For Gender
gender_label = Label(root, text="Gender", bg="#365899", font=("times nem roman", 18, "bold"), fg="#cedb18")
gender_label.grid(row=4, column=6, sticky="w")
combo_gender = ttk.Combobox(root, textvariable=gender_var,width=24, font=("times new roman", 17, "bold"), state="readonly")
combo_gender['values'] = ("Male", "Female","Others")
combo_gender.grid(row=4, column=7)

# For Phone No.
phone_label = Label(root, text="Phone No.",bg="#365899", fg="#cedb18", font=("times new roman", 20, "bold"))
phone_label.grid(row=5, column=6, sticky="w")
phone_entry = Entry(root, textvariable=phone_var, width=26, font=("times new roman", 17, "bold"))
phone_entry.grid(row=5, column=7)

# For Country
country_label = Label(root, text="Country",bg="#365899", font=("times nem roman", 18, "bold"), fg="#cedb18")
country_label.grid(row=6, column=6, sticky="w")
combo_country = ttk.Combobox(root, textvariable=country_var,width=24, font=("times new roman", 17, "bold"), state="readonly")
combo_country['values'] = ("India", "United State", "Europe", "China", "Nepal")
combo_country.grid(row=6, column=7)

# Submit Button
submit_btn = Button(root, text="Submit", fg="red", bg="#365899",bd=3, font=("times new roman", 15, "bold"), relief=RIDGE, command=getdata)
submit_btn.grid(row=7, columnspan=13, pady=20)


root.mainloop()