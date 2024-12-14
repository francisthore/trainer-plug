from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.models.base_model import Base
from db.session import engine, get_db
from api.routes import auth, users
Base.metadata.create_all(bind=engine)

# my constants
DATABASE_URL = settings.DATABASE_URL
FRONTEND_URL = settings.FRONTEND_URL
origins = [FRONTEND_URL]
# constants end

app = FastAPI(title="Trainer Plug API")
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)
app.include_router(auth.router)
app.include_router(users.router)

@app.get('/')
async def root():
  """Root endpoint"""
  return {'msg': 'Welcome to Trainer Plug API'}
