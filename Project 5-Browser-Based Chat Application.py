import tkinter as tk

def send_message():
    message = entry.get()

    if message.strip():
        chat_box.insert(tk.END, "You: " + message + "\n")
        entry.delete(0, tk.END)

        # Simple bot reply
        chat_box.insert(tk.END, "Bot: Message Received!\n\n")

root = tk.Tk()
root.title("Chat Application")
root.geometry("500x400")

chat_box = tk.Text(root, height=15, width=55)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

root.mainloop()