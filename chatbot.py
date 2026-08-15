def chatbot():
    while True:
        print("Welcome to student chatbot")
        question = input("Ask your question: ").lower()
        if question == "exit":
            print("Thank you!Goodbye.")
            break
        elif question == "fees":
            print("College fees is Rs50,000.")
        elif question == "hostel":
            print("Hostel fees is Rs70,000.")
        elif question == "attendance":
            print("Minimum attendance required is 75%.")
        elif question == "library":
            print("Library timing is 9 AM to 5 PM.")
        elif question == "hod":
            print("HOD is Dr. Rajesh Kumar.")
        elif question == "principal":
            print("Principal is Dr. Rakesh Sharma.")
        elif question == "exam":
            print("Exams will start from December.")
        elif question == "subjects":
            print("Subjects are Python, AI, DBMS and English.")
        elif question == "canteen":
            print("Canteen is open from 8 AM to 4 PM.")
        elif question == "placement":
            print("Top companies visit every year for placements.")
        elif question == "admission":
            print("Admission process starts in June.")
        elif question == "contact":
            print("College contact number is 0987654321.")
        elif question == "hello":
            print("Hello! How can I help you?")
        elif question == "hi":
            print("Hi! Welcome to our college chatbot.")
        elif question == "bye":
            print("Thank you for using the chatbot. Have a nice day!")
        elif question == "location":
            print("Our college is located in Noida.")
        elif question == "courses":
            print("We offer BTECH, BCA, BBA, MBA and MCA courses.")
        elif question == "website":
            print("Visit our official website: www.college.edu")
        elif question == "timing":
            print("College timing is 9 AM to 5 PM.")
        elif question == "holiday":
            print("Please check the academic calendar for holidays.")
        elif question == "wifi":
            print("College Wifi is available for all students.")
        elif question == "sports":
            print("Sports facilities include Cricket, Football and Badminton.")
        elif question == "computer lab":
            print("Computer lab is open from 9 AM to 5 PM.")
        elif question == "scholarship":
            print("Eligible students can apply for scholarships.")
        elif question == "dress code":
            print("Students should wear proper college uniform.")
        elif question == "help":
            print("You can ask about:")
            print("fees")
            print("hostel")
            print("attendance")
            print("library")
            print("hod")
            print("principal")
            print("exam")
            print("subjects")
            print("canteen")
            print("placement")
            print("admission")
            print("contact")
            print("location")
            print("courses")
            print("website")
            print("timing")
            print("holiday")
            print("wifi")
            print("sports")
            print("computer lab")
            print("scholarship")
            print("dress code")
        else:
            print("Sorry, I don't understand your question.")
chatbot()



