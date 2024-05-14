import tkinter as tk
import keyboard

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        label.config(text=f"Tecla pressionada: {event.name}")

# Configurações da janela
root = tk.Tk()
root.title("Monitor de Teclado")
root.geometry("250x80")

# Configurações do rótulo
label = tk.Label(root, text="Pressione uma tecla")
label.pack(pady=20)

# Conectar o evento de teclado
keyboard.hook(on_key_event)

root.mainloop()
