## How to run backend locally for development
1. Application is written on WSL environment, other systems not tested for local development
2. You need to have mysql installed on your machine or dockerized
3. mysql need to be running with following settings: `mysql+pymysql://backend:backend@localhost/backend`, default port
4. From backend directory run uvicorn main:app --reload
