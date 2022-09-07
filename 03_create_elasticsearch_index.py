import subprocess

from config import JDBC_DRIVER_LIBRARY, JDBC_DRIVER_CLASS, JDBC_CONNECTION_STRING, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_TABLENAME, ELASTICSEARCH_INDEXNAME, LOGSTASH_BINNAME

if __name__ == '__main__':
    with open('logstash.conf', 'w') as conf_file:
        conf_file.write(
'''input {{
  jdbc {{
    jdbc_driver_library => "{}"
    jdbc_driver_class => "{}"
    jdbc_connection_string => "{}"
    jdbc_user => "{}"
    jdbc_paging_enabled => true
    jdbc_page_size => 20000
    jdbc_password => "{}"
    statement => "SELECT * FROM {} where p_type not LIKE '%Letter%' and p_type  not LIKE '%Editorial%' and p_type  not LIKE '%News%' and p_type not like '%Erratum%'"
    tracking_column => "s_id"
    use_column_value => true
  }}
}}
output {{
  elasticsearch {{
    document_id => "%{{s_id}}"
    document_type => "data"
    index => "{}"
    hosts => ["http://localhost:9200"]
  }}
  stdout {{
    codec => rubydebug
  }}
}}
'''.format(
    JDBC_DRIVER_LIBRARY,
    JDBC_DRIVER_CLASS,
    JDBC_CONNECTION_STRING,
    MYSQL_USERNAME,
    MYSQL_PASSWORD,
    MYSQL_TABLENAME,
    ELASTICSEARCH_INDEXNAME
)
        )
    subprocess.run([LOGSTASH_BINNAME, '-f', 'logstash.conf'])
