--Q1
Create VIEW EmployeesPerCountry As
select c.country_name, COUNT(e.employee_id) AS "Number of Employees"
from countries c, locations l, departments d, employees e
where c.country_id = l.country_id AND l.location_id = d.location_id AND d.department_id = e.department_id
group by c.country_name
order by COUNT(e.employee_id) desc;

Select * from EmployeesPerCountry
where country_name = "United Kingdom";

--Q2
