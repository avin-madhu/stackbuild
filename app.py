from avin_build_tools import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import *


# basic GUI setup
# root = tk.Tk()
root = ctk.CTk()
root.title("Stackbuild")
root.geometry("600x500")
icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'appicon.ico')
appicon = root.iconbitmap(icon_path)
set_appearance_mode("light")


tabControl = ttk.Notebook(root)

# different switchable tabs for easy navigation and organisation

# Frontend Tab
frontend_tab = ttk.Frame(tabControl)
tabControl.add(frontend_tab, text='Frontend')

# Backend Tab
backend_tab = ttk.Frame(tabControl)
tabControl.add(backend_tab, text='Backend')

# Fullstack Tab
fullstack_tab = ttk.Frame(tabControl)
tabControl.add(fullstack_tab, text='New Setup')


# Add a logging window to show progress
log_frame = ttk.LabelFrame(root, text="Setup Log", padding=(10, 10))
log_frame.pack(fill='both', expand=True, padx=10, pady=10)
log_widget = tk.Text(log_frame, wrap='word', height=10)
log_widget.pack(fill='both', expand=True)


# Frontend Tab Buttons (React, Next.js)
react_button = ctk.CTkButton(master=frontend_tab, corner_radius=32, text="Create React App", command=lambda: create_react_app(log_widget))
react_button.pack(pady=10)

next_button = ctk.CTkButton(master=frontend_tab, corner_radius=32, text="Create Next.js App", command=lambda: create_next_app(log_widget))
next_button.pack(pady=10)

Vue_button = ctk.CTkButton(master=frontend_tab, corner_radius=32, text="Create Vue App", command=lambda: create_vue_app(log_widget))
Vue_button.pack(pady=10)

# Backend Tab Buttons (Django, others)
django_button = ctk.CTkButton(master=backend_tab, corner_radius=32, text="Create Django Project", command=lambda: create_django_app(log_widget))
django_button.pack(pady=10)

# Fullstack Tab Placeholder (can add more setups here)
new_setup_button = ctk.CTkButton(master=fullstack_tab, corner_radius=32, text="Add New Setup", command=add_new_setup)
new_setup_button.pack(pady=10)

# Pack and show the tabs
tabControl.pack(expand=1, fill="both")

# Start the main loop of the GUI
root.mainloop()

