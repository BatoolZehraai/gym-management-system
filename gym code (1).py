import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "GYM"
}

def connect_db():
    return mysql.connector.connect(**db_config)

class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

# Inheritance
class Person:
    def __init__(self, nam, num, id, join_date):
        self.nam, self.num, self.id, self.join_date = nam, num, id, join_date

    def display_info(self):
        print(f"Name: {self.nam}, ID: {self.id}, Cell: {self.num}, Joined: {self.join_date}")

# Inheritance
class Customer(Person):
    def __init__(self, nam, num, id, join_date, fee):
        super().__init__(nam, num, id, join_date)
        self.fee = fee

    def display(self):
        self.display_info()
        print(f"Fee: {self.fee}")

# Inheritance
class Trainer(Person):
    def __init__(self, nam, num, id, join_date, salary):
        super().__init__(nam, num, id, join_date)
        self.salary = salary

    def display(self):
        self.display_info()
        print(f"Salary: {self.salary}")

# Abstraction
class Equipment:
    def __init__(self, nam, dmg):
        self.nam, self.dmg = nam, dmg

    def display(self):
        print(f"Equipment Name: {self.nam}, Damaged: {self.dmg}")

# Abstraction
class Membership:
    def __init__(self, typ, perks, dur, cost):
        self.typ, self.perks, self.dur, self.cost = typ, perks, dur, cost

    def display(self):
        print(f"Type: {self.typ}, Perks: {self.perks}, Duration: {self.dur}, Cost: {self.cost}")

# Abstraction
class Payment:
    def __init__(self, pay_id, cust_id, amt, due_date):
        self.pay_id, self.cust_id, self.amt, self.due_date = pay_id, cust_id, amt, due_date

    def display(self):
        print(f"Payment ID: {self.pay_id}, Customer ID: {self.cust_id}, Amount: {self.amt}, Due Date: {self.due_date}")

