DROP DATABASE IF EXISTS estacionamento;
CREATE DATABASE estacionamento;

CREATE USER estacionamento IDENTIFIED BY "estacione";
DROP USER IF EXISTS estacionamento;
GRANT ALL ON *.* TO estacionamento WITH GRANT OPTION;
SELECT * FROM estacionamento;

SELECT * FROM estacionamento.users;
SELECT * FROM estacionamento.roles;
SELECT * FROM estacionamento.user_roles;



SELECT * FROM estacionamento.consertos;
SELECT * FROM estacionamento.vagas;
SELECT * FROM estacionamento.solucoes;
SELECT * FROM estacionamento.reclamacoes;
