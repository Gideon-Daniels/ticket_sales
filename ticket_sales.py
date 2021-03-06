from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

window = Tk()
window.title("Ticket Sales")
window.config(bg="#0d1117")
window.geometry("500x600")



# Gideon Daniels


class ClcTicketSales:
    cell_num = StringVar()
    price = StringVar()
    num_of_tickets = StringVar()
    variable = StringVar()
    variable.set("Choose an category")

    def __init__(self, window):
        # Labels
        self.label1 = Label(window, text="Enter cell number")
        self.label2 = Label(window, text="Select Ticket Category")
        self.label3 = Label(window, text="Number of tickets bought")
        # Entries
        self.cell_num_entry = Entry(window)
        # self.select_ticket_category = OptionMenu(window, self.variable, "Soccer", "Movie", "Theatre")
        self.select_ticket_category = Combobox(window, text=self.variable)
        self.select_ticket_category['values'] = ("Soccer", "Movie", "Theater")
        self.number_of_tickets_bought = Spinbox(window, from_=0, to=100, )
        # buttons
        self.calculate_ticket_button = Button(window, text="Calculate Ticket", command=self.calc_prepayment)
        self.clear_entries_button = Button(window, text="Clear", command=self.clear)
        # Output
        self.output_label_1 = Label(window, text="", textvariable=self.price)
        self.output_label_2 = Label(window, text="", textvariable=self.num_of_tickets)
        self.output_label_3 = Label(window, text="", textvariable=self.cell_num)
        self.output_pattern_top = Label(window, text="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        self.output_pattern_bottom = Label(window, text="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        # Placing
        # First Column x= 10
        self.label1.place(x=10, y=100)
        self.label2.place(x=10, y=175)
        self.label3.place(x=10, y=250)
        self.calculate_ticket_button.place(x=10, y=325)
        # Second Column x = 250
        self.cell_num_entry.place(x=250, y=100)
        self.select_ticket_category.place(x=250, y=175)
        self.number_of_tickets_bought.place(x=250, y=250)
        self.clear_entries_button.place(x=350, y=325)
        # Output
        self.output_pattern_top.place(x=10, y=360)
        self.output_label_1.place(x=100, y=400)
        self.output_label_2.place(x=100, y=425)
        self.output_label_3.place(x=100, y=450)
        self.output_pattern_bottom.place(x=10, y=490)
    # Functions

    def calc_prepayment(self):
        try:
            if self.select_ticket_category.get() == "Soccer":
                pay_me = float(self.number_of_tickets_bought.get()) * 40 + 0.14 * (
                            float(self.number_of_tickets_bought.get()) * 40)
                self.price.set("Amount Payable: R" + str(pay_me))
                self.num_of_tickets.set(
                    "Reservation for " + self.select_ticket_category.get() + " for " + self.number_of_tickets_bought.get())
                self.cell_num.set("was done by " + self.cell_num_entry.get())

            elif self.select_ticket_category.get() == "Movie":
                pay_me = float(self.number_of_tickets_bought.get()) * 75 + 0.14 * (
                            float(self.number_of_tickets_bought.get()) * 75)
                self.price.set("Amount Payable: R" + str(pay_me))
                self.num_of_tickets.set(
                    "Reservation for " + self.select_ticket_category.get() + " for " + self.number_of_tickets_bought.get())
                self.cell_num.set("was done by " + self.cell_num_entry.get())

            elif self.select_ticket_category.get() == "Theatre":
                pay_me = float(self.number_of_tickets_bought.get()) * 100 + 0.14 * (
                            float(self.number_of_tickets_bought.get()) * 100)
                self.price.set("Amount Payable: R" + str(pay_me))
                self.num_of_tickets.set(
                    "Reservation for " + self.select_ticket_category.get() + " for " + self.number_of_tickets_bought.get())
                self.cell_num.set("was done by " + self.cell_num_entry.get())

        except ValueError:
            messagebox.showerror("error", "Invalid input. Please try again.")



    def clear(self):
        self.cell_num_entry.delete(0, END)
        # self.select_ticket_category.delete(0, END)
        self.number_of_tickets_bought.delete(0, END)


object_ticket_sales = ClcTicketSales(window)
window.mainloop()