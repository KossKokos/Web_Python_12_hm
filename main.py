import uvicorn
from fastapi import FastAPI

from src.routes import contacts, auth

app = FastAPI()

# create route so i don't need to add contacts/... everytimeto my routes functions
app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# start server, main:app - name of the file and app - Fastapi, reload=True - for authomatical reload
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)