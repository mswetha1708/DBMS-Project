create table if not exists Branchs(Bid int NOT NULL PRIMARY KEY,Bname varchar(100),email varchar(100),city varchar (20),Pno int);
INSERT INTO Branchs VALUES(123,'HolidayInn-Aurum','Aurum@holidayinn.com','FrankFurt',23459109);
INSERT INTO Branchs VALUES(124,'HolidayInn-Platinum','Platinum@holidayinn.com','Munich',34567100);
INSERT INTO Branchs VALUES(125,'HolidayInn-Silver','Silver@holidayinn.com','Berlin',45910110);
CREATE TABLE  Availability (RoomType varchar(20),nofrooms int,paymentstatus varchar(20),cost float,Bid int,foreign key (Bid) references Branchs(Bid));
ALTER TABLE Availability DROP paymentstatus;
ALTER TABLE Availability ADD froms date;
ALTER TABLE Availability ADD tos date;
INSERT INTO Availability VALUES ("Privilege Double-AC",5,5000,123,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Privilege Double-AC",5,5500,124,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Privilege Double-AC",5,5500,125,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Heritage4-bed-AC",5,9000,125,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Heritage4-bed-AC",5,7000,123,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Heritage4-bed-AC",5,8000,124,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Club Class-AC",5,10000,125,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("HeritageDouble-NonAC",5,5100,123,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("HeritageDouble-NonAC",5,5300,124,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("HeritageDouble-NonAC",5,5000,124,"2019-4-11","2019-4-17");
UPDATE Availability SET Bid=125 where RoomType like "H%" AND cost=5000;
INSERT INTO Availability VALUES ("Club Class-AC",5,12000,123,"2019-4-11","2019-4-17");
INSERT INTO Availability VALUES ("Club Class-AC",5,12000,124,"2019-4-11","2019-4-17");



