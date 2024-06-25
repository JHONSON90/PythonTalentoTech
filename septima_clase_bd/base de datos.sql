create	database consumos;
use consumos;

create table estudiantes(
    idEstudiantes int primary key auto_increment,
    nombre varchar(50),
    apellido varchar(50)
);

create table cursos(
    idCursos int primary key auto_increment,
    nombre varchar(100)
);

create table incripciones(
idEstudiantes INT,
idCursos INT,
    FOREING KEY (idEstudiantes) reference estudiantes(idEstudiantes),
    foreing key (idCursos) reference cursos(idCursos),
    primary key (idEstudiantes, idCursos)
    );