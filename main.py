import tkinter as tk
from tkinter import messagebox
import socket

def dns_lookup():
    domain_name = domain_entry.get()
    try:
        ip_address = socket.gethostbyname(domain_name)
        result_label.config(text=f"The IP address of {domain_name} is {ip_address}")
    except socket.gaierror:
        result_label.config(text=f"Failed to resolve the domain name: {domain_name}")

# Create main window
root = tk.Tk()
root.title("DNS Lookup")

# Create and place widgets
domain_label = tk.Label(root, text="Enter Domain Name:")
domain_label.grid(row=0, column=0, pady=5)

domain_entry = tk.Entry(root, width=30)
domain_entry.grid(row=0, column=1, pady=5)

lookup_button = tk.Button(root, text="Lookup", command=dns_lookup)
lookup_button.grid(row=1, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
