def write_student_data():
    with open("report.txt", "a") as file:
        while True:
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            marks = input("Enter marks (out of 100): ")

            # Store entry in the specified format
            file.write(f"Name: {name}, Subject: {subject}, Marks: {marks}\n")

            cont = input("Do you want to add another entry? (y/n): ").strip().lower()
            if cont != "yes":
                break


def read_and_display_data():
    try:
        with open("report.txt", "r") as file:
            lines = file.readlines()

            total_students = len(lines)
            total_marks = 0

            print("\n--- All Entries ---")
            for line in lines:
                print(line.strip())
                parts = line.strip().split(", ")
                for part in parts:
                    if "Marks" in part:
                        mark = int(part.split(":")[1].strip())
                        total_marks += mark

            average_marks = total_marks / total_students if total_students > 0 else 0

            print("\nTotal number of students:", total_students)
            print("Average marks:", round(average_marks, 2))
    except FileNotFoundError:
        print("No report.txt file found. Please add student data first.")


# Main menu
while True:
    print("\n--- Student Report Menu ---")
    print("1. Add student data")
    print("2. Display report")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        write_student_data()
    elif choice == "2":
        read_and_display_data()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
1
