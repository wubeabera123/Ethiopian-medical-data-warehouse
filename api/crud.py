from sqlalchemy.orm import Session
from . import models, schemas

def create_detection_result(db: Session, detection_result: schemas.DetectionResultCreate):
    db_result = models.DetectionResult(**detection_result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()
