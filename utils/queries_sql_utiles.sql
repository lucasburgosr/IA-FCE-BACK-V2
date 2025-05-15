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

-- CREAR TABLA QUE REGISTRE LAS CONSULTAS POR UNIDAD DE ALUMNO
CREATE TABLE alumno_unidad_stats (
    alumno_id  INT  NOT NULL,
    unidad_id  INT  NOT NULL,
    preguntas_count INT NOT NULL DEFAULT 0,
    PRIMARY KEY (alumno_id, unidad_id),
    FOREIGN KEY (alumno_id) REFERENCES alumno(alumno_id) ON DELETE CASCADE,
    FOREIGN KEY (unidad_id) REFERENCES unidad(unidad_id) ON DELETE CASCADE
);

-- LO MISMO PARA SUBTEMAS
CREATE TABLE alumno_subtema_stats (
    alumno_id  INT  NOT NULL,
    subtema_id  INT  NOT NULL,
    preguntas_count INT NOT NULL DEFAULT 0,
    PRIMARY KEY (alumno_id, subtema_id),
    FOREIGN KEY (alumno_id) REFERENCES alumno(alumno_id) ON DELETE CASCADE,
    FOREIGN KEY (subtema_id) REFERENCES subtema(subtema_id) ON DELETE CASCADE
);

-- CUANDO INSERTAMOS UNA PREGUNTA, PODEMOS CALCULAR EN SQL CON
INSERT … ON CONFLICT … DO UPDATE SET preguntas_count = preguntas_count + 1

-- INSERT para tabla unidad
INSERT INTO unidad (unidad_id, nombre, materia_id)
VALUES (1, 'Lógica y Conjuntos', 1);
INSERT INTO unidad (unidad_id, nombre, materia_id)
VALUES (2, 'Vectores. Rectas y Planos', 1);
INSERT INTO unidad (unidad_id, nombre, materia_id)
VALUES (3, 'Matrices y Determinantes. Aplicaciones', 1);
INSERT INTO unidad (unidad_id, nombre, materia_id)
VALUES (4, 'Sistemas de Ecuaciones Lineales (SEL). Aplicaciones', 1);
INSERT INTO unidad (unidad_id, nombre, materia_id)
VALUES (5, 'Subespacios de Vectores de Rn. Aplicaciones a Matrices y Sistemas', 1);

-- INSERT para tabla subtema
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (1, 'Proposición', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (2, 'Operaciones lógicas', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (3, 'Leyes lógicas', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (4, 'Relaciones lógicas', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (5, 'Predicados', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (6, 'Cuantificadores', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (7, 'Proposiciones universales', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (8, 'Métodos de demostración', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (9, 'Refutación', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (10, 'Nociones básicas de la teoría de conjuntos', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (11, 'Conjuntos numéricos', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (12, 'Relación y función: nociones básicas', 1);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (13, 'Vectores en el espacio bidimensional, tridimensional y n-dimensional', 2);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (14, 'Operaciones con vectores', 2);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (15, 'Producto punto', 2);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (16, 'Longitud y ángulo entre vectores', 2);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (17, 'Propiedades de los vectores', 2);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (18, 'Rectas y planos en el espacio tridimensional', 2);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (19, 'Clasificación de matrices', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (20, 'Operaciones y propiedades con matrices', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (21, 'Rango', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (22, 'Matriz inversa y propiedades', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (23, 'Matrices elementales', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (24, 'Cálculo de la inversa', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (25, 'Determinantes y propiedades', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (26, 'Aplicaciones', 3);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (27, 'Clasificación de los SEL', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (28, 'Métodos de resolución de SEL: matricial', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (29, 'Métodos de resolución de SEL: eliminación de Gauss', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (30, 'Métodos de resolución de SEL: Gauss–Jordan', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (31, 'SEL homogéneos', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (32, 'Propiedades de los SEL', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (33, 'Aplicaciones', 4);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (34, 'Subespacios', 5);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (35, 'Espacio generado y conjunto generador', 5);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (36, 'Dependencia e independencia lineal', 5);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (37, 'Propiedades de los subespacios', 5);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (38, 'Base', 5);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (39, 'Dimensión', 5);
INSERT INTO subtema (subtema_id, nombre, unidad_id)
VALUES (40, 'Aplicación a matrices y sistemas de ecuaciones lineales', 5);