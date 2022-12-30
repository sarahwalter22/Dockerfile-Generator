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

# layout the input fields and button in the GUI window
base_image_label.pack()
base_image_dropdown.pack()
base_image_entry.pack()
cmd_label.pack()
cmd_dropdown.pack()
cmd_entry.pack()
port_label.pack()
port_dropdown.pack()
port_entry.pack()
volume_label.pack()
volume_dropdown.pack()
volume_entry.pack()
env_var_label.pack()
env_var_dropdown.pack()
env_var_entry.pack()
workdir_label.pack()
workdir_dropdown.pack()
workdir_entry.pack()
create_button.pack()

# start the GUI event loop
window.mainloop()

