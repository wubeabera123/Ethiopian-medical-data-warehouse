# Ethiopian-medical-data-warehouse

Overview
This project involves implementing an object detection system using the YOLO (You Only Look Once) model and exposing the detection results through a FastAPI application. The project consists of multiple tasks, including data collection, processing, and building an API to serve the data.

Table of Contents
Task 2: Data Collection
Task 3: Object Detection Using YOLO
Task 4: Expose the Collected Data Using FastAPI
Installation
Usage
Contributing

Task 2: Data Collection
Overview
In this task, data is collected from the Chemed Telegram Channel to prepare for object detection.

Steps
Identify the source of data, which is the Chemed Telegram Channel: Chemed Telegram Channel.
Implement a web scraping script to collect images shared in the channel.

Task 3: Object Detection Using YOLO
Overview
This task focuses on setting up an environment for object detection using the YOLO model.

Steps
Setting Up the Environment

Install the necessary dependencies, including OpenCV, TensorFlow, or PyTorch, depending on the YOLO implementation.

pip install opencv-python
pip install torch torchvision  # for PyTorch-based YOLO
pip install tensorflow  # for TensorFlow-based YOLO
Downloading the YOLO Model

Clone the YOLOv5 repository and install the requirements:

git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
Preparing the Data

Collect images from the Chemed Telegram Channel.
Use the pre-trained YOLO model to detect objects in the images.
Processing the Detection Results

Extract relevant data from the detection results, such as bounding box coordinates, confidence scores, and class labels.
Store detection data in a database table.
Monitoring and Logging

Implement logging to track the scraping process, capture errors, and monitor progress.
Task 4: Expose the Collected Data Using FastAPI
Overview
This task involves setting up a FastAPI application to expose the collected detection data via API endpoints.

Steps
Setting Up the Environment

Install FastAPI and Uvicorn:

pip install fastapi uvicorn
Create a FastAPI Application

Set up a basic project structure for the FastAPI application:
api/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py
Database Configuration

In database.py, configure the database connection using SQLAlchemy.
Creating Data Models

In models.py, define SQLAlchemy models for the database tables.
Creating Pydantic Schemas

In schemas.py, define Pydantic schemas for data validation and serialization.
CRUD Operations

In crud.py, implement CRUD (Create, Read, Update, Delete) operations for the database.
Creating API Endpoints

In main.py, define the API endpoints using FastAPI.
Installation
To install the required dependencies for the project, run the following command:


pip install -r requirements.txt
Note: Ensure you have Python 3.6 or higher installed.

Usage
Start the FastAPI server:


uvicorn main:app --reload
Access the API documentation at http://127.0.0.1:8000/docs to interact with the API endpoints.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.