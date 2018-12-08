/*
O serviço de agenda permite que você armazene seus contatos na nuvem. Cada contato é
representado pelo seu nome, sobrenome, celular, e-mail e aniversário (data de nascimento do
contato).
*/

-- Nem o e-mail nem o celular podem se repetir em contatos diferentes.

CREATE TABLE IF NOT EXISTS contatos (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nome TEXT NOT NULL,
  sobrenome TEXT NOT NULL,
  celular TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  aniversario DATE
);

select * from contatos;