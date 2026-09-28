employees = []

def add_employee():
    print("\n========== ADD EMPLOYEE ==========")

    name = input("Enter employee name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    department = input("Enter department: ").strip()

    if department == "":
        print("Department cannot be empty.")
        return

    role = input("Enter job role: ").strip()

    if role == "":
        print("Role cannot be empty.")
        return

    print("\nEmployee Type:")
    print("1. Faculty")
    print("2. Staff")

    employee_type_choice = input("Enter choice: ")

    if employee_type_choice == "1":
        employee_type = "Faculty"
    elif employee_type_choice == "2":
        employee_type = "Staff"
    else:
        print("Invalid employee type.")
        return

    try:
        salary = float(input("Enter monthly salary: "))

        if salary <= 0:
            print("Salary must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid salary.")
        return

    employee = {
        "id": len(employees) + 1,
        "name": name,
        "department": department,
        "role": role,
        "type": employee_type,
        "salary": salary,
        "overtime": 0
    }

    employees.append(employee)

    print("\nEmployee added successfully!")
    print("Employee ID:", employee["id"])

def view_employees():
    print("\n========== EMPLOYEE LIST ==========")

    if len(employees) == 0:
        print("No employees found.")
        return

    for employee in employees:
        print("----------------------------------------")
        print("ID         :", employee["id"])
        print("Name       :", employee["name"])
        print("Department :", employee["department"])
        print("Role       :", employee["role"])
        print("Type       :", employee["type"])
        print("Salary     :", employee["salary"])
        print("Overtime   :", employee["overtime"], "hours")


def find_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None

def add_overtime():
    print("\n========== ADD OVERTIME ==========")

    try:
        employee_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Invalid employee ID.")
        return

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee not found.")
        return

    try:
        hours = float(input("Enter overtime hours: "))

        if hours < 0:
            print("Overtime hours cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    employee["overtime"] += hours

    print("Overtime added successfully.")


def calculate_payroll(employee):
    basic_salary = employee["salary"]

    overtime_hours = employee["overtime"]

    hourly_rate = basic_salary / 160

    overtime_pay = (
        overtime_hours
        * hourly_rate
        * 1.5
    )

    gross_salary = (
        basic_salary
        + overtime_pay
    )
    if employee["type"] == "Faculty":
        tax_rate = 0.10
    else:
        tax_rate = 0.08

    tax = gross_salary * tax_rate

    
    retirement = gross_salary * 0.05

    net_salary = (
        gross_salary
        - tax
        - retirement
    )

    return (
        basic_salary,
        overtime_pay,
        gross_salary,
        tax,
        retirement,
        net_salary
    )


def generate_payslip():
    print("\n========== GENERATE PAYSLIP ==========")

    try:
        employee_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Invalid employee ID.")
        return

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee not found.")
        return

    (
        basic_salary,
        overtime_pay,
        gross_salary,
        tax,
        retirement,
        net_salary
    ) = calculate_payroll(employee)

    print("\n")
    print("=" * 50)
    print("              UNIVERSITY PAYSLIP")
    print("=" * 50)

    print("Employee ID      :", employee["id"])
    print("Employee Name    :", employee["name"])
    print("Department       :", employee["department"])
    print("Role             :", employee["role"])
    print("Employee Type    :", employee["type"])

    print("-" * 50)

    print(
        "Basic Salary     : ₹",
        format(basic_salary, ".2f")
    )

    print(
        "Overtime Pay     : ₹",
        format(overtime_pay, ".2f")
    )

    print(
        "Gross Salary     : ₹",
        format(gross_salary, ".2f")
    )

    print(
        "Tax              : ₹",
        format(tax, ".2f")
    )

    print(
        "Retirement       : ₹",
        format(retirement, ".2f")
    )

    print("-" * 50)

    print(
        "NET SALARY       : ₹",
        format(net_salary, ".2f")
    )

    print("=" * 50)


def search_employee():
    print("\n========== SEARCH EMPLOYEE ==========")

    search = input(
        "Enter name or department: "
    ).lower()

    found = False

    for employee in employees:

        if (
            search in employee["name"].lower()
            or search in employee["department"].lower()
        ):
            print("----------------------------------------")
            print("ID         :", employee["id"])
            print("Name       :", employee["name"])
            print("Department :", employee["department"])
            print("Role       :", employee["role"])
            print("Type       :", employee["type"])

            found = True

    if not found:
        print("No matching employee found.")

def remove_employee():
    print("\n========== REMOVE EMPLOYEE ==========")

    try:
        employee_id = int(
            input("Enter employee ID: ")
        )
    except ValueError:
        print("Invalid employee ID.")
        return

    employee = find_employee(employee_id)

    if employee is None:
        print("Employee not found.")
        return

    employees.remove(employee)

    print(
        "Employee",
        employee["name"],
        "removed successfully."
    )


def payroll_report():
    print("\n========== PAYROLL REPORT ==========")

    if len(employees) == 0:
        print("No employees available.")
        return

    total_gross = 0
    total_tax = 0
    total_retirement = 0
    total_net = 0

    for employee in employees:

        (
            basic_salary,
            overtime_pay,
            gross_salary,
            tax,
            retirement,
            net_salary
        ) = calculate_payroll(employee)

        total_gross += gross_salary
        total_tax += tax
        total_retirement += retirement
        total_net += net_salary

        print("----------------------------------------")

        print(
            employee["id"],
            employee["name"]
        )

        print(
            "Gross Salary : ₹",
            format(gross_salary, ".2f")
        )

        print(
            "Tax          : ₹",
            format(tax, ".2f")
        )

        print(
            "Retirement   : ₹",
            format(retirement, ".2f")
        )

        print(
            "Net Salary   : ₹",
            format(net_salary, ".2f")
        )

    print("\n========================================")

    print(
        "Total Employees :",
        len(employees)
    )

    print(
        "Total Gross     : ₹",
        format(total_gross, ".2f")
    )

    print(
        "Total Tax       : ₹",
        format(total_tax, ".2f")
    )

    print(
        "Total Retirement: ₹",
        format(total_retirement, ".2f")
    )

    print(
        "Total Net       : ₹",
        format(total_net, ".2f")
    )

    print("========================================")


def main():

    while True:

        print("\n")
        print("==========================================")
        print(" UNIVERSITY PAYROLL MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Add Overtime")
        print("5. Generate Payslip")
        print("6. Payroll Report")
        print("7. Remove Employee")
        print("8. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            add_overtime()

        elif choice == "5":
            generate_payslip()

        elif choice == "6":
            payroll_report()

        elif choice == "7":
            remove_employee()

        elif choice == "8":
            print("\nThank you for using the system.")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select 1-8."
            )

if __name__ == "__main__":
    main()
