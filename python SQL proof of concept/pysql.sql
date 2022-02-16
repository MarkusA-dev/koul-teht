CREATE DATABASE ORDERBASE
GO

USE ORDERBASE
CREATE TABLE Ordertable(
	OrderId int unique IDENTITY(3000, 10),
	Orderer varchar(50),
	ClientAge int,
	OrderCost money
)
GO

INSERT INTO Ordertable
values
('Heidi', 25, '20.00'),	
('Chi li', 32, '100.50'),
('Larry', 20, '25.00'),
('Jesse', 23, '30.00'),
('John', 26, '15.00')

