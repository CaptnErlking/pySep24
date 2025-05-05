-- to query the bob based on full name (equala)
select * from employees where name = "Bob Brown";

-- to query the bob based on his name ends with (equala)
select * from employees where name like "%Brown";

-- to query the bob based on his name starts with (equala)
select * from employees where name like "Bob%";

-- to query all coloumns selectors
select id, name, dept_id, job_title, salary, bonus from employees;

-- to display name, salary and bonus for all employess
select name, salary, bonus from employees;
select name, salary, bonus, salary + bonus as total_salary from employees;

-- operators + - * pow

-- to display name, bonus, change_percentage, changed_bonus for all employees
select name, bonus, 15 as change_percentage, bonus / 100 * 115 as changed_bonus from employees;
select name, bonus, 15 as change_percentage, bonus * 1.15 as changed_bonus from employees;
select name, bonus, 15 as change_percentage, (bonus + (bonus * 0.15)) as changed_bonus from employees;

-- filtering | conditional query | where condition
	-- compariosion operators 	=	!=	<> 	<	>	<=	>=
	-- logical operator			AND	OR	NOT
-- to display employees where salary is above 70000
select * from employees where salary > 70000;

-- to display employess where salary is between 60000 and 70000
select * from employees where salary >= 65000 AND salary <= 85000;
select * from employees where salary between 60000 and 80000;

-- to display name in asc order
select * from employees order by name;
-- to display name in dsc order
select * from employees order by name desc;
-- to display salary in acs order
select * from employees order by salary;
-- to display salary in dsc order
select * from employees order by salary desc;

-- to display top 3 salaried
select * from employees order by salary desc limit 3;
-- to display top 3 salaried rows
select * from employees order by salary desc limit 3 offset 3;

-- limit and offset are used for pagination
	-- limit defines rows count to be selected
    -- off set defines rows count to be skipped
