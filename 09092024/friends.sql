-- To create a Database
create database FriendsManagementDb;

-- To select Database
use FriendsManagementDb;

-- To create table
create table person (
	id int primary key auto_increment,
    first_name varchar(255) not null,
    last_name varchar(255) not null
);
desc person;
select * from person;

insert into person(first_name,last_name)
values('Akshay','Anand');

insert into person(first_name,last_name)
values('Tanish','Arora');

insert into person(first_name,last_name)
values	('Adithya','Manipulator'),
		('Arnav','Sharma');
        
insert into person(first_name,last_name)
values('Tillu','Puppy');

-- to query Adithya 
select * from person where id=3;

-- to query by first_name
select * from person where first_name='Tanish';

-- to update last_name of 'Adithya'
update person
set last_name = 'M'
where id=3;




