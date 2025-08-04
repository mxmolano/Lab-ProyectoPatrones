-- Crear base de datos (ejecutar en consola psql como superusuario)
CREATE DATABASE comentarios_db;

-- Conectarse a la base de datos (dentro de psql)
-- \c comentarios_db

-- Crear tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);