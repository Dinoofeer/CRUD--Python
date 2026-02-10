-- =============================================
-- EJECUTAR EN SQL Server Management Studio
-- Conectado a: SQL5106.site4now.net
-- BD: db_a34a77_capecac
-- =============================================

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'usuarios')
BEGIN
    CREATE TABLE usuarios (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(150) NOT NULL,
        created_at DATETIME DEFAULT GETDATE()
    );
END
GO

PRINT '>> Tabla usuarios creada correctamente.';
GO
