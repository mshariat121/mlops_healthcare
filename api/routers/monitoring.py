from fastapi import APIRouter, HTTPException
from monitoring.drift_monitor import run_psi_monitor

router = APIRouter()

@router.get("/psi")
def get_psi(feature: str = "length_of_stay_hours"):
    try:
        return run_psi_monitor(feature)
    except FileNotFoundError as ex:
        raise HTTPException(status_code=503, detail=str(ex))
