import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to run commands and create projects
def run_command(command, directory, log_widget):
    try:
        process = subprocess.Popen(command, shell=True, cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                log_widget.insert(tk.END, output.strip().decode() + '\n')
                log_widget.see(tk.END)
        # messagebox.showinfo("Success", f"{' '.join(command)} completed successfully!")
        log_widget.insert(tk.END, "Project setup has been successful !!")
        answer = messagebox.askquestion("Suggestion","Do you want to open with vs code??")
        print(answer)
        if answer == 'yes':
            subprocess.Popen(['code', directory], shell=True)  # Use Popen to launch VS Code
        else:
            log_widget.insert(tk.END, "\nSo, you chose not to open with VS code.")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Sorry, I Failed to create the project: {e}")

def check_system(package, log_widget) -> bool:
    result = subprocess.run([package, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        version = result.stdout.decode().strip()  # Get the output and decode it
        log_widget.insert(tk.END, f"npm is installed. Version: {version}")
        return True
    else:
        return False

# Function to initialize React project
def create_react_app(log_widget):

    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        log_widget.insert(tk.END, "Initializing React project...\n")
        run_command(["npx", "create-react-app", "my-react-app"], directory, log_widget)


# Function to initialize Django project
def create_django_app(log_widget):
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        log_widget.insert(tk.END, "Initializing Django project...\n")
        run_command(["django-admin", "startproject", "my_django_project"], directory, log_widget)

# Function to initialize Next.js project
def create_next_app(log_widget):
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        log_widget.insert(tk.END, "Initializing Next.js project...\n")
        run_command(["npx", "create-next-app", "my-next-app"], directory, log_widget)

def create_vue_app(log_widget):
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        log_widget.insert(tk.END, "Initializing Vue project...\n")
        run_command(["npm", "install", "-g", "@vue/cli"], directory, log_widget)
        run_command(["vue", "create", "my-vue-app"], directory, log_widget)
    

# Function to add new project setups (can be extended)
def add_new_setup():
    # Simple form to add new framework (just as an idea placeholder)
    tk.messagebox.showinfo("Feature Coming Soon", "My creator Avin will be adding setup features!")