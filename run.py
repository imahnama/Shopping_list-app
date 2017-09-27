from app.app import app

app.config['SECRET_KEY'] = "Am a SECRET_KEY"

if __name__ == '__main__':
    app.run(port=7000)
