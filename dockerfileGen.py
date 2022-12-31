# generates a very simple GUI that accepts user input to create a basic dockerfile.
# user input includes both predefined and user generated options
# see the readme for more details
# I built this for fun and it's probably buggy, use at your own risk
# copyright sarah walter

import tkinter as tk

def create_dockerfile():
    # get the values from the input fields
    base_image = base_image_variable.get()
    if base_image == "custom":
        base_image = base_image_entry.get()
    cmd_type = cmd_type_variable.get()
    cmd = cmd_variable.get()
    if cmd == "custom":
        cmd = cmd_entry.get()
    cmd2 = cmd2_variable.get()
    if cmd2 == "custom":
        cmd2 = cmd2_entry.get()
    cmd3 = cmd3_variable.get()
    if cmd3 == "custom":
        cmd3 = cmd3_entry.get()
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
    cmd_list = []
    if cmd:  # if cmd is not empty or None
        cmd_list.append(cmd)
    if cmd2:  # if cmd2 is not empty or None
        cmd_list.append(cmd2)
    if cmd3:  # if cmd3 is not empty or None
        cmd_list.append(cmd3)
    # condition the formatting on the user's CMD type selection
    if cmd_type == "SHELL":
        dockerfile += f"CMD {' '.join(cmd_list)}\n"
    else:
        dockerfile += f'CMD ["' + '","'.join(cmd_list) + '"]\n'
    dockerfile += f"EXPOSE {port}\n"
    dockerfile += f'VOLUME ["{volume}"]\n'
    dockerfile += f"ENV {env_var}\n"
    dockerfile += f"WORKDIR {workdir}\n"

    # write the Dockerfile to a file
    with open("Dockerfile", "w") as f:
        f.write(dockerfile)

# create the GUI window
window = tk.Tk()
window.title("Sarah's Dockerfile Wizard")
window.geometry("1024x768+100+100")  # set the dimensions of the window

# create the input fields
# base image
base_image_label = tk.Label(text="Base Image:")
base_image_variable = tk.StringVar(window)
base_image_dropdown = tk.OptionMenu(window, base_image_variable, "alpine", "ubuntu", "debian", "custom")
base_image_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
base_image_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
base_image_entry = tk.Entry(state="disabled")
base_image_variable.trace("w", lambda *args: base_image_entry.config(state="normal" if base_image_variable.get() == "custom" else "disabled"))

# CMD type
cmd_type_label = tk.Label(text="CMD Type:")
cmd_type_variable = tk.StringVar(window)
cmd_type_dropdown = tk.OptionMenu(window, cmd_type_variable, "SHELL", "exec")
cmd_type_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
cmd_type_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
cmd_type_variable.trace("w", lambda *args: update_cmd_defaults())

# CMD
cmd_label = tk.Label(text="CMD 1:")
cmd_variable = tk.StringVar(window)
cmd_dropdown = tk.OptionMenu(window, cmd_variable, "bash", "sh", "custom")
cmd_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
cmd_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
cmd_entry = tk.Entry(state="disabled")
cmd_variable.trace("w", lambda *args: cmd_entry.config(state="normal" if cmd_variable.get() == "custom" else "disabled"))

# CMD 2
cmd2_label = tk.Label(text="CMD 2:")
cmd2_variable = tk.StringVar(window)
cmd2_dropdown = tk.OptionMenu(window, cmd2_variable, "bash", "sh", "custom")
cmd2_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
cmd2_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
cmd2_entry = tk.Entry(state="disabled")
cmd2_variable.trace("w", lambda *args: cmd2_entry.config(state="normal" if cmd2_variable.get() == "custom" else "disabled"))

# CMD 3
cmd3_label = tk.Label(text="CMD 3:")
cmd3_variable = tk.StringVar(window)
cmd3_dropdown = tk.OptionMenu(window, cmd3_variable, "bash", "sh", "custom")
cmd3_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
cmd3_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
cmd3_entry = tk.Entry(state="disabled")
cmd3_variable.trace("w", lambda *args: cmd3_entry.config(state="normal" if cmd3_variable.get() == "custom" else "disabled"))

# port
port_label = tk.Label(text="Port:")
port_variable = tk.StringVar(window)
port_dropdown = tk.OptionMenu(window, port_variable, "80", "443", "8080", "custom")
port_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
port_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
port_entry = tk.Entry(state="disabled")
port_variable.trace("w", lambda *args: port_entry.config(state="normal" if port_variable.get() == "custom" else "disabled"))

# select volume - set s some image metadata to say a directory inside the image is a volume
volume_label = tk.Label(text="Volume:")
volume_variable = tk.StringVar(window)
volume_dropdown = tk.OptionMenu(window, volume_variable, "/app/data", "/var/lib/docker/volumes/", "/app/logs", "custom")
volume_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
volume_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
volume_entry = tk.Entry(state="disabled")
volume_variable.trace("w", lambda *args: volume_entry.config(state="normal" if volume_variable.get() == "custom" else "disabled"))

# env var
env_var_label = tk.Label(text="Environment Variable:")
env_var_variable = tk.StringVar(window)
env_var_dropdown = tk.OptionMenu(window, env_var_variable, "NODE_ENV=production", "APP_DEBUG=true", "custom")
env_var_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
env_var_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
env_var_entry = tk.Entry(state="disabled")
env_var_variable.trace("w", lambda *args: env_var_entry.config(state="normal" if env_var_variable.get() == "custom" else "disabled"))

# workdir
workdir_label = tk.Label(text="Working Directory:")
workdir_variable = tk.StringVar(window)
workdir_dropdown = tk.OptionMenu(window, workdir_variable, "/desktop", "/app/src", "/app/bin", "custom")
workdir_dropdown.config(bg="#fff", fg="#333", padx=10, pady=5)
workdir_dropdown["menu"].config(font=("Arial", 14), bg="#fff", fg="#333")
workdir_entry = tk.Entry(state="disabled")
workdir_variable.trace("w", lambda *args: workdir_entry.config(state="normal" if workdir_variable.get() == "custom" else "disabled"))

# create Dockerfile button
create_button = tk.Button(text="Create Dockerfile", command=create_dockerfile)
create_button.config(bg="#333", fg="#fff", font=("Arial", 14), padx=20, pady=10)

# layout the input field s and button
base_image_label.pack()
base_image_dropdown.pack()
base_image_entry.pack()
cmd_type_label.pack()
cmd_type_dropdown.pack()
cmd_label.pack()
cmd_dropdown.pack()
cmd_entry.pack()
cmd2_label.pack()
cmd2_dropdown.pack()
cmd2_entry.pack()
cmd3_label.pack()
cmd3_dropdown.pack()
cmd3_entry.pack()
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

window.mainloop()


