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

