CREATE DATABASE IF NOT EXISTS bat_bot;
USE bat_bot;

CREATE TABLE IF NOT EXISTS robins(
    id_robin INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre_robin VARCHAR(30) NOT NULL,
    habilidades TEXT NOT NULL,
    armas TEXT NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS villanos(
	id_villano CHAR(3) PRIMARY KEY,
	nombre_villano VARCHAR(20) NOT NULL,
	identidad VARCHAR(20) NOT NULL,
	habilidad TEXT NOT NULL,
	aparicion TEXT NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS batmans(
	id_batman CHAR(3) PRIMARY KEY,
	descripcion TEXT NOT NULL,
	version TEXT NOT NULL,
	aparicion TEXT NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO robins(id_robin,nombre_robin,habilidades,armas) VALUES
('Dick Grayson(Nightwing)','Maestría en Investigación,Maestría en acrobacia,Intimidación,Experto en Artes Marciales,Profecional en Armas,Maestro del Sigilo,Francotirador profesional,Poligdota','Wing Dings,Batarangs,Varas de Esgrima,Vara de Robin'),
('Jason Todd(Red Hodd)','Maestro en artes marciales,Gran manejo de armas letales,Experto Acróbata','Doble pistola'),
('Tim Drake(Red Robin)','Maestro en Artes Marciales,Gran Detective,Acceso a tecnología avanzada y gadgets','Shurikens "R",Discos con el emblema de Red Robin, palos Bo plegables, ganchos'),
('Stephanie Brown(Batgirl)','Excelentes habilidades de sigilo,Gran acróbata,Gran peleadora','Batarangs, ganchos, bombas de gas, el dispositivo de invisibilidad'),
('Damian Wayne','Hábil artista marcial,Alto nivel de resistencia,Fue entrenado en las disciplinas de la ciencia forense, la acrobacia, la criminología, el disfraz y el escapismo','Katana espada, garfios,nudillos de bronce con púas,una máscara de Robin con una variedad de lentes para la situación variada'),
('Carrie Kelley(Catgirl)','Artes Marciales,Gadgets,Reistencia','Cañón de brazo que dispara batarangs');

INSERT INTO villanos(id_villano,nombre_villano,identidad,habilidad,aparicion) VALUES
('Ra´s Al Ghul','Desconocida','Fuerza, velocidad, agilidad y resistencia físicas aumentadas,Domina las artes marciales y el combate cuerpo-a-cuerpo, Es un brillante táctico ','Batman no.232'),
('Bane','Dorrance','Fuerza sobrehumana, alta inteligencia, gran escapista, experto estratega, experto en el disfraz','Batman: La Venganza de Bane número 1'),
('Joker','Desconocido','Coeficiente intelectual de genio,Especialista en sustancias tóxicas,Experto en combate cuerpo a cuerpo,Experto en ingeniería y química,Especialista en explosivos,Alta resistencia,Memoria eidética,Experto en computadoras,Experto en armas blancas y de fuego','Batman #1 Detective Comics #168 (como Red Hood)'),
('Deathstroke','Slade Joseph Wilson','Mejora de atributos físicos y mentales,Factor regenerativo de curación,Experto en artes marciales,Cualificado combatiente armado / desarmado,Maestro táctico,Estratega,Acceso a equipos de alta tecnología,Hábil manipulador','New Teen Titans #2'),
('Enigma(The Riddle)','Edward Nigma','Intelecto de Genio,Detective Experto,Rico Independiente,Escapista','Detective Comics nº140');

INSERT INTO batmans(id_batman,descripcion,version,aparicion) VALUES
('Coeficiente Intelectial Superior (200),Detective Experto,Escapista Experto,Condicion Fisica Extraordinaria,Experto en Artes Marciales Mixtas,Acceso a equipos de alta tecnología,Memoria Fotografica,Extraordinaria Fuerza y Agilidad,Extraordario Manejo De Armamento Militar,Gran Inventor,Razonamiento Intelectual ','Bruce Wayne(Nueva Tierra)','Detective Comics #27 (Mayo de 1939)'),
('Agilidad,Gran escapista,Gadgets,Fortuna,Gran intelecto,Habilidoso francotiraor,Resistencia,Sigilo,Experto en combate Desarmado,Maestro en Armas','Thomas Wayne Jr(Tierra-3)','Justice League of America #29 ,Justice League Vol 2 23 (New 52)'),
('Experto en medicina,Experto en Negocios,Gran tirador,Experto en combate cuerpo a cuerpo','Thomas Wayne(Flashpoint)','Flashpoint #1'),
('Sanacion,Experto en combate','Logan Wayne(Universo Amalgama)','Marvel Versus DC #3 (Abril, 1996)'),
('Análisis táctico,Acrobacia,Combate avanzado mano a mano','Batman(Tierra-30)','Superman: Red Son #1(June, 2003)');

SHOW TABLES;

DESCRIBE robins;
DESCRIBE villanos;
DESCRIBE batmans;

SELECT * FROM robins;
SELECT * FROM villanos;
SELECT * FROM batmans;

CREATE USER 'batman'@'localhost' IDENTIFIED BY 'batman.1297';
GRANT ALL PRIVILEGES ON bat_bot.* TO 'batman'@'localhost';
FLUSH PRIVILEGES;
