import tkinter as tk
window = tk.Tk()
window.title("Student Chatbot")
window.geometry("400x500")
entry = tk.Entry(window, width=40, font=("Arial", 11))
entry.pack(pady=10)
Label = tk.Label(window, text="Student Chatbot", font=("Arial", 18, "bold"))
Label.pack(pady=20)
result = tk.Label(window, text="", wraplength=350)
result.pack(pady=10)
history = tk.Text(window, height=12, width=45, font=("Arial", 10))
history.pack(pady=10)
def send():
    question = entry.get().lower()
    if question == "fees":
        result.config(text="College fees is Rs.50,000")
    elif question == "hostel":
        result.config(text="Hostel fees is 70,000")
    elif question =="attendance":
        result.config(text="Minimum attendance required is 75%.")
    elif question =="library":
        result.config(text="Library timing is 9 AM to 5 PM.")
    elif question =="hod":
        result.config(text="HOD is Dr. Rajesh Kumar.")
    elif question =="principal":
        result.config(text="Principal is Dr. Rakesh Sharma.")
    elif question =="exam":
        result.config(text="Exams will start from December.")
    elif question =="subjects":
        result.config(text="Subjects are Python, AI, DBMS and English.")
    elif question =="canteen":
        result.config(text="Canteen is open from 8 AM to 4 PM.")
    elif question =="placement":
        result.config(text="You can ask about placements.")
    elif question =="holiday":
        result.config(text="Sunday is a holiday.")
    elif question =="wifi":
        result.config(text="College WIFI is available.")
    elif question =="sports":
        result.config(text="College has sports facilities.")
    elif question =="computer lab":
        result.config(text="Computer lab is available for students.")
    elif question =="scholarships":
        result.config(text="Scholarship is available for eligible students.")
    elif question =="dress code":
        result.config(text="Students should wear proper college uniform.")
    elif question =="help":
        result.config(text="You can ask about fees, HOD, hostel, attendance, library, principal, exam and subjects.")
    else:
        result.config(text="Sorry, I don't understand your question.")
    history.insert(tk.END, "You: " + question + "\n")
    history.insert(tk.END, "Bot: " + result.cget("text") + "\n\n")
button = tk.Button(window, text="Send", command=send, width=12, font=("Arial", 10, "bold"))
button.pack(pady=10)
def clear_chat():
    history.delete("1.0", tk.END)
    result.config(text="")
    entry.delete(0, tk.END)
clear_button = tk.Button(window, text="Clear Chat", command=clear_chat, width=12, font=("Arial", 10, "bold"))
clear_button.pack(pady=5)
window.bind("<Return>", lambda event:send())
window.mainloop()
