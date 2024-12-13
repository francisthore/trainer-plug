from fastapi import FastAPI


app = FastAPI(title="Trainer Plug API")

@app.get('/')
async def root():
  """Root endpoint"""
  return {'msg': 'Welcome to Trainer Plug API'}
