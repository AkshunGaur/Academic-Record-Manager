import ui
from records import StudentRepository


def main():
    repo = StudentRepository()
    ui.welcome()

    while True:
        ui.print_menu()
        choice = ui.get_choice()

        if choice == "1":
            name = input("Enter student name: ").strip()
            marks = ui.get_marks_input(
                "Enter marks for first subject: ",
                "Enter marks for second subject: ",
            )
            if marks is None:
                print("Error: Please enter numbers only for marks.")
            else:
                success, message = repo.add_student(name, marks[0], marks[1])
                print(message)

        elif choice == "2":
            report = repo.all_students()
            if not report:
                print("No records found in the system.")
            else:
                print("\n--- STUDENT REPORTS ---")
                for name, marks, average in report:
                    ui.show_report_row(name, marks, average)

        elif choice == "3":
            highest_average, toppers = repo.find_topper()
            if not toppers:
                print("No data available for analysis.")
            else:
                ui.show_topper(highest_average, toppers)

        elif choice == "4":
            name = input("Enter name to search: ").strip()
            result = repo.search_student(name)
            if result is None:
                print("Student not found.")
            else:
                actual_name, marks, average = result
                print("Found -> Name:", actual_name, "| Marks:", marks, "| Average:", average)

        elif choice == "5":
            name = input("Enter name of student to update marks: ").strip()
            if repo.search_student(name) is None:
                print("Student not found in records.")
            else:
                actual_name, current_marks, _ = repo.search_student(name)
                print("Current marks for", actual_name, "are:", current_marks)
                marks = ui.get_marks_input(
                    "Enter new marks for first subject: ",
                    "Enter new marks for second subject: ",
                )
                if marks is None:
                    print("Error: Please enter valid numbers only.")
                else:
                    repo.update_marks(name, marks[0], marks[1])
                    print("Success: Marks updated successfully!")

        elif choice == "6":
            name = input("Enter name to delete: ").strip()
            deleted_name = repo.delete_student(name)
            if deleted_name is None:
                print("Student not found.")
            else:
                print("Student record deleted.")

        elif choice == "7":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice, pick between 1 and 7.")


if __name__ == "__main__":
    main()

# I hope this works great and everyone finds it helpful for easier and
# more efficient task completion.
# Thank You
# Regards, Have a nice day.
