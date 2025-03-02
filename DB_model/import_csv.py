import pandas as pd
from db_connection import get_db_connection

df = pd.read_csv('data\candidates.csv', sep=';')

df.columns = [
    'first_name', 'last_name', 'email', 'application_date', 'country',
    'yoe', 'seniority', 'technology', 'code_challenge_score', 'technical_interview_score'
]

conn = get_db_connection()
cursor = conn.cursor()

# INSERT IGNORE para evitar duplicados
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Candidates (
            first_name, last_name, email, application_date, country, yoe, seniority, technology, 
            code_challenge_score, technical_interview_score
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['first_name'], row['last_name'], row['email'], row['application_date'], row['country'],
        row['yoe'], row['seniority'], row['technology'], row['code_challenge_score'], row['technical_interview_score']
    ))

conn.commit()
cursor.close()
conn.close()
