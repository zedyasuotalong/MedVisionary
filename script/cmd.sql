create table doctor(
  id int NOT NULL AUTO_INCREMENT,
  account varchar(64)  unique not null,
  password varchar(64) not null,
  gender tinyint default 0 check(gender in (0,1)),
  age tinyint default 20 check(age >= 0),
  phone varchar(16) NULL,
  email varchar(32) NULL,
  level tinyint default 0,
  reg_time varchar(32) NULL,
  primary key(id)
);
