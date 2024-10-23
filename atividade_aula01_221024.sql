ATIVIDADE: Crie uma nova tabela chamada 'professores', com a mesma quantidade de características, de 'alunos',
--fazendo ao menos duas injeções de dados e uma consulta  (igual ao exemplo acima

CREATE TABLE professores (
  matricula INTEGER PRIMARY KEY,
  nome_professor TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados teste
INSERT INTO professores VALUES (1, 'Gloria', 'F');
INSERT INTO professores VALUES (2, 'Marcia', 'F');

-- consultando as injeções realizadas
SELECT * FROM professores WHERE matricula=1;
