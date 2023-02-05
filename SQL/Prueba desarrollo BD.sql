use MarvelAPI

create table thumbnail(
idImg int primary key identity (1,1) not null, 
descripcion varchar(100) not null
);

create table marvel_characters(
id int primary key identity (1,1) not null, 
nombre varchar(100) not null, 
descripcion varchar(100) not null, 
comics_available int not null,
idImg int not null,
Constraint fk_img Foreign key (idImg) references thumbnail (idImg)
);

create table stories(
id int primary key identity (1,1) not null, 
descripcion varchar(40) not null
);