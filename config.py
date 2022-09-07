CSV_DIRNAME = 'csv'

NIH_USERNAME = 'anonymous@nih.gov'

NIH_PASSWORD = 'd36f8930-5a72-40c9-989a-3211ef828e10'

NIH_DOWNLOAD_WAIT_TIME = 10

NIH_DOWNLOAD_NUM_RETRIES = 10

MYSQL_USERNAME = 'hoang'
# MYSQL_USERNAME = 'pubmed'

MYSQL_PASSWORD = '123456'
# MYSQL_PASSWORD = 'Dummy@123'

MYSQL_TABLENAME = 'cord_19.nih_20220907'

MYSQL_CHARSET = 'utf8mb4'

MYSQL_COLLATE = 'utf8mb4_unicode_520_ci'
# MYSQL_COLLATE = 'utf8mb4_0900_ai_ci'

ELASTICSEARCH_INDEXNAME = 'nih_20220907'

JDBC_DRIVER_LIBRARY = '/usr/share/java/mariadb-jdbc/mariadb-java-client.jar'
# JDBC_DRIVER_LIBRARY = '/usr/share/java/mysql-connector-java-8.0.11.jar'

JDBC_DRIVER_CLASS = 'org.mariadb.jdbc.Driver'
# JDBC_DRIVER_CLASS = 'com.mysql.jdbc.Driver'

JDBC_CONNECTION_STRING = 'jdbc:mariadb://localhost:3306?useCursorFetch=true'
# JDBC_CONNECTION_STRING = 'jdbc:mysql://localhost:3306?useCursorFetch=true'

LOGSTASH_BINNAME = '/usr/share/logstash/bin/logstash'

PUBDATE_RANGES = [
    ('2018-01-01', '2019-12-31'),
    ('2020-01-01', '2020-01-31'),
    ('2020-02-01', '2020-02-29'),
    ('2020-03-01', '2020-03-31'),
    ('2020-04-01', '2020-04-30'),
    ('2020-05-01', '2020-05-31'),
    ('2020-06-01', '2020-06-30'),
    ('2020-07-01', '2020-07-31'),
    ('2020-08-01', '2020-08-31'),
    ('2020-09-01', '2020-09-30'),
    ('2020-10-01', '2020-10-31'),
    ('2020-11-01', '2020-11-30'),
    ('2020-12-01', '2020-12-31'),
#     ('2021-01-01', '2021-01-31'),
#     ('2021-02-01', '2021-02-28'),
#     ('2021-03-01', '2021-03-31'),
#     ('2021-04-01', '2021-04-30'),
#     ('2021-05-01', '2021-05-31'),
#     ('2021-06-01', '2021-06-30'),
#     ('2021-07-01', '2021-07-31'),
#     ('2021-08-01', '2021-08-31'),
#     ('2021-09-01', '2021-09-30'),
#     ('2021-10-01', '2021-10-31'),
#     ('2021-11-01', '2021-11-30'),
#     ('2021-12-01', '2021-12-31'),
#     ('2022-01-01', '2022-01-31'),
#     ('2022-02-01', '2022-02-28'),
#     ('2022-03-01', '2022-03-31'),
#     ('2022-04-01', '2022-04-30'),
#     ('2022-05-01', '2022-05-31'),
#     ('2022-06-01', '2022-06-30'),
#     ('2022-07-01', '2022-07-31'),
#     ('2022-08-01', '2022-08-31'),
#     ('2022-09-01', '2022-09-30'),
#     ('2022-10-01', '2022-10-31'),
#     ('2022-11-01', '2022-11-30'),
#     ('2022-12-01', '2022-12-31')
]
