from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import example, endpoint_handler
from app.db.database import engine
from app.managers import example as example_model


app = FastAPI()
origins = "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoint_handler.router)
app.include_router(example.router)
example_model.models.Base.metadata.create_all(bind=engine)
