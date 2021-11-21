#!/usr/bin/env python3

import requests
import sys
from utils.db import DB
from utils.db_init import init_db

NASA_EONET_BASE_URL = 'https://eonet.gsfc.nasa.gov/api/v3'

def main():

    init_db()

    events = requests.get(f'{NASA_EONET_BASE_URL}/events').json()['events']
    sources = requests.get(f'{NASA_EONET_BASE_URL}/sources').json()['sources']
    categories = requests.get(f'{NASA_EONET_BASE_URL}/categories').json()['categories']

    query = 'TRUNCATE TABLE sources CASCADE;'
    DB.execute(query)
    for source in sources:
        query = 'INSERT INTO sources (eonet_id, title, source, link) VALUES (%s, %s, %s, %s);'
        DB.execute(query, (
            source['id'],
            source['title'],
            source['source'],
            source['link']
        ))

    query = 'TRUNCATE TABLE categories CASCADE;'
    DB.execute(query)
    for category in categories:
        query = 'INSERT INTO categories (eonet_id, title, description, link, layers) VALUES (%s, %s, %s, %s, %s);'
        DB.execute(query, (
            category['id'],
            category['title'],
            category['description'],
            category['link'],
            category['layers']
        ))

    query = 'TRUNCATE TABLE events CASCADE;'
    DB.execute(query)
    for event in events:
        query = 'INSERT INTO events (eonet_id, title, description, link, closed) VALUES (%s, %s, %s, %s, %s);'
        DB.execute(query, (
            event['id'],
            event['title'],
            event['description'],
            event['link'],
            event['closed']
        ))

    query = 'TRUNCATE TABLE events_data CASCADE;'
    DB.execute(query)
    for event in events:
        for geometry in event['geometry']:
            query = 'INSERT INTO events_data (time, event_eonet_id, magnitude_value, magnitude_unit, geometry) VALUES (%s, %s, %s, %s, point(%s, %s));'
            DB.execute(query, (
                geometry['date'],
                event['id'],
                geometry['magnitudeValue'],
                geometry['magnitudeUnit'],
                geometry['coordinates'][0],
                geometry['coordinates'][1]
            ))

    query = 'TRUNCATE TABLE events_sources CASCADE;'
    DB.execute(query)
    for event in events:
        for source in event['sources']:
            query = 'INSERT INTO events_sources (event_eonet_id, source_eonet_id, source_url) VALUES (%s, %s, %s);'
            DB.execute(query, (
                event['id'],
                source['id'],
                source['url']
            ))

    query = 'TRUNCATE TABLE events_categories CASCADE;'
    DB.execute(query)
    for event in events:
        for category in event['categories']:
            query = 'INSERT INTO events_categories (event_eonet_id, category_eonet_id) VALUES (%s, %s);'
            DB.execute(query, (
                event['id'],
                category['id']
            ))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