# Encapsulation
class GymManager:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def add_customer(self, customer):
        query = "INSERT INTO customers (id, name, cell_number, id_number, join_date, fee) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (customer.id, customer.nam, customer.num, customer.id, customer.join_date, customer.fee))
        self.conn.commit()

    def add_trainer(self, trainer):
        query = "INSERT INTO trainers (id, name, cell_number, id_number, join_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (trainer.id, trainer.nam, trainer.num, trainer.id, trainer.join_date, trainer.salary))
        self.conn.commit()

    def add_equipment(self, equipment):
        query = "INSERT INTO equipment (id, name, damaged) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (equipment.id, equipment.nam, equipment.dmg))
        self.conn.commit()

    def get_customers(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_trainers(self):
        query = "SELECT * FROM trainers"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_equipments(self):
        query = "SELECT * FROM equipment"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_memberships(self):
        query = "SELECT * FROM membership"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_payments(self):
        query = "SELECT * FROM payments"
        self.cursor.execute(query)
        return self.cursor.fetchall()

# GUI
class GymManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.gym_manager = GymManager()

        self.main_menu()

    def main_menu(self):
        tk.Label(self.root, text="Gym Management System", font=('Helvetica', 18, 'bold')).pack(pady=20)

        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def register(self):
        self.clear_window()
        self.root.title("Register")

        tk.Label(self.root, text="Register", font=('Helvetica', 18, 'bold')).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show='*')
        password_entry.pack()

        tk.Button(self.root, text="Register", command=lambda: self.save_user(username_entry.get(), password_entry.get())).pack(pady=10)

    def save_user(self, username, password):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User registered successfully")
        self.main_menu()

    def login(self):
        self.clear_window()
        self.root.title("Login")

        tk.Label(self.root, text="Login", font=('Helvetica', 18, 'bold')).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show='*')
        password_entry.pack()

        tk.Button(self.root, text="Login", command=lambda: self.authenticate_user(username_entry.get(), password_entry.get())).pack(pady=10)

    def authenticate_user(self, username, password):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            messagebox.showinfo("Success", "Login successful")
            self.manage_gym()
        else:
            messagebox.showerror("Error", "Invalid username or password")
            self.main_menu()

    def manage_gym(self):
        self.clear_window()
        self.root.title("Gym Management System")

        tk.Label(self.root, text="Gym Management System", font=('Helvetica', 18, 'bold')).pack(pady=20)

        tk.Button(self.root, text="Add Customer", command=self.add_customer).pack(pady=10)
        tk.Button(self.root, text="Add Trainer", command=self.add_trainer).pack(pady=10)
        tk.Button(self.root, text="Add Equipment", command=self.add_equipment).pack(pady=10)
        tk.Button(self.root, text="Show Customers", command=self.show_customers).pack(pady=10)
        tk.Button(self.root, text="Show Trainers", command=self.show_trainers).pack(pady=10)
        tk.Button(self.root, text="Show Equipments", command=self.show_equipments).pack(pady=10)
        tk.Button(self.root, text="Show Memberships", command=self.show_memberships).pack(pady=10)
        tk.Button(self.root, text="Show Payments", command=self.show_payments).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.main_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_customer(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Customer")

        tk.Label(self.new_window, text="Name:").pack()
        nam_entry = tk.Entry(self.new_window)
        nam_entry.pack()

        tk.Label(self.new_window, text="Cell Number:").pack()
        num_entry = tk.Entry(self.new_window)
        num_entry.pack()

        tk.Label(self.new_window, text="ID:").pack()
        id_entry = tk.Entry(self.new_window)
        id_entry.pack()

        tk.Label(self.new_window, text="Join Date (YYYY-MM-DD):").pack()
        join_date_entry = tk.Entry(self.new_window)
        join_date_entry.pack()

        tk.Label(self.new_window, text="Fee:").pack()
        fee_entry = tk.Entry(self.new_window)
        fee_entry.pack()

        tk.Button(self.new_window, text="Add", command=lambda: self.save_customer(nam_entry.get(), num_entry.get(), id_entry.get(), join_date_entry.get(), fee_entry.get())).pack()

    def save_customer(self, nam, num, id, join_date, fee):
        join_date = datetime.strptime(join_date, "%Y-%m-%d").date()
        customer = Customer(nam, num, id, join_date, float(fee))
        self.gym_manager.add_customer(customer)
        messagebox.showinfo("Success", "Customer added successfully")

    def add_trainer(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Trainer")

        tk.Label(self.new_window, text="Name:").pack()
        nam_entry = tk.Entry(self.new_window)
        nam_entry.pack()

        tk.Label(self.new_window, text="Cell Number:").pack()
        num_entry = tk.Entry(self.new_window)
        num_entry.pack()

        tk.Label(self.new_window, text="ID:").pack()
        id_entry = tk.Entry(self.new_window)
        id_entry.pack()

        tk.Label(self.new_window, text="Join Date (YYYY-MM-DD):").pack()
        join_date_entry = tk.Entry(self.new_window)
        join_date_entry.pack()

        tk.Label(self.new_window, text="Salary:").pack()
        salary_entry = tk.Entry(self.new_window)
        salary_entry.pack()

        tk.Button(self.new_window, text="Add", command=lambda: self.save_trainer(nam_entry.get(), num_entry.get(), id_entry.get(), join_date_entry.get(), salary_entry.get())).pack()

    def save_trainer(self, nam, num, id, join_date, salary):
        join_date = datetime.strptime(join_date, "%Y-%m-%d").date()
        trainer = Trainer(nam, num, id, join_date, float(salary))
        self.gym_manager.add_trainer(trainer)
        messagebox.showinfo("Success", "Trainer added successfully")

    def add_equipment(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Equipment")

        tk.Label(self.new_window, text="Equipment Name:").pack()
        nam_entry = tk.Entry(self.new_window)
        nam_entry.pack()

        tk.Label(self.new_window, text="Damaged (Yes/No):").pack()
        dmg_entry = tk.Entry(self.new_window)
        dmg_entry.pack()

        tk.Button(self.new_window, text="Add", command=lambda: self.save_equipment(nam_entry.get(), dmg_entry.get())).pack()

    def save_equipment(self, nam, dmg):
        dmg = True if dmg.lower() == 'yes' else False
        equipment = Equipment(nam, dmg)
        self.gym_manager.add_equipment(equipment)
        messagebox.showinfo("Success", "Equipment added successfully")

    def show_customers(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Customers")

        columns = ('ID', 'Name', 'Cell Number', 'ID Number', 'Join Date', 'Fee')
        tree = ttk.Treeview(self.new_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        customers = self.gym_manager.get_customers()
        for customer in customers:
            tree.insert('', tk.END, values=customer)

        tree.pack()

    def show_trainers(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Trainers")

        columns = ('ID', 'Name', 'Cell Number', 'ID Number', 'Join Date', 'Salary')
        tree = ttk.Treeview(self.new_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        trainers = self.gym_manager.get_trainers()
        for trainer in trainers:
            tree.insert('', tk.END, values=trainer)

        tree.pack()

    def show_equipments(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Equipments")

        columns = ('ID', 'Name', 'Damaged')
        tree = ttk.Treeview(self.new_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        equipments = self.gym_manager.get_equipments()
        for equipment in equipments:
            tree.insert('', tk.END, values=equipment)

        tree.pack()

    def show_memberships(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Memberships")

        columns = ('ID', 'Type', 'Perks', 'Duration', 'Cost')
        tree = ttk.Treeview(self.new_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        memberships = self.gym_manager.get_memberships()
        for membership in memberships:
            tree.insert('', tk.END, values=membership)

        tree.pack()

    def show_payments(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Payments")

        columns = ('ID', 'Customer ID', 'Payment ID', 'Amount', 'Due Date')
        tree = ttk.Treeview(self.new_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)

        payments = self.gym_manager.get_payments()
        for payment in payments:
            tree.insert('', tk.END, values=payment)

        tree.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementApp(root)
    root.mainloop()