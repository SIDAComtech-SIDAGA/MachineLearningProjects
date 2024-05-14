CREATE DATABASE BookShop;

CREATE TABLE books(
    ID INT NOT NULL AUTO_INCREMENT,
    Title VARCHAR(50) NOT NULL,
    PRIMARY KEY(ID)
);

INSERT INTO books(ID,Title) VALUES 
(1,'THE CATCHER IN THE RYE'),
(2,"NINE STORIES"),
(3,"FRANNY AND ZOOEY"),
(4,"THE GREAT GATSBY"),
(5,"TENDER ID THE NIGHT")
;

-- ################
SELECT Employees .*, Departments.Name FROM Employees JOIN Departments ON Departments.ID = Employees.DeptID;