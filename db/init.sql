CREATE DATABASE IF NOT EXISTS bandnamesdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bandnamesdb;

CREATE TABLE IF NOT EXISTS adjectives (
  id INT AUTO_INCREMENT PRIMARY KEY,
  adjective VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS nouns (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

-- permet de s'assurer que les tables soit vide
TRUNCATE TABLE adjectives;
TRUNCATE TABLE nouns;

-- 10 adjectifs
INSERT INTO adjectives (adjective) VALUES
('Rapide'),
('Lumineux'),
('Ancien'),
('Silencieux'),
('Sombre'),
('Puisssant'),
('Fragile'),
('Flemmard'),
('Majestueux'),
('Durable'),
('Frigide'),
('Brulant');

-- 10 noms
INSERT INTO nouns (name) VALUES
('Biscuits'),
('Alpacca'),
('Echo'),
('Mers'),
('Monstres'),
('Etoiles'),
('Villages'),
('Dragons'),
('Lanterns'),
('Nuage'),
('Soleil'),
('Mirroires');