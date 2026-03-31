# import tkinter as tk
# import os
# import sys

# def open_chat():
#     os.system("python client_GUI.py")

# def open_detection():
#     os.system("python client.py")

# def exit_app():
#     root.destroy()

# root = tk.Tk()
# root.title("Safe Chat – Home")
# root.geometry("500x400")
# root.configure(bg="#0f172a")

# title = tk.Label(
#     root,
#     text="SAFE CHAT",
#     font=("Times New Roman", 24, "bold"),
#     fg="white",
#     bg="#0f172a"
# )
# title.pack(pady=30)

# subtitle = tk.Label(
#     root,
#     text="Cyberbullying Detection System",
#     font=("Times New Roman", 14),
#     fg="#38bdf8",
#     bg="#0f172a"
# )
# subtitle.pack(pady=10)

# btn_style = {
#     "font": ("Times New Roman", 14),
#     "width": 22,
#     "height": 2
# }

# tk.Button(root, text="Start Chat", command=open_chat, **btn_style).pack(pady=10)
# tk.Button(root, text="Detect Cyberbullying", command=open_detection, **btn_style).pack(pady=10)
# tk.Button(root, text="Exit", command=exit_app, **btn_style).pack(pady=20)

# root.mainloop()
# import tkinter as tk
# from PIL import Image, ImageTk
# import os

# # ---------- FUNCTIONS ----------
# def open_chat():
#     os.system("python client_GUI.py")

# def open_detection():
#     os.system("python client.py")

# def exit_app():
#     root.destroy()

# # ---------- ROOT WINDOW ----------
# root = tk.Tk()
# root.title("Safe Chat | Home")
# root.geometry("900x600")
# root.configure(bg="#020617")

# # ---------- HEADER ----------
# header = tk.Frame(root, bg="#020617")
# header.pack(fill="x", pady=10)

# logo_img = Image.open("assets/logo.png").resize((80, 80))
# logo = ImageTk.PhotoImage(logo_img)

# tk.Label(header, image=logo, bg="#020617").pack(side="left", padx=20)

# tk.Label(
#     header,
#     text="SAFE CHAT",
#     font=("Times New Roman", 28, "bold"),
#     fg="#38bdf8",
#     bg="#020617"
# ).pack(side="left")

# # ---------- MAIN CONTENT ----------
# content = tk.Frame(root, bg="#020617")
# content.pack(expand=True, fill="both", padx=40)

# # Left Info Panel
# left = tk.Frame(content, bg="#020617")
# left.pack(side="left", expand=True, fill="both")

# tk.Label(
#     left,
#     text="Cyberbullying Detection System",
#     font=("Times New Roman", 20, "bold"),
#     fg="white",
#     bg="#020617"
# ).pack(anchor="w", pady=10)

# tk.Label(
#     left,
#     text=(
#         "Safe Chat is an intelligent system that detects\n"
#         "cyberbullying messages using Machine Learning.\n\n"
#         "✔ Real-time chat monitoring\n"
#         "✔ Secure communication\n"
#         "✔ AI-based abuse detection"
#     ),
#     font=("Times New Roman", 14),
#     fg="#cbd5f5",
#     bg="#020617",
#     justify="left"
# ).pack(anchor="w", pady=10)

# # Right Button Panel
# right = tk.Frame(content, bg="#020617")
# right.pack(side="right", padx=40)

# btn_style = {
#     "font": ("Times New Roman", 14, "bold"),
#     "width": 22,
#     "height": 2,
#     "bg": "#1e293b",
#     "fg": "white",
#     "activebackground": "#38bdf8",
#     "activeforeground": "#020617",
#     "bd": 0
# }

# tk.Button(right, text="🚀 Start Secure Chat", command=open_chat, **btn_style).pack(pady=15)
# tk.Button(right, text="🔍 Detect Cyberbullying", command=open_detection, **btn_style).pack(pady=15)
# tk.Button(right, text="❌ Exit", command=exit_app, **btn_style).pack(pady=30)

# # ---------- FOOTER ----------
# tk.Label(
#     root,
#     text="Developed as part of Cyber Security Project | M.Tech",
#     font=("Times New Roman", 11),
#     fg="#64748b",
#     bg="#020617"
# ).pack(pady=10)

# root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
import os

# ================= FUNCTIONS =================
def open_chat():
    os.system("python client_GUI.py")

def open_detection():
    os.system("python client.py")

def exit_app():
    root.destroy()

# ================= ROOT WINDOW =================
root = tk.Tk()
root.title("Safe Chat | Home")
root.geometry("900x600")
root.resizable(False, False)

# ================= BACKGROUND IMAGE =================
bg_img = Image.open("assets/background.png").resize((900, 600))
bg = ImageTk.PhotoImage(bg_img)

bg_label = tk.Label(root, image=bg)
bg_label.image = bg
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================= BANNER IMAGE =================

# ================= DARK BLUE OVERLAY PANEL =================
overlay = tk.Frame(
    root,
    bg="#020617",
    highlightbackground="#1E293B",
    highlightthickness=1
)
overlay.place(x=40, y=180, width=820, height=350)

# ================= LEFT CONTENT =================
left = tk.Frame(overlay, bg="#020617")
left.pack(side="left", fill="both", expand=True, padx=25, pady=25)

tk.Label(
    left,
    text="Cyberbullying Detection System",
    font=("Times New Roman", 22, "bold"),
    fg="#38BDF8",
    bg="#020617"
).pack(anchor="w", pady=(0, 12))

tk.Label(
    left,
    text=(
        "Safe Chat is an AI-powered cyber security system designed\n"
        "to detect, monitor, and prevent cyberbullying behavior\n"
        "in real-time online communication.\n\n"
        "✔ Real-time chat monitoring using Machine Learning\n"
        "✔ Secure and reliable communication\n"
        "✔ AI-based abusive content detection\n"
        "✔ Multi-language support (English, Hinglish, Kannada)\n"
        "✔ Suitable for social platforms and education systems"
    ),
    font=("Times New Roman", 14),
    fg="#CBD5F5",
    bg="#020617",
    justify="left"
).pack(anchor="w")

# ================= RIGHT BUTTONS =================
right = tk.Frame(overlay, bg="#020617")
right.pack(side="right", padx=35, pady=30)

btn_style = {
    "font": ("Times New Roman", 14, "bold"),
    "bg": "#1E293B",
    "fg": "#FFFFFF",
    "activebackground": "#38BDF8",
    "activeforeground": "#020617",
    "width": 22,
    "height": 2,
    "bd": 0,
    "cursor": "hand2"
}

tk.Button(
    right,
    text="🚀 Start Secure Chat",
    command=open_chat,
    **btn_style
).pack(pady=12)

tk.Button(
    right,
    text="🔍 Detect Cyberbullying",
    command=open_detection,
    **btn_style
).pack(pady=12)

tk.Button(
    right,
    text="❌ Exit",
    command=exit_app,
    **btn_style
).pack(pady=22)

# ================= FOOTER =================
tk.Label(
    root,
    text="Developed as part of Cyber Security Project | Safe Chat",
    font=("Times New Roman", 11),
    fg="#94A3B8",
    bg="#020617"
).place(relx=0.5, y=575, anchor="center")

root.mainloop()
