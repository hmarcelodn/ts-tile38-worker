## Tile38 High-Load and Connectivity POC

This is a Falcon API which persists geofence objects to Tile38 through the redis protocol. This proof-of-concepts offers a high-load test with Artillery.

## Installing and Running

Run the following commands to install dependencies

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

Run the Falcon Api with gunicorn

    gunicorn main:app --reload

Install Artillery to perform a stress-test from CLI easily

    npm install -g artillery
    sh perf_test/run.sh

Running kombu/celery worker proof-of-concepts

    cd workers/
    python consumer.py

Running producer

    cd workers/
    python producer.py

Installing Tile38 and running locally

    brew install tile38
    tile38-server -vv

Installing and Running rabbitmq with Docker locally

    docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Opening the rabbitmq management console (guest:guest)

    http://localhost:15672/
