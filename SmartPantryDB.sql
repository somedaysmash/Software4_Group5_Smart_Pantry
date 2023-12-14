-- Creating our Smart Pantry database to contain our stock
DROP DATABASE smart_pantry;

-- Creating our Smart Pantry database to contain our stock
CREATE DATABASE IF NOT EXISTS Smart_Pantry;

-- Using our database
USE Smart_Pantry;

-- Creating the Fridge table
CREATE TABLE Fridge (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    IngredientName VARCHAR(255) NOT NULL,
    TypeOfIngredient VARCHAR(255),
    Quantity DECIMAL(10, 2) NOT NULL,
    UnitOfMeasurement VARCHAR(20),
    MinimumQuantityNeeded DECIMAL(10, 2),
    SellByDate DATE
);

-- Creating the Freezer table
CREATE TABLE Freezer (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    IngredientName VARCHAR(255) NOT NULL,
    TypeOfIngredient VARCHAR(255),
    Quantity DECIMAL(10, 2) NOT NULL,
    UnitOfMeasurement VARCHAR(20),
    MinimumQuantityNeeded DECIMAL(10, 2),
    SellByDate DATE
);

-- Creating the Pantry table
CREATE TABLE Pantry (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    IngredientName VARCHAR(255) NOT NULL,
    TypeOfIngredient VARCHAR(255),
    Quantity DECIMAL(10, 2) NOT NULL,
    UnitOfMeasurement VARCHAR(20),
    MinimumQuantityNeeded DECIMAL(10, 2),
    SellByDate DATE
);

-- Inserting stock data into the Fridge table
INSERT INTO Fridge (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate)
VALUES
    ('Semi-Skimmed  Milk', 'Dairy', 1000, 'mls', 200, '2023-12-31'),
    ('Salted Butter', 'Dairy, Fats', 113, 'grams', 50, '2024-01-31'),
    ('Chicken breast', 'Protein', 300, 'grams', 100, '2023-12-31'),
    ('Kale', 'Vegetable', 50, 'grams', 0, '2023-12-31'),
    ('Single Cream', 'Dairy', 200, 'mls', 0, '2023-12-31'),
	('Eggs', 'Protein', 12.00, 'piece', 6.00, '2023-12-15'),
	('Mild Cheddar Cheese', 'Dairy', 400, 'grams', 0.20, '2023-12-25'),
	('Greek Yogurt', 'Dairy', 500, 'grams', 100, '2023-12-31'),
	('Lettuce', 'Vegetable', 200, 'grams', 100, '2023-12-31'),
	('Carrots', 'Vegetable', 500, 'grams', 250, '2023-12-31'),
	('Apples', 'Fruit', 100, 'grams', 500, '2023-12-31'),
	('Lemons', 'Fruit', 300, 'grams', 150, '2023-12-31'),
	('Tomato Ketchup', 'Condiment', 500, 'mls', 50, '2023-12-31'),
    ('Apple Juice', 'Fruit', 1000, 'mls', 100, '2023-12-31'),
    ('Cream', 'Dairy', 150, 'mls', 100, '2023-12-09');

-- Inserting stock data into the Freezer table
INSERT INTO Freezer (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate)
VALUES
    ('Ice Cream', 'Dairy, Dessert' , 1000, 'mls', 0, '2024-06-30'),
    ('Minced beef', 'Protein', 200, 'grams', 100, '2023-12-05'),
    ('Frozen Peas', 'Vegetable', 100, 'grams', 50, '2024-02-15'),
    ('Broccoli', 'Vegetable', 500, 'grams', 200, '2023-12-31'),
	('Sweetcorn', 'Vegetable', 500, 'grams', 0, '2023-12-31'),
	('Green beans', 'Vegetable', 500, 'grams', 100, '2023-12-31'),
	('Potato Waffles', 'Grain, Carobohydrate', 750, 'grams', 200, '2023-12-31');

-- Inserting stock data into the Pantry table
INSERT INTO Pantry (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate)
VALUES
	('Plain Flour', 'Grain', 200, 'grams', 100, '2023-12-31'),
    ('Self Raising Flour', 'Grain', 200, 'grams', 100, '2023-12-31'),
	('Caster Sugar', 'Sweetener', 500, 'grams', 150, '2023-12-31'),
	('Basmati Rice', 'Grain', 1000, 'grams', 200, '2023-12-31'),
	('Fusilli Pasta', 'Grain', 500, 'grams', 250, '2023-12-31'),
	('Oats', 'Grain', 1000, 'grams', 250, '2023-12-31'),
	('Weetabix', 'Grain', 750, 'grams', 250, '2023-12-31'),
	('Baked Beans', 'Protein', 800, 'grams', 400, '2023-12-31'),
	('Chopped Tomatoes', 'Vegetable', 1200, 'grams', 400, '2023-12-31'),
	('Smooth Peanut butter', 'Protein', 300, 'grams', 100, '2023-12-31'),
	('Cream Crackers', 'Grain', 150, 'grams', 0, '2023-12-31'),
    ('Medium Sliced White Bread', 'Grain', 800, 'grams', 200, '2023-12-31'),
    ('Tortilla Chips', 'Grain', 150, 'grams', 0, '2024-03-31'),
    ('Mustard', 'Condiment', 70, 'mls', 10, '2023-12-24'),
	('Mayonnaise', 'Condiment', 400, 'mls', 50, '2023-12-31'),
	('Dark Soy sauce', 'Condiment', 250, 'mls', 100, '2023-12-31'),
	('Honey', 'Condiment', 500, 'grams', 100, '2023-12-31'),
    ('Baking powder', 'Baking', 100, 'grams', 50, '2023-12-31'),
	('Baking soda', 'Baking', 100, 'grams', 50, '2023-12-31'),
	('Vanilla extract', 'Baking', 50, 'mls', 20, '2023-12-31'),
    ('Table Salt', 'Spice', 500, 'grams', 100, '2023-12-31'),
	('Ground Black pepper', 'Spice', 100, 'grams', 10, '2023-12-31'),
	('Ground Cinnamon', 'Spice', 100, 'grams', 20, '2023-12-31'),
	('Ground Nutmeg', 'Spice', 100, 'grams', 02, '2023-12-31'),
	('Smoked Paprika', 'Spice', 100, 'grams', 20, '2023-12-31');

-- Creating a view named ProteinView
CREATE OR REPLACE VIEW ProteinView AS
-- Selecting all columns from Fridge, Freezer, and Pantry tables
SELECT * FROM Fridge
-- Using WHERE to filter the results by TypeOfIngredient
WHERE TypeOfIngredient LIKE '%Protein%'
-- Using UNION to combine the results from different tables
UNION
SELECT * FROM Freezer
WHERE TypeOfIngredient LIKE '%Protein%'
UNION
SELECT * FROM Pantry
WHERE TypeOfIngredient LIKE '%Protein%';

-- View to see which ingredients are passed sellbydate
CREATE OR REPLACE VIEW ExpiredIngredients AS
SELECT *
FROM Fridge
WHERE SellByDate < CURDATE()
UNION ALL
SELECT *
FROM Freezer
WHERE SellByDate < CURDATE()
UNION ALL
SELECT *
FROM Pantry
WHERE SellByDate < CURDATE();

-- View to see which ingredients are coming to an end today or in the next two days
CREATE OR REPLACE VIEW ExpiringIngredients AS
SELECT *
FROM Fridge
WHERE SellByDate BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 2 DAY)
UNION ALL
SELECT *
FROM Freezer
WHERE SellByDate BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 2 DAY)
UNION ALL
SELECT *
FROM Pantry
WHERE SellByDate BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 2 DAY);
