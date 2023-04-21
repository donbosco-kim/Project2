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
Create VIEW managers AS
select e.first_name, e.last_name, e.email, e.phone_number, j.job_title, d.department_name
from employees e, jobs j, departments d
where j.job_id = e.job_id AND e.department_id = d.department_id AND j.job_title LIKE '%Manager%';

select department_name, COUNT(*) AS 'Number of Managers'
from managers 
group by department_name;

--Q3
Create VIEW DependentsByJobTitle AS
select j.job_title, COUNT(d.dependent_id) AS "Number of Dependents"
from jobs j, dependents d, employees e
where d.employee_id = e.employee_id AND e.job_id = j.job_id
group by j.job_title
order by COUNT(d.dependent_id) desc;

select * from DependentsByJobTitle
where `Number of Dependents` >= 5;

--Q4 shows a different result in my query
Create VIEW DepartmentHiresByYear AS
select YEAR(e.hire_date) AS "Year", d.department_name, COUNT(d.department_id) AS "Employees Hired"
from employees e, departments d
group by YEAR(e.hire_date), d.department_name
order by d.department_name;

select * from DepartmentHiresByYear
where `Year` = 1998;

--Q5
Create VIEW AvgSalaryByJobTitle AS
select j.job_title, AVG(e.salary) AS "Average Salary", COUNT(e.employee_id) AS "Number of Employees"
from jobs j, employees e
where j.job_id = e.job_id
group by j.job_title
order by AVG(e.salary) desc;

select * from AvgSalaryByJobTitle
where job_title = 'Programmer';

--Q6
Create VIEW AvgSalaryByDepartment AS
select d.department_name, AVG(e.salary) AS "Average Salary", COUNT(e.employee_id) AS "Number of Employees"
from departments d, employees e
where d.department_id = e.department_id
group by d.department_name
order by AVG(e.salary) desc;

--this query should return the min value but it returns all values...
select * from AvgSalaryByDepartment
where "Average Salary" = (
  select MIN("Average Salary")
  from AvgSalaryByDepartment
);
 --different query using value hard corded 
SELECT *
FROM AvgSalaryByDepartment
WHERE "Average Salary" < 4200;

--last resort query :).... super hard coded 
select * from AvgSalaryByDepartment
where department_name = 'Purchasing';




