#cross join means  return all possible combinations of rows from two tables
# self join means is when a table is joined with itself
SELECT *
FROM table1
CROSS JOIN table2;


SELECT e1.name AS Employee, e2.name AS Manager
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.emp_id

create table colors(name varchar(50) primary key);
insert into colors values
('Red'),('Blue'),('Black'),('Orange'),('Green')

select * from colors;

select * from sizes cross join colors order by sizes.name;

select * from sizes cross join colors order by 
colors.name

create table amazon_company 
(employee_id int primary key,
employee_name varchar(50),
manager_id int)

insert into amazon_company values
(101,'siddarth',102),
(102,'vidhyasree',103),
(103,'narendra',101),
(104,'satyalakshmi',103),
(105,'pooja',101)

select * from amazon_company

select B.manager_id,B.employee_name,A.employee_name as mangaer_name from amazon_company as A  join
 amazon_company as B on 
