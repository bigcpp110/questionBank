import os
from app import create_app

app = create_app("development")


if __name__ == '__main__':
    app.run(host="localhost",port=8000,debug=True)