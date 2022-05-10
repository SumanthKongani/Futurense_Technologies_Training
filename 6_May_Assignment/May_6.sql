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

# inner join
select * from orderdetails od inner join orders o on od.orderNumber = o.orderNumber;

# left join
select * from orderdetails od left join orders o on od.orderNumber = o.orderNumber;

# right join
select * from orderdetails od right join orders o on od.orderNumber = o.orderNumber;

# outer join
select * from orderdetails od left outer join orders o on od.orderNumber = o.orderNumber;

# bridging unrelated tables
select * from employees e cross join customers c ;

# Multi-Condition Joins
select * from orderdetails od left join orders o on od.orderNumber = o.orderNumber AND quantityOrdered > 26;

# Multiple join 
select * from orderdetails od 
left join orders o on od.orderNumber = o.orderNumber
left join customers c on c.customerNumber = o.customerNumber;

# union
select customerName from customers union select firstName from employees;

