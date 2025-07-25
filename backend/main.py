from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import symbolic, optimizer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(symbolic.router, prefix="/symbolic")
app.include_router(optimizer.router, prefix="/optimize")