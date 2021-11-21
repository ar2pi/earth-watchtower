# Earth Watchtower

## Data sources

- https://eonet.gsfc.nasa.gov/docs/v3
- https://www.climatewatchdata.org/data-explorer/historical-emissions
- https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api
- https://data.worldbank.org/indicator
    - https://datahelpdesk.worldbank.org/knowledgebase/articles/898599-indicator-api-queries
    - https://datahelpdesk.worldbank.org/knowledgebase/articles/1886701-sdmx-api-queries

## Local setup

### Requirements

- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
- [docker](https://docs.docker.com/)

### Python environment

```sh
cd src/
pyenv install 3.9.6
pyenv virtualenv 3.9.6 earth-watchtower-py396
pyenv activate earth-watchtower-py396
pip install -r requirements.txt
```

### Start the database

```sh
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:2.5.0-pg14
docker cp psql timescaledb:/home
docker container exec -it timescaledb sh -c "psql -h localhost -p 5432 -U postgres -a < /home/psql/earth-watchtower-database.sql"
docker container exec -it timescaledb sh -c "psql -h localhost -p 5432 -U postgres -a earth-watchtower < /home/psql/earth-watchtower-schema.sql"
python setup-db.py
```
https://docs.timescale.com/  
https://hub.docker.com/r/timescale/timescaledb  
https://www.postgresql.org/docs/14/app-psql.html

Visualize and manage the database with [pgAdmin](https://www.pgadmin.org/)

### Run the project

```sh
./src/main.py [-vvvvv]
```
