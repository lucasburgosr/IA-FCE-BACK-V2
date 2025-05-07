SELECT * FROM usuario;
SELECT * FROM alumno;

INSERT INTO usuario (email, contrasena, nombres, apellido, nro_documento, firebase_uid, created_at, type)
VALUES 
('pennis.nazarena@fce.uncu.edu.ar','$2b$12$0vPwH9LcDZvlSx9b3zSTDeYCSdQ/X0Gao8CWBRxCJReNEkvdiT66O', 'Nazarena', 'Pennis', 47080410, 'f1BM3gwbd6WssXnmyPdaGIpobYi1', NOW(), 'alumno'),
('profesor@fce.uncu.edu.ar', '$2b$12$o2anKj85TYbuI998pdm.u.LLJntnz6VAHm4ZpR0z7lAisEDWQvy0m', 'Profesor', 'Prueba', 40000000, '5zyU71SDWbcPBbkVbH8Tnr4pSyl2', NOW(), 'profesor')

INSERT INTO alumno (alumno_id)
VALUES (1)

INSERT INTO materia (materia_id, nombre)
VALUES (1, 'Matemática')

INSERT INTO profesor (profesor_id, materia_id)
VALUES (2, 1)

SELECT * FROM alumno;

INSERT INTO asistente (asistente_id, nombre, instructions, materia_id)
VALUES ('asst_LMnzwqHscAlIEBRRrWzB6myW', 'Tutor de Matemática V1', '-', 1);

INSERT INTO alumno_asistente (id, asistente_id)
VALUES (1, 'asst_LMnzwqHscAlIEBRRrWzB6myW');