from pydantic import BaseModel

class DetectionResultBase(BaseModel):
    image_name: str
    detected_object: str
    confidence_score: float
    x_min: float
    y_min: float
    x_max: float
    y_max: float

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True
