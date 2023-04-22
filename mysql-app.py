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

