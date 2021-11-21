# Earth Watchtower

![watchtower](/watchtower.png)

## Data sources

- https://eonet.gsfc.nasa.gov/docs/v3
- https://sedac.ciesin.columbia.edu/data/set/pend-gdis-1960-2018/data-download
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
# Configure python venv
pyenv install 3.9.6
pyenv virtualenv 3.9.6 earth-watchtower-py396
pyenv activate earth-watchtower-py396

# Install dependencies
cd src/
pip install -r requirements.txt
```

### Start the database

```sh
docker network create earth-watchtower
docker run -d --name timescaledb -p 5432:5432 --network earth-watchtower -e POSTGRES_PASSWORD=password timescale/timescaledb:2.5.0-pg14
docker cp psql timescaledb:/home
docker container exec -it timescaledb sh -c "psql -h localhost -p 5432 -U postgres -a < /home/psql/earth-watchtower-database.sql"
docker container exec -it timescaledb sh -c "psql -h localhost -p 5432 -U postgres -a earth-watchtower < /home/psql/earth-watchtower-schema.sql"
```

References:
- https://docs.timescale.com/  
- https://hub.docker.com/r/timescale/timescaledb  
- https://www.postgresql.org/docs/14/app-psql.html

Visualize and manage the database with [pgAdmin](https://www.pgadmin.org/)

### Start Grafana

```sh
docker run -d --name grafana -p 3000:3000 --network earth-watchtower grafana/grafana:8.2.5
```

### Run the project

```sh
./src/main.py [-vvvvv]
```
