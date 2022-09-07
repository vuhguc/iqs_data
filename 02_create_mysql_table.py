import os
import pandas as pd
import mysql.connector

from config import MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_TABLENAME, MYSQL_CHARSET, MYSQL_COLLATE, CSV_DIRNAME

if __name__ == '__main__':

    # Create table
    db = mysql.connector.connect(
        user = MYSQL_USERNAME,
        password = MYSQL_PASSWORD
    )
    cursor = db.cursor()
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS {} (
                s_id varchar(64),
                doi text,
                version varchar(4),
                pmcid varchar(16),
                pmid int,
                p_date datetime,
                p_type text,
                p_as text,
                source text,
                title text,
                abstract mediumtext,
                symp text,
                cd text,
                target text,
                device text,
                authors text,
                a_count int,
                journal text,
                citation_count int,
                PRIMARY KEY (s_id)
            ) DEFAULT CHARSET={} COLLATE={};
        '''.format(MYSQL_TABLENAME, MYSQL_CHARSET, MYSQL_COLLATE)
    )
    db.commit()

    # Upload csv files
    for root, dirnames, filenames in os.walk(CSV_DIRNAME):
        for filename in sorted(filenames):
            if filename.endswith('.csv'):
                print('Uploading {}'.format(filename))
                df = pd.read_csv(os.path.join(root, filename)).set_index('System ID')
                for index, row in df.iterrows():
                    row[row.isna()] = None
                    try:
                        cursor.execute(
                            '''
                                INSERT INTO {} (
                                    s_id,
                                    doi,
                                    version,
                                    pmcid,
                                    pmid,
                                    p_date,
                                    p_type,
                                    p_as,
                                    source,
                                    title,
                                    abstract,
                                    symp,
                                    cd,
                                    target,
                                    device,
                                    authors,
                                    a_count,
                                    journal,
                                    citation_count
                                )
                                VALUES (
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s
                                )
                            '''.format(MYSQL_TABLENAME),
                            (
                                index,
                                row['DOI'],
                                row['Latest Version'],
                                row['PMCID'],
                                row['PMID'],
                                row['Publication Date'],
                                row['Publication Types'],
                                row['Published As'],
                                row['Source'],
                                row['Title'],
                                row['Abstract'],
                                row['Condition'],
                                row['Chemicals & Drugs'],
                                row['Target'],
                                row['Devices'],
                                row['Authors'],
                                row['Author Count'],
                                row['Journal Name Full'],
                                row['Total Citations']
                            )
                        )
                        db.commit()
                    except Exception as e:
                        print(e)
