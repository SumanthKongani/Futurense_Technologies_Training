use classicmodels;

show tables;

select * from customers;
select * from employees;
select * from offices;
select * from orderdetails;
select * from orders;
select * from payments;
select * from productlines;
select * from products;

select customerName, phone, city, creditLimit from customers;

select distinct(city) from customers;

select * from products where productLine = 'Motorcycles';

select * from products where productLine = 'Classic Cars' and buyPrice >= 48.81;

select * from products where productLine = 'Classic Cars' or quantityInStock < 3000;

select * from products where MSRP in (95.7, 214.3, 118.94, 193.66);

select * from products where MSRP <> 214.3;

select * from payments where checkNumber like '%Q%';
select * from payments where checkNumber like '_Q%';

select * from payments where checkNumber like '%5_';
select * from payments where checkNumber like '_Q_';

select productLine, sum(quantityInStock) as total from products group by productLine;

select productLine, sum(quantityInStock) as total from products group by productLine order by total desc;


select productLine, productName, sum(quantityInStock) as total, sum(quantityInStock*buyPrice) 
as CostPrice, sum(quantityInStock*MSRP) as Inventory  from products group by productLine, productName order by Inventory desc;

select productLine, productName, sum(quantityInStock) as total, sum(quantityInStock*buyPrice) 
as CostPrice, sum(quantityInStock*MSRP) as Inventory  from products group by productLine, productName having Inventory >=1000000 order by Inventory desc;





