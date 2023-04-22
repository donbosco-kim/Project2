import mysql.connector 

def get_uk_employees(mycursor):
    #create query
    sql_query = "Select * from EmployeesPerCountry where country_name = 'United Kingdom'"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results and show the number of employees in UK
    for record in query_result:
        print(f"United Kingdom: {record[1]}")
    return

def get_num_managers(mycursor):
    sql_query = "select department_name, COUNT(*) AS 'Number of Managers' from managers group by department_name"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show the number of managers in each dept
    print("\n-----Number of Managers in Eache Dept-----\n")
    for record in query_result:
        print(f"{record[0]}: {record[1]} managers")
    return

def get_jobtitle_dependents(mycursor):
    sql_query = "select * from DependentsByJobTitle where `Number of Dependents` >= 5"
    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show the number of depends in each job title
    print("\n-----Number of Dependents for each Job Title-----\n")
    for record in query_result:
        print(f"{record[0]}: {record[1]} dependents")
    return

def get_num_dept_hired(mycursor):
    sql_query = "select * from DepartmentHiresByYear where `Year` = 1998"
    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show the number of dept hired in 1998
    print("\n-----Number of Hired in 1998-----\n")
    for record in query_result:
        print(f"{record[1]}: {record[2]} employees hired")
    return

def get_avg_salary_programmers(mycursor):
    sql_query = "select * from AvgSalaryByJobTitle where job_title = 'Programmer'"
    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show the avg salary for programmers
    print("\n-----Average Salary for Programmers-----\n")
    for record in query_result:
        print(f"{record[0]}: ${record[1]} - {record[2]} employees")
    return

def get_deptname_lowest_salary(mycursor):
    sql_query = "select * from AvgSalaryByDepartment where department_name = 'Purchasing'"
    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show the lowest total salary
    print("\n------Lowest Total Salary------\n")
    for record in query_result:
        print(f"{record[0]}: ${record[1]} - {record[2]} employees")
    return

def get_employees_nodependents(mycursor):
    sql_query = "select * from EmployeeDependents where `Number of Dependents` = 0"
    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show employees with no dependts
    print("\n-----Employees with no Dependents-----\n")
    for record in query_result:
        print(f"{record[0]} {record[1]}: {record[4]} dependents \n Email: {record[2]} - Phone: {record[3]}")
    return

def get_regions_nolocations(mycursor):
    sql_query = "select * from CountryLocation where `Number of Locations` = 0"
    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()
    
    #loop through results and show regions with no locations
    print("\n-----Regions with no Locations-----\n")
    for record in query_result:
        print(f"{record[0]}: {record[1]} locations")
    return

def print_menu():
    print("\nChoose an option")
    print("1. Show Number of Employees in UK")
    print("2. Show number of managers per department")
    print("3. Show the job titles with the most dependents")
    print("4. Show number of department hires in 1998")
    print("5. Show average salary for programmers")
    print("6. Show department name with the lowest average salary")
    print("7. Show employees with no dependents")
    print("8. Show regions with no locations")
    print("9. Exit Application")
    return

def get_user_choice():
    print_menu()
    choice = int(input("\nEnter Choice: "))
    return choice

def main():
    #create conection object to connect to database
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            password="root",
            database="project2"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error occured: {err}\nExiting program...")
        quit()
        
    #create database cursor
    mycursor = mydb.cursor()
    while (True):
        try:
            user_choice = get_user_choice()
            if user_choice == 1:
                get_uk_employees(mycursor)
            elif user_choice == 2:
                get_num_managers(mycursor)
            elif user_choice == 3:
                get_jobtitle_dependents(mycursor)
            elif user_choice == 4:
                get_num_dept_hired(mycursor)
            elif user_choice == 5:
                get_avg_salary_programmers(mycursor)
            elif user_choice == 6:
                get_deptname_lowest_salary(mycursor)
            elif user_choice == 7:
                get_employees_nodependents(mycursor)
            elif user_choice == 8:
                get_regions_nolocations(mycursor)
            elif user_choice == 9:
                print("Bye!!!")
                break
            else:
                print("Error, number must be 1-9")
        except ValueError:
                print("Please enter a number.")
