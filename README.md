# **Workshop 01: ETL with Python and SQL**  

*Data transformation and analysis of hiring processes through an efficient ETL pipeline.*  

---  

## **1. Introduction**  
This project implements an **Extract, Transform, Load (ETL) pipeline** to process data on technology candidates. Using **Python**, **Pandas**, and **SQL**, we migrate data from a CSV file to a relational database and generate visualizations in Power BI. This exercise showcases skills in data engineering and relational database management.  

### **Objectives**  
- Migrate data from a CSV file to an SQL database.  
- Structure information in normalized tables.  
- Implement rules for candidate selection and hiring.  
- Analyze trends and patterns in hiring through visualizations.  

---  

## **2. Project Structure**  

```
📂 CHALLENGE
│── 📂 config          # Future configurations
│   ├── requirements.txt   # Project dependencies
│── 📂 data            # Input data
│   ├── candidates.csv # Dataset with candidate information
│── 📂 DB_model        # Database model and loading scripts
│   ├── Hirings.sql    # Database and table creation script
│   ├── import_csv.py  # CSV to MySQL migration script
│── 📂 notebooks       # Exploratory data analysis (EDA)
│   ├── EDA_001.ipynb      # Data cleaning, visualization, and analysis
│── 📂 venv            # Python virtual environment
│── .gitignore         # Files to exclude from version control
│── db_connection.py   # MySQL connection module
│── README.md          # Project documentation
```  

---  

## **3. Installation and Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/isabellaperezcav/workshop_01_ETL.git
cd workshop_01_ETL
```  

### **2. Create the Virtual Environment and Install Dependencies**  
```bash
pip install -r requirements.txt
```  

### **3. Set Up the Database**  
Run the `Hirings.sql` script in MySQL to create the database:  
```bash
mysql -u root -p < DB_model/Hirings.sql
```  

### **4. Import Data**  
```bash
python DB_model/import_csv.py
```  

---  

## **4. ETL Pipeline: Detailed Description**  

### **Extraction**  
- Database connection using `db_connection.py`.  
- Data reading from the `data/candidates.csv` file.  

### **Transformation**  
- **Data cleaning**: Removing null values and duplicates.  
- **Rule creation**: Candidates are marked as `hired` if `code_challenge_score` and `technical_interview_score` ≥ 7.  
- **Date conversion**: Transforming `application_date` into a datetime format.  

### **Load**  
- Inserting transformed data into the `Candidates` table.  
- Creating and populating the `contracted` table.  

---  

## **5. Exploratory Data Analysis (EDA)**  

The `EDA_001.ipynb` notebook includes visualizations and analysis such as:  

- **Hiring distribution**: Proportion of hired vs. non-hired candidates.  
- **Most popular technologies**: Top 10 most in-demand skills.  
- **Countries with the most participation**: Geographic distribution of candidates.  
- **Experience levels**: Hiring analysis based on seniority.  

---  

## **6. Visualizations**  
The visualizations were created in **Power BI** and are available in:  

- `dashboard/desafioETL.pbix` (Editable Power BI file)  
- `dashDesafioETL.pdf` (Exported PDF version)  

---  

## **7. Conclusions**  
This project automates the migration and analysis of technology hiring data. It enables the extraction of key insights, such as hiring trends, distribution by country, and experience levels. Thanks to this ETL pipeline, data-driven decision-making becomes more effective and precise.  

---  

## **8. Final Notes**  
- All data used in this project is fictional and randomly generated.  
- A public library was used to generate test data.  