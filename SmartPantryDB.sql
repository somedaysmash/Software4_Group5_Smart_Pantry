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
    ('Eggs', 'Protein', 12, 'Each', 6, '2023-12-01'),
    ('Milk', 'Dairy', 1, 'Litre', 0.5, '2023-11-15'),
    ('Butter', 'Dairy, Fats', 113, 'Grams', 50, '2023-12-10'),
    ('Chicken', 'Protein', 300, 'Grams', 100, '2023-11-20'),
    ('Kale', 'Vegetable', 50, 'Grams', 0, '2023-11-18');

-- Inserting stock data into the Freezer table
INSERT INTO Freezer (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate)
VALUES
    ('Ice Cream', 'Dairy, Dessert' , 1, 'Tub', 0.5, '2024-06-30'),
    ('Ground beef', 'Protein', 200, 'Grams', 100, '2023-12-05'),
    ('Frozen Peas', 'Vegetable', 100, 'Grams', 50, '2024-02-15');

-- Inserting stock data into the Pantry table
INSERT INTO Pantry (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate)
VALUES
    ('Salt', 'Spices/Seasonings', 700, 'Grams', 100, '2028-11-13'),
    ('Pepper', 'Spices/Seasonings', 200, 'Grams', 50, '2026-11-11'),
    ('Olive Oil', 'Fats', 1, 'Liter', 0.3, '2024-10-01'),
    ('Sugar', 'Sugar', 500, 'Grams', 200, '2024-08-15'),
    ('Canned Tuna', 'Protein, Fish', 1, 'Can', 0.5, '2024-09-30'),
    ('Pasta', 'Pasta, Carbohydrate', 300, 'Grams', 150, '2024-07-01'),
    ('Rice', 'Grains, Carbohydrate', 300, 'Grams', 150, '2025-01-01');

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

