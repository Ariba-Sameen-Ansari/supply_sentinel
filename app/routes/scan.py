from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

# Input schema
class ScanRequest(BaseModel):
    packages: List[str]

# Output schema
class ScanResult(BaseModel):
    results: Dict[str, str]

@router.post("/scan", response_model=ScanResult)
def scan_packages(data: ScanRequest):
    dummy_flags = {}
    for pkg in data.packages:
        if "crypto" in pkg.lower():
            dummy_flags[pkg] = "⚠️ Potentially risky – Obfuscated crypto usage"
        else:
            dummy_flags[pkg] = "✅ Clean"

    return {"results": dummy_flags}
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

from app.services.analyzer import analyze_package
from app.services.mitre_mapper import get_mitre_description
from app.utils.logger import log_detection

router = APIRouter()

class ScanRequest(BaseModel):
    packages: List[str]

class ScanResult(BaseModel):
    results: List[Dict]

@router.post("/scan", response_model=ScanResult)
def scan_packages(data: ScanRequest):
    results = []

    for pkg in data.packages:
        analysis = analyze_package(pkg)
        if analysis["mitre_technique"]:
            analysis["mitre_description"] = get_mitre_description(analysis["mitre_technique"])
        else:
            analysis["mitre_description"] = "None"

        log_detection(analysis)
        results.append(analysis)

    return {"results": results}
