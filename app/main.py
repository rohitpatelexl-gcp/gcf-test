from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI running on GCP Cloud Run 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}



gcloud run deploy fastapi-app --image us-central1-docker.pkg.dev/learning-gcp-480617/fastapi-repo/fastapi-app --platform managed --region us-central1 --allow-unauthenticated
