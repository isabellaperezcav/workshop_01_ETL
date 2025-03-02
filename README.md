# **Migración y Visualización de Datos de Contrataciones**

## **1. Introducción**
Este proyecto tiene como objetivo migrar datos desde un archivo CSV a una base de datos relacional y generar visualizaciones con información relevante sobre las contrataciones en tecnología.

## **2. Estructura del Proyecto**

```
📂 DESAFIO
│── 📂 config
│── 📂 data
│   ├── candidates.csv
│── 📂 DB_model
│   ├── Hirings.sql
│   ├── import_csv.py
│── 📂 notebooks
│   ├── EDA.ipynb
│   ├── graficas.ipynb
│── 📂 venv
│── .gitignore
│── db_connection.py
│── desktop.ini
│── README.md
│── requirements.txt
```

### **Explicación de Archivos y Carpetas**
- **`config/`**: Directorio reservado para futuras configuraciones.
- **`data/candidates.csv`**: Dataset con la información de candidatos.
- **`DB_model/`**: Contiene el modelo de base de datos y scripts de importación.
  - `Hirings.sql`: Creación de la base de datos y estructura de la tabla.
  - `import_csv.py`: Script para cargar datos desde CSV a MySQL.
- **`notebooks/`**: Contiene los notebooks para análisis y visualización.
  - `EDA.ipynb`: Análisis exploratorio de datos.
  - `graficas.ipynb`: Generación de visualizaciones y reportes en PDF.
- **`venv/`**: Entorno virtual con dependencias del proyecto.
- **`.gitignore`**: Archivos y carpetas a excluir del control de versiones.
- **`db_connection.py`**: Módulo para conectar a la base de datos MySQL.
- **`requirements.txt`**: Lista de dependencias necesarias.
- **`README.md`**: Documentación del proyecto.

## **3. Instalación y Configuración**

### **1. Clonar el repositorio**
```bash
git clone https://github.com/isabellaperezcav/workshop_01_ETL
cd DESAFIO
```

### **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **3. Configurar la Base de Datos**
Ejecutar el script `Hirings.sql` en MySQL para crear la base de datos:
```sql
mysql -u root -p < DB_model/Hirings.sql
```

### **4. Importar Datos**
```bash
python DB_model/import_csv.py
```

## **5. Visualizaciones**
Dashboard realizado en powerBi con los datos de la db, este se encuentra disponible en "dashboard/desafioETL.pbix"

## **6. Conclusiones**
Este proyecto permite migrar datos de contrataciones a MySQL y analizarlos con gráficos informativos, facilitando la toma de decisiones basada en datos.

