create table medico(
    id integer primary key,
    nome text not null,
    cidade text,
    cpf text not null unique,
    rg integer not null unique,
    especialidade text not null,
);
create table paciente(
    id integer primary key,
    nome text not null,
    cidade text,
    cpf text not null unique,
    rg integer not null unique,
    doenca text not null,
);
create table consulta(
    medico_id integer,
    paciente_id integer,
    horario time,
    foreign key(medico_id) references medico(id),
    foreign key(paciente_id) references paciente(id)
);
