from sqlalchemy.orm import Session
from . import models, schemas

# Create a detection result
def create_detection_result(db: Session, detection_result: schemas.DetectionResultCreate):
    db_result = models.DetectionResult(**detection_result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

# Get all detection results with pagination
def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()

# Get a single detection result by ID
def get_detection_result_by_id(db: Session, detection_result_id: int):
    return db.query(models.DetectionResult).filter(models.DetectionResult.id == detection_result_id).first()

# Edit (Update) a detection result
def update_detection_result(db: Session, detection_result_id: int, updated_result: schemas.DetectionResultUpdate):
    db_result = db.query(models.DetectionResult).filter(models.DetectionResult.id == detection_result_id).first()

    if db_result:
        for key, value in updated_result.dict(exclude_unset=True).items():
            setattr(db_result, key, value)

        db.commit()
        db.refresh(db_result)
        return db_result
    return None

# Delete a detection result
def delete_detection_result(db: Session, detection_result_id: int):
    db_result = db.query(models.DetectionResult).filter(models.DetectionResult.id == detection_result_id).first()

    if db_result:
        db.delete(db_result)
        db.commit()
        return True
    return False
