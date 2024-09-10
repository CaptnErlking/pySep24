Create Database EmployeeManagementDb;

-- To select database 
USE EmployeeManagementDb;

-- To create table 
CREATE TABLE Person
(
	id INT PRIMARY KEY auto_increment,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);
DESC Person;
SELECT * FROM Person;
/*
CREATE TABLE Person
(
	id INT auto_increment,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);
*/


INSERT INTO Person(first_name, last_name)
VALUES('rahul', 'dravid');

INSERT INTO Person(first_name, last_name)
VALUES('rohit', 'sharma');

INSERT INTO Person(first_name, last_name)
VALUES('virat', 'kohli'), 
 ('suryakumar','yadav');

-- to query virat kohli by id 
SELECT * FROM Person WHERE id=3;

-- to query virat by name 
SELECT * FROM Person WHERE first_name='virat';
-- to query all the persons
SELECT * FROM Person;
-- to query all the persons
SELECT id, first_name, last_name FROM Person;

INSERT INTO Person(first_name, last_name)
VALUES('Maheswaran','G');

-- to update Maheswaran lastname as 'Govindaraju'
UPDATE Person 
SET last_name='Govindaraju'
WHERE id=5;

DELETE FROM Person
WHERE id=5;


-- departments {id, name}
CREATE TABLE departments
(
    id INT PRIMARY KEY auto_increment,
    name VARCHAR(100) NOT NULL
);
DESC departments;
SELECT * FROM departments;

INSERT INTO departments(name) 
VALUES ('Analysis'),('Design'),('Development'),('Testing');

use EmployeeManagementDb;
-- drop the table 
-- delete person
select * from Person;
truncate table Person;
drop table if exists person;
desc Person;
-- deapartments
-- delete departments
select * from departments;
truncate table departments;
drop table if exists departments;
desc departments;
drop database if exists employeemanagementdb;
-- drop db if there, otherwise create db
drop database if exists EmployeeManagementDb;
Create database if not exists EmployeeManagementDb;
use EmployeeManagementDb;
-- departments,employees, projects,assignments
-- departments{id,name}
DROP TABLE IF EXISTS departments;
        CREATE TABLE if not exists departments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
desc departments; 
select * from departments;
-- employees{id,name,dept_id,job_title,salary,bonus}
-- projects{id,name,budget}
-- assignments{id,employee_id,project_id,role}
drop table if exists employees;
create table if not exists employees(
id int primary key auto_increment,
name varchar(255) not null,
dept_id int not null,
job_title varchar(100) not null,
salary float not null,
bonus float not null,
foreign key(dept_id) references departments(id)
);
desc employees;
select * from employees;
-- projects{id,name,budget}
DROP TABLE if exists projects;
        CREATE TABLE if not exists projects (
            id INT  PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            budget float NOT NULL
        );
        desc projects;
        select * from projects;
-- assignments{id,employee_id,project_id,role}
DROP TABLE if exists assignments;
        CREATE TABLE if not exists assignments (
            id INT PRIMARY KEY AUTO_INCREMENT,
            employee_id INT NOT NULL,
            project_id INT NOT NULL,
            role VARCHAR(255) NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES employees(id),
            FOREIGN KEY (project_id) REFERENCES projects(id)
        );
desc assignments;
select * from assignments;

INSERT INTO departments (name) VALUES
        ('IT Department'),
        ('Product Development'),
        ('Quality Assurance'),
        ('Sales'),
        ('IT Support');
SELECT * FROM departments;
        
INSERT INTO employees (name, dept_id, job_title, salary, bonus) VALUES
        ('John Doe', 1, 'Software Engineer', 70000, 5000),
        ('Jane Smith', 1, 'Data Scientist', 80000, 6000),
        ('Alice Johnson', 2, 'Product Manager', 90000, 7000),
        ('Bob Brown', 2, 'UI/UX Designer', 65000, 4500),
        ('Charlie Davis', 3, 'QA Engineer', 60000, 4000),
        ('Emily Wilson', 3, 'Technical Writer', 55000, 3500),
        ('Frank Thomas', 4, 'Sales Manager', 75000, 5500),
        ('Grace Lee', 4, 'Marketing Specialist', 68000, 5000),
        ('Henry Martinez', 5, 'System Administrator', 72000, 5200),
        ('Ivy Clark', 5, 'Database Administrator', 74000, 5300);
SELECT * FROM employees;
INSERT INTO projects (name, budget) VALUES
        ('Project Alpha', 100000),
        ('Project Beta', 150000),
        ('Project Gamma', 200000),
        ('Project Delta', 250000),
        ('Project Epsilon', 300000);
	SELECT * FROM projects;
INSERT INTO assignments (employee_id, project_id, role) VALUES
        (1, 1, 'Lead Developer'),
        (2, 1, 'Data Analyst'),
        (3, 2, 'Project Manager'),
        (4, 2, 'Designer'),
        (5, 3, 'QA Lead'),
        (6, 3, 'Technical Writer'),
        (7, 4, 'Sales Executive'),
        (8, 4, 'Marketing Analyst'),
        (9, 5, 'Systems Engineer'),
        (10, 5, 'Database Analyst');
	SELECT * FROM assignments;





