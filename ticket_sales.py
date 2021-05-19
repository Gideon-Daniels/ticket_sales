from tkinter import *
window = Tk()
window.title("Ticket Sales")
window.geometry("800x800")

# Gideon Daniels


class ClcTicketSales:

    def __init__(self, window, ):
        self.variable = StringVar()
        self.cell = StringVar()
        self.category = StringVar()
        self.tickets = StringVar()
        self.output_results = StringVar()
        self.variable.set("Choose an category")
        # Labels
        self.label1 = Label(window, text="Enter cell number")
        self.label2 = Label(window, text="Select Ticket Catagory")
        self.label3 = Label(window, text="Number of tickets bought")
        # Entries
        self.cell_num_entry = Entry(window)
        self.select_ticket_category = OptionMenu(window, self.variable, "Soccer", "Movie", "Theatre")  # change to drop down box
        self.number_of_tickets_bought = Spinbox(window, from_=0, to=100, textvariable=self.tickets)
        #buttons
        self.calculate_ticket_button = Button(window, text="Calculate Ticket", command=lambda: self.calc_prepayment(
                                      self.cell_num_entry.get(), self.select_ticket_category, self.number_of_tickets_bought.get()))
        self.clear_entries_button = Button(window, text="Clear Entries", command=self.clear)
        #Output
        self.output_label = Label(window, textvariable=self.output_results, bg="#ffe", width=75, height=75)
        #Placing

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
        self.output_label.place(x=10, y=400)

    def calc_prepayment(self, cell_num, category, nr_tickets):
        if category == "Soccer":
            total = self.nr_tickets * 40
            total_vat_included = total - int(total * 14/100)
            output = "Amount Payable : " + str(total_vat_included) + "\n" + \
                     "Reservation for soccer for "+ str(nr_tickets) + \
                     "was done by" + str(cell_num)
            return self.output_results.set(output)

        elif category == "Movie":
            total = nr_tickets * 75
            total_vat_included = total - int(total * 14/100)
            output = "Amount Payable : " + str(total_vat_included) + "\n" + \
                     "Reservation for soccer for " + str(nr_tickets) + \
                     "was done by" + str(cell_num)
            return self.output_results.set(output)

        elif category == "Theater":
            total = nr_tickets * 100
            total_vat_included = total - int(total * 14/100)
            output = "Amount Payable : " + str(total_vat_included) + "\n" + \
                     "Reservation for soccer for " + str(nr_tickets) + \
                     "was done by" + str(cell_num)
            return self.output_results.set(output)

    def clear(self):
        self.cell_num_entry.delete()
        self.select_ticket_catagory.delete()
        self.number_of_tickets_bought.delete()
        self.select_ticket_catagory.delete()
        self.output_label.set(" ")



# nr_tickets_picked = ClcTicketSales.__getattribute__("number_of_tickets_bought")
# category_selected = ClcTicketSales.__getattribute__("select_ticket_category")



ClcTicketSales(window)
window.mainloop()
