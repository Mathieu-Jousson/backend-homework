-- Création de la base de données et la table notes
CREATE DATABASE IF NOT EXISTS todo_app CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE todo_app;

CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    done BOOLEAN DEFAULT FALSE
);

-- Un petit exemple (je suis très satisfait d'avoir coché cette case je vous l'avoue)
INSERT INTO notes (title, content, done) VALUES
('Info', "Coder l'appli to-do-notes", TRUE);
