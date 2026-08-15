import tkinter as tk

# =========================
# Main Window
# =========================
window = tk.Tk()
window.title("Student Chatbot")
window.geometry("520x700")
window.configure(bg="#eef3f8")
window.resizable(False, False)


# =========================
# Colors
# =========================
BG_COLOR = "#eef3f8"
HEADER_COLOR = "#2563eb"
HEADER_DARK = "#1d4ed8"
TEXT_COLOR = "#1f2937"
SECONDARY_TEXT = "#64748b"
WHITE = "#ffffff"
INPUT_BG = "#ffffff"
BORDER_COLOR = "#d9e2ec"
SEND_COLOR = "#2563eb"
SEND_HOVER = "#1d4ed8"
CLEAR_COLOR = "#ef4444"
CLEAR_HOVER = "#dc2626"


# =========================
# Header
# =========================
header = tk.Frame(
    window,
    bg=HEADER_COLOR,
    height=105
)
header.pack(fill="x")
header.pack_propagate(False)

title = tk.Label(
    header,
    text="Student Chatbot",
    font=("Arial", 24, "bold"),
    fg=WHITE,
    bg=HEADER_COLOR
)
title.pack(pady=(20, 2))

subtitle = tk.Label(
    header,
    text="Your college information assistant",
    font=("Arial", 10),
    fg="#dbeafe",
    bg=HEADER_COLOR
)
subtitle.pack()


# =========================
# Main Content
# =========================
main_frame = tk.Frame(
    window,
    bg=BG_COLOR
)
main_frame.pack(fill="both", expand=True, padx=28)


# =========================
# Input Label
# =========================
input_label = tk.Label(
    main_frame,
    text="Enter your question",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
input_label.pack(anchor="w", pady=(20, 7))


# =========================
# Rounded Input Container
# =========================
input_container = tk.Frame(
    main_frame,
    bg=INPUT_BG,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)
input_container.pack(fill="x")

entry = tk.Entry(
    input_container,
    font=("Arial", 12),
    bg=INPUT_BG,
    fg=TEXT_COLOR,
    relief="flat",
    bd=0,
    insertbackground=HEADER_COLOR
)
entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(15, 8),
    pady=12
)


# =========================
# Send Button
# =========================
def send():
    question = entry.get().lower()

    if question == "fees":
        result.config(text="College fees is Rs.50,000")
    elif question == "hostel":
        result.config(text="Hostel fees is 70,000")
    elif question == "attendance":
        result.config(text="Minimum attendance required is 75%.")
    elif question == "library":
        result.config(text="Library timing is 9 AM to 5 PM.")
    elif question == "hod":
        result.config(text="HOD is Dr. Rajesh Kumar.")
    elif question == "principal":
        result.config(text="Principal is Dr. Rakesh Sharma.")
    elif question == "exam":
        result.config(text="Exams will start from December.")
    elif question == "subjects":
        result.config(text="Subjects are Python, AI, DBMS and English.")
    elif question == "canteen":
        result.config(text="Canteen is open from 8 AM to 4 PM.")
    elif question == "placement":
        result.config(text="You can ask about placements.")
    elif question == "holiday":
        result.config(text="Sunday is a holiday.")
    elif question == "wifi":
        result.config(text="College WIFI is available.")
    elif question == "sports":
        result.config(text="College has sports facilities.")
    elif question == "computer lab":
        result.config(text="Computer lab is available for students.")
    elif question == "scholarships":
        result.config(text="Scholarship is available for eligible students.")
    elif question == "dress code":
        result.config(text="Students should wear proper college uniform.")
    elif question == "help":
        result.config(
            text="You can ask about fees, HOD, hostel, attendance, "
                 "library, principal, exam and subjects."
        )
    else:
        result.config(text="Sorry, I don't understand your question.")

    history.insert(tk.END, "You: " + question + "\n")
    history.insert(tk.END, "Bot: " + result.cget("text") + "\n\n")
    history.see(tk.END)


send_button = tk.Button(
    input_container,
    text="Send",
    command=send,
    font=("Arial", 10, "bold"),
    bg=SEND_COLOR,
    fg=WHITE,
    activebackground=SEND_HOVER,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    padx=18,
    pady=7,
    cursor="hand2"
)
send_button.pack(side="right", padx=(0, 7), pady=6)


# =========================
# Helper Text
# =========================
helper = tk.Label(
    main_frame,
    text="Try: fees, hostel, attendance, library, HOD, principal",
    font=("Arial", 9),
    bg=BG_COLOR,
    fg=SECONDARY_TEXT
)
helper.pack(anchor="w", pady=(6, 0))


# =========================
# Output Label
# =========================
output_label = tk.Label(
    main_frame,
    text="Chatbot Response",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
output_label.pack(anchor="w", pady=(18, 7))


# =========================
# Output Card
# =========================
result_frame = tk.Frame(
    main_frame,
    bg=WHITE,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)
result_frame.pack(fill="x")

result = tk.Label(
    result_frame,
    text="Your chatbot response will appear here.",
    wraplength=420,
    font=("Arial", 11),
    bg=WHITE,
    fg=TEXT_COLOR,
    justify="left",
    anchor="w"
)
result.pack(
    fill="x",
    padx=16,
    pady=15
)


# =========================
# Chat History Label
# =========================
history_title = tk.Label(
    main_frame,
    text="Chat History",
    font=("Arial", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
history_title.pack(anchor="w", pady=(18, 7))


# =========================
# Chat History Container
# =========================
history_frame = tk.Frame(
    main_frame,
    bg=WHITE,
    highlightbackground=BORDER_COLOR,
    highlightthickness=1
)
history_frame.pack(fill="both", expand=True)


history = tk.Text(
    history_frame,
    height=11,
    font=("Arial", 10),
    bg=WHITE,
    fg="#374151",
    relief="flat",
    bd=0,
    wrap="word",
    padx=12,
    pady=10,
    spacing1=2,
    spacing3=4
)
history.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================
# Scrollbar
# =========================
scrollbar = tk.Scrollbar(
    history_frame,
    command=history.yview,
    bg="#cbd5e1",
    activebackground="#94a3b8",
    relief="flat",
    bd=0
)
scrollbar.pack(
    side="right",
    fill="y"
)

history.config(
    yscrollcommand=scrollbar.set
)


# =========================
# Clear Chat Function
# =========================
def clear_chat():
    history.delete("1.0", tk.END)
    result.config(text="Your chatbot response will appear here.")
    entry.delete(0, tk.END)
    entry.focus()


# =========================
# Clear Button Area
# =========================
button_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR
)
button_frame.pack(pady=14)


clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    command=clear_chat,
    width=14,
    font=("Arial", 10, "bold"),
    bg=CLEAR_COLOR,
    fg=WHITE,
    activebackground=CLEAR_HOVER,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    padx=10,
    pady=7,
    cursor="hand2"
)
clear_button.pack()


# =========================
# Hover Effects
# =========================
def send_enter(event):
    send_button.config(bg=SEND_HOVER)


def send_leave(event):
    send_button.config(bg=SEND_COLOR)


def clear_enter(event):
    clear_button.config(bg=CLEAR_HOVER)


def clear_leave(event):
    clear_button.config(bg=CLEAR_COLOR)


send_button.bind("<Enter>", send_enter)
send_button.bind("<Leave>", send_leave)

clear_button.bind("<Enter>", clear_enter)
clear_button.bind("<Leave>", clear_leave)


# =========================
# Enter Key
# =========================
window.bind("<Return>", lambda event: send())

entry.focus()

window.mainloop()

