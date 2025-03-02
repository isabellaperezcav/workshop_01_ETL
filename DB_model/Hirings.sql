CREATE DATABASE Hirings;
USE Hirings;

CREATE TABLE Candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    application_date DATE,
    country VARCHAR(100),
    yoe INT,
    seniority VARCHAR(50),
    technology VARCHAR(100),
    code_challenge_score FLOAT,
    technical_interview_score FLOAT,
    contracted BOOLEAN
);