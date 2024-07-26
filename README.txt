docker-compose up  
docker-compose up  -d // runs in background


docker cp input.csv namenode:/input.csv

docker exec -it namenode /bin/bash
hdfs dfs -mkdir -p /path/to/your
hdfs dfs -put /input.csv /path/to/your/input.csv
exit



docker cp process_data.py spark:/process_data.py

docker exec -it spark /bin/bash
spark-submit /process_data.py
