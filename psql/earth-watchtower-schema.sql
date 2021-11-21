-- Generate earth-watchtower tables

CREATE TABLE events (
    id SERIAL,
    eonet_id VARCHAR(20) UNIQUE NOT NULL,
    title TEXT,
    description TEXT,
    link TEXT,
    closed BOOLEAN,
    PRIMARY KEY (id, eonet_id)
);

CREATE TABLE sources (
    id SERIAL,
    eonet_id VARCHAR(20) UNIQUE NOT NULL,
    title TEXT,
    source TEXT,
    link TEXT,
    PRIMARY KEY (id, eonet_id)
);

CREATE TABLE categories (
    id SERIAL,
    eonet_id VARCHAR(20) UNIQUE NOT NULL,
    title TEXT,
    link TEXT,
    description TEXT,
    layers TEXT,
    value SMALLSERIAL,
    PRIMARY KEY (id, eonet_id)
);

CREATE TABLE events_sources (
    event_eonet_id VARCHAR(20) NOT NULL REFERENCES events (eonet_id) ON DELETE CASCADE ON UPDATE CASCADE,
    source_eonet_id VARCHAR(20) NOT NULL REFERENCES sources (eonet_id) ON DELETE CASCADE ON UPDATE CASCADE,
    source_url TEXT,
    PRIMARY KEY (event_eonet_id, source_eonet_id)
);

CREATE TABLE events_categories (
    event_eonet_id VARCHAR(20) NOT NULL REFERENCES events (eonet_id) ON DELETE CASCADE ON UPDATE CASCADE,
    category_eonet_id VARCHAR(20) NOT NULL REFERENCES categories (eonet_id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (event_eonet_id, category_eonet_id)
);

CREATE TABLE events_data (
    time TIMESTAMPTZ NOT NULL,
    event_eonet_id VARCHAR(20) NOT NULL REFERENCES events (eonet_id) ON DELETE CASCADE ON UPDATE CASCADE,
    magnitude_value DOUBLE PRECISION,
    magnitude_unit VARCHAR(10),
    geometry POINT
);
