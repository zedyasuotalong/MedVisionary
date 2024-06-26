DROP TABLE IF EXISTS images;
DROP TABLE IF EXISTS doctorpatient;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS patients;

create table doctor(
  Doctor_ID int NOT NULL AUTO_INCREMENT,
  account varchar(64)  unique not null,
  password varchar(64) not null,
  gender tinyint default 0 check(gender in (0,1)),
  age tinyint default 20 check(age >= 0),
  phone varchar(16) NULL,
  email varchar(32) NULL,
  level tinyint default 0,
  reg_time varchar(32) NULL,
  primary key(Doctor_ID)
);

CREATE TABLE `patients` (
  `Patient_ID` int NOT NULL AUTO_INCREMENT,
  `Patient_Name` varchar(100) NOT NULL,
  `Sex` varchar(2) NOT NULL,
  `Birth_Date` date NOT NULL,
  `Phone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`Patient_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE doctorpatient (
    Relation_ID INT PRIMARY KEY AUTO_INCREMENT,
    Doctor_ID INT NOT NULL,
    Patient_ID INT NOT NULL,
    UNIQUE (Doctor_ID, Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES doctor (Doctor_ID),
    FOREIGN KEY (Patient_ID) REFERENCES patients (Patient_ID)
);

CREATE TABLE `images` (
  `Image_ID` int NOT NULL AUTO_INCREMENT,
  `Examine_Date` datetime NOT NULL,
  `Image_Modality` varchar(50) NOT NULL,
  `Body_Part` varchar(50) DEFAULT NULL,
  `Patient_ID` INT NOT NULL,
  `Diagnosis_Notes` text,
  `Image_Data` longblob NOT NULL,
  `Device` varchar(64) NOT NULL,
  `Number_of_images` int NOT NULL,
  PRIMARY KEY (`Image_ID`),
  KEY `Patient_ID` (`Patient_ID`),
  CONSTRAINT `images_ibfk_1` FOREIGN KEY (`Patient_ID`) REFERENCES `patients` (`Patient_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
