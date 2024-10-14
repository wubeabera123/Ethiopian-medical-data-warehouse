from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api import models, schemas, crud, database

# Create FastAPI instance
app = FastAPI()

# Create the database tables on startup
@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)

@app.post("/detection-results/", response_model=schemas.DetectionResult)
def create_detection_result(
    detection_result: schemas.DetectionResultCreate, 
    db: Session = Depends(database.get_db)
):
    """Create a new detection result."""
    return crud.create_detection_result(db=db, detection_result=detection_result)

@app.get("/detection-results/", response_model=list[schemas.DetectionResult])
def read_detection_results(
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(database.get_db)
):
    """Retrieve detection results with pagination."""
    results = crud.get_detection_results(db=db, skip=skip, limit=limit)
    return results

# Optionally, add a health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
