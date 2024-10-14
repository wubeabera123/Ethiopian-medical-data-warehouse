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

class DetectionResultUpdate(BaseModel):
    image_name: str | None = None
    detected_object: str | None = None
    confidence_score: float | None = None
    x_min: float | None = None
    y_min: float | None = None
    x_max: float | None = None
    y_max: float | None = None

class DetectionResult(DetectionResultBase):
    id: int

    class Config:
        orm_mode = True
