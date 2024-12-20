make db-upgrade

gunicorn -w $CONCURRENCY -b $SERVER_HOST:$SERVER_PORT server:app
