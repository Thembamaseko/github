from app import create_app, socketIO

app = create_app(__name__)

if __name__ == "__main__":
    socketIO.run(app)
