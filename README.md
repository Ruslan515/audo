1. database in Postgre. go to dir `postgre_docker` and run `docker-compose up -d`
2. task_01 and task_02. run crawler. go to `task_01_crawler` and run in terminal `python3 parsing_lenta.py`. all data write to docker postgre
3. task_03. go to `task_03_api`, run `python3 server.py` in one terminal and in another terminal run `python3 client.py`
