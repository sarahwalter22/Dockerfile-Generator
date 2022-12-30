import tkinter as tk

def create_dockerfile():
    # get the values from the input fields
    base_image = base_image_variable.get()
    if base_image == "custom":
        base_image = base_image_entry.get()
    cmd = cmd_variable.get()
    if cmd == "custom":
        cmd = cmd_entry.get()
    port = port_variable.get()
    if port == "custom":
        port = port_entry.get()
    volume = volume_variable.get()
    if volume == "custom":
        volume = volume_entry.get()
    env_var = env_var_variable.get()
    if env_var == "custom":
        env_var = env_var_entry.get()
    workdir = workdir_variable.get()
    if workdir == "custom":
        workdir = workdir_entry.get()

    # create the Dockerfile
    dockerfile = f"FROM {base_image}\n"
    dockerfile += f"CMD {cmd}\n"
    dockerfile += f"EXPOSE {port}\n"
    dockerfile += f"VOLUME {volume}\n"
    dockerfile += f"ENV {env_var}\n"
    dockerfile += f"WORKDIR {workdir}\n"

    # write the Dockerfile to a file
    with open("Dockerfile", "w") as f:
        f.write(dockerfile)

# create the GUI window
window = tk.Tk()
window.title("Create Dockerfile")

# create the input fields
base_image_label = tk.Label(text="Base image:")
base_image_variable = tk.StringVar(window)
base_image_dropdown = tk.OptionMenu(window, base_image_variable, "alpine", "ubuntu", "debian", "custom")
base_image_entry = tk.Entry(state="disabled")
base_image_variable.trace("w", lambda *args: base_image_entry.config(state="normal" if base_image_variable.get() == "custom" else "disabled"))
cmd_label = tk.Label(text="CMD:")
cmd_variable = tk.StringVar(window)
cmd_dropdown = tk.OptionMenu(window, cmd_variable, "bash", "sh", "custom")
cmd_entry = tk.Entry(state="disabled")
cmd_variable.trace("w", lambda *args: cmd_entry.config(state="normal" if cmd_variable.get() == "custom" else "disabled"))
port_label = tk.Label(text="Exposed port:")
port_variable = tk.StringVar(window)
port_dropdown = tk.OptionMenu(window, port_variable, "80", "443", "8080", "custom")
port_entry = tk.Entry(state="disabled")
port_variable.trace("w", lambda *args: port_entry.config(state="normal" if port_variable.get() == "custom" else "disabled"))
volume_label = tk.Label(text="Volume:")
volume_variable = tk.StringVar(window)
volume_dropdown = tk.OptionMenu(window, volume_variable, "/var/www/html", "/var/log", "/app/data", "custom")
volume_entry = tk.Entry(state="disabled")
volume_variable.trace("w", lambda *args: volume_entry.config(state="normal" if volume_variable.get() == "custom" else "disabled"))
env_var_label = tk.Label(text="Environment variable:")
env_var_variable = tk.StringVar(window)
env_var_dropdown = tk.OptionMenu(window, env_var_variable, "FOO=bar", "BAR=foo", "custom")
env_var_entry = tk.Entry(state="disabled")
env_var_variable.trace("w", lambda *args: env_var_entry.config(state="normal" if env_var_variable.get() == "custom" else "disabled"))
workdir_label = tk.Label(text="Working directory:")
workdir_variable = tk.StringVar(window)
workdir_dropdown = tk.OptionMenu(window, workdir_variable, "/app", "/desktop", "/usr/local/bin", "custom")
workdir_entry = tk.Entry(state="disabled")
workdir_variable.trace("w", lambda *args: workdir_entry.config(state="normal" if workdir_variable.get() == "custom" else "disabled"))


# create the "Create Dockerfile" button
create_button = tk.Button(text="Create Dockerfile", command=create_dockerfile)

# trying to use a grid based layout to organize the input fields and dropdown menus
base_image_label.grid(row=0, column=0)
base_image_dropdown.grid(row=0, column=1)
base_image_entry.grid(row=0, column=2)
cmd_label.grid(row=1, column=0)
cmd_dropdown.grid(row=1, column=1)
cmd_entry.grid(row=1, column=2)
port_label.grid(row=2, column=0)
port_dropdown.grid(row=2, column=1)
port_entry.grid(row=2, column=2)
volume_label.grid(row=3, column=0)
volume_dropdown.grid(row=3, column=1)
volume_entry.grid(row=3, column=2)
env_var_label.grid(row=4, column=0)
env_var_dropdown.grid(row=4, column=1)
env_var_entry.grid(row=4, column=2)
workdir_label.grid(row=5, column=0)
workdir_dropdown.grid(row=5, column=1)
workdir_entry.grid(row=5, column=2)
create_button.grid(row=6, column=1)

# start the GUI event loop
window.mainloop()

