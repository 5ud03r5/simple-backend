import os
import importlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.managers import example as example_model
from app.managers._endpoint_handler.creators._router_creator import _ext_routers

app = FastAPI()
origins = "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists(_ext_routers):
    print("Creating ext_router file...")
    routers_list = [
        os.path.splitext(file)[0]
        for file in os.listdir("app/routers")
        if os.path.isfile(os.path.join("app/routers", file)) and file != "__init__.py"
    ]
    with open(_ext_routers, "w") as file:
        file.write(
            "from app.routers import "
            + ", ".join([file for file in routers_list])
            + "\n"
        )
        file.write(
            "routers = [" + ", ".join([file + ".router" for file in routers_list]) + "]"
        )

routers = []

if os.path.exists(_ext_routers):
    imported_module = importlib.import_module("app.ext_routers")
    routers = imported_module.routers

for router in routers:
    app.include_router(router)

example_model.models.Base.metadata.create_all(bind=engine)
