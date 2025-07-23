from fastapi import FastAPI
from app.routes import scan

app = FastAPI(title="Supply Sentinel – CI/CD Threat Analyzer")

# Include the scanning route
app.include_router(scan.router, prefix="/api")
