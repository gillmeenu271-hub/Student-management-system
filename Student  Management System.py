# Simple Student Management System (Beginner Friendly)
students = {}
# Add Student
def add_student():
    s_id = input("Enter ID: ")
    if s_id in students:
        print("ID already exists")
        return
    
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    
    students[s_id] = [name, course]
    print("Student added successfully")

# View Students
def view_students():
    if not students:
        print("No data found")
        return

    for s_id, data in students.items():
        print(s_id, "-", data[0], "-", data[1])

# Update Student
def update_student():
    s_id = input("Enter ID: ")

    if s_id in students:
        name = input("New Name: ")
        course = input("New Course: ")
        students[s_id] = [name, course]
        print("Updated successfully")
    else:
        print("ID not found")

# Delete Student
def delete_student():
    s_id = input("Enter ID: ")

    if s_id in students:
        del students[s_id]
        print("Deleted successfully")
    else:
        print("ID not found")

# Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice")