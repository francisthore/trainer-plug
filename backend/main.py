from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.models.base_model import Base
from db.session import engine, get_db
from api.routes import (
    auth, upload_router,
    users, trainers, profiles,
    trainer_verification, clients,
    messages, notifications
  )
from core.error_middleware import ExceptionHandlingMiddleware
from utils.logging_helper import logger

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
app.add_middleware(ExceptionHandlingMiddleware)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(trainers.router)
app.include_router(profiles.router)
app.include_router(upload_router.router)
app.include_router(trainer_verification.router)
app.include_router(clients.router)
app.include_router(messages.router)
app.include_router(notifications.router)


@app.exception_handler(RequestValidationError)
async def handle_validation_error(
  request: Request,
  exc: RequestValidationError
  ):
  """Handles validation error"""
  logger.error(f"Validation error: {exc.errors()}")
  return JSONResponse(
    status_code=422,
    content={
      "success": False,
      "message": "Invalid request params",
      "errors": exc.errors()
    }
  )


@app.get('/')
async def root():
  """Root endpoint"""
  return {'msg': 'Welcome to Trainer Plug API'}
