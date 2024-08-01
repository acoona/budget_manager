import tkinter as tk
import datetime
import json

FONT = "Times New Roman"

def main():
    window = tk.Tk()
    window.title("Budget Manager")
    window.minsize(width=300,height=150)
    window.config(padx=20, pady=20)

    # title = tk.Label()
    # title.config(text="Budget Manager", font=("Times New Roman", 25, "bold"))
    # title.grid(row=0, column=1, columnspan=1)

    author = tk.Label()
    author.config(text="Designed by Xiaoming, made for Xiaoming", font=(FONT, 15, "italic"))
    author.grid(row=0, column=0, columnspan=2, padx=10, pady=30)

    document_button = tk.Button()
    document_button.config(text="Document", command=lambda: document(window), font=(FONT,15))
    document_button.grid(row=2,column=0)
    
    spending_button = tk.Button()
    spending_button.config(text="Spending history", command=spending_history, font=(FONT,15))
    spending_button.grid(row=2,column=1)

    window.mainloop()

def document(parent):
    new_document = tk.Toplevel(parent)
    new_document.transient(parent)
    new_document.title("Purchase")
    new_document.minsize(width=300, height=250)
    new_document.config(padx=20,pady=20)

    item_name = tk.Label(new_document, text="Name:", font=(FONT, 15))
    item_name.grid(row=0,column=0,pady=10)
    
    item_amount = tk.Label(new_document, text="Amount:", font=(FONT, 15))
    item_amount.grid(row=1,column=0, pady=10)

    item_date = tk.Label(new_document, text="Date:", font=(FONT, 15))
    item_date.grid(row=2,column=0, pady=10)

    item_category = tk.Label(new_document, text="Category:", font=(FONT, 15))
    item_category.grid(row=3,column=0, pady=10)

    name_text = tk.Entry(new_document)
    name_text.grid(row=0,column=1,pady=10, columnspan=2)

    amount_text = tk.Entry(new_document)
    amount_text.grid(row=1,column=1,pady=10,columnspan=2)

    today = datetime.date.today()
    date_text = tk.Entry(new_document)
    date_text.insert(0,f"{today}")
    date_text.grid(row=2,column=1,pady=10, columnspan=2)

    category_text = tk.Entry(new_document)
    category_text.grid(row=3,column=1,pady=10, columnspan=2)

    enter_button = tk.Button(new_document)
    enter_button.config(text="Enter",font=(FONT,15), command=lambda: enter(name_text, amount_text, date_text, category_text, new_document))
    enter_button.grid(row=4,column=0,columnspan=2,pady=10)

    cancel_button = tk.Button(new_document)
    cancel_button.config(text="Cancel",font=(FONT,15),command=lambda:new_document.destroy())
    cancel_button.grid(row=4,column=1,columnspan=2,pady=10)

def enter(name, amount, date, category, window):
    item_name = name.get()
    item_amount = float(amount.get())
    item_date = date.get()
    item_category = category.get()

    infor = {
        "name": item_name,
        "amount": item_amount,
        "date": item_date,
        "category": item_category
    }
    infor_json = json.dumps(infor, indent=4)

    with open("data.json","w") as file:
        file.write(infor_json)
    name.delete(0, tk.END)
    amount.delete(0,tk.END)
    date.delete(0, tk.END)
    category.delete(0,tk.END)
    

def spending_history():
    pass


if __name__ == "__main__":
    main()
