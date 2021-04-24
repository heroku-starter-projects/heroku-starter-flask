from app import config
from app import create_app

print('Creating app...')
app = create_app()

if __name__ == "__main__":
    print('App running and listening on port {}'.format(config.PORT))
    app.run(host=config.HOST, port=config.PORT)
