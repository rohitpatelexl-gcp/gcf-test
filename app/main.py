from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running on GCP Cloud Run 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
