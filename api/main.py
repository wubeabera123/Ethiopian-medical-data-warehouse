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

@app.get("/detection-results/{detection_result_id}", response_model=schemas.DetectionResult)
def read_detection_result(
    detection_result_id: int,
    db: Session = Depends(database.get_db)
):
    """Retrieve a specific detection result by ID."""
    result = crud.get_detection_result_by_id(db=db, detection_result_id=detection_result_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return result

@app.put("/detection-results/{detection_result_id}", response_model=schemas.DetectionResult)
def update_detection_result(
    detection_result_id: int,
    updated_result: schemas.DetectionResultUpdate,
    db: Session = Depends(database.get_db)
):
    """Update a detection result."""
    result = crud.update_detection_result(db=db, detection_result_id=detection_result_id, updated_result=updated_result)
    if result is None:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return result

@app.delete("/detection-results/{detection_result_id}", response_model=dict)
def delete_detection_result(
    detection_result_id: int,
    db: Session = Depends(database.get_db)
):
    """Delete a detection result."""
    success = crud.delete_detection_result(db=db, detection_result_id=detection_result_id)
    if not success:
        raise HTTPException(status_code=404, detail="Detection result not found")
    return {"detail": "Detection result deleted"}

# Optionally, add a health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
