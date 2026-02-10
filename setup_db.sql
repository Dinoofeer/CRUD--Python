-- =============================================
-- EJECUTAR ESTE SCRIPT COMO ADMINISTRADOR (sa)
-- EN SQL Server Management Studio
-- =============================================

-- 1. Crear la base de datos
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'crud_examen')
BEGIN
    CREATE DATABASE crud_examen;
END
GO

USE crud_examen;
GO

-- 2. Crear tabla de usuarios (inicio de sesion)
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'usuarios')
BEGIN
    CREATE TABLE usuarios (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL,
        email NVARCHAR(150) NOT NULL UNIQUE,
        password_hash NVARCHAR(255) NOT NULL,
        created_at DATETIME DEFAULT GETDATE()
    );
END
GO

-- =============================================
-- 3. Crear LOGIN y USER restringido
--    Tiene SELECT, INSERT, UPDATE, DELETE en la tabla
--    NO puede hacer DROP, ALTER, CREATE (protege estructura)
-- =============================================

-- Crear login a nivel de servidor
IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = 'app_crud_login')
BEGIN
    CREATE LOGIN app_crud_login WITH PASSWORD = 'CrudApp2026!';
END
GO

-- Crear usuario en la BD vinculado al login
IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'app_crud_user')
BEGIN
    CREATE USER app_crud_user FOR LOGIN app_crud_login;
END
GO

-- Denegar permisos peligrosos (DDL) a nivel de base de datos
DENY ALTER ANY SCHEMA TO app_crud_user;
DENY CREATE TABLE TO app_crud_user;
DENY ALTER ON dbo.usuarios TO app_crud_user;
DENY CONTROL ON dbo.usuarios TO app_crud_user;
GO

-- Otorgar SOLO operaciones DML en la tabla usuarios
GRANT SELECT ON dbo.usuarios TO app_crud_user;
GRANT INSERT ON dbo.usuarios TO app_crud_user;
GRANT UPDATE ON dbo.usuarios TO app_crud_user;
GRANT DELETE ON dbo.usuarios TO app_crud_user;
GO

PRINT '>> Base de datos, tabla y usuario restringido creados correctamente.';
PRINT '>> Login: app_crud_login | Password: CrudApp2026!';
PRINT '>> Permisos: SELECT, INSERT, UPDATE, DELETE en usuarios.';
PRINT '>> DENEGADO: DROP, ALTER, CREATE (no puede destruir estructura).';
GO
