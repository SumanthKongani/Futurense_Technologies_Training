show variables like 'have_query_cache';

create database application;
use application;

create table credentials (
id int primary key auto_increment,
user_name varchar(20),
password varchar(100)
);

insert into credentials (user_name, password) values ('incendero', 'incendero');

select * from credentials;