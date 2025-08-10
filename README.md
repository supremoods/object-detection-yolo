# Object Detection Setup

## Python Version
- Requires **Python 3.9.6**

---

## Prerequisites
- [`ultralytics`](https://pypi.org/project/ultralytics/) – for YOLO models
- `yolo` – (optional) older YOLO package, install only if needed
- `opencv-python` (`cv2`) – for image/video processing

---

## Setup Instructions

### 1. Create a Virtual Environment
```bash
python3 -m venv obj-detection
```


### 2. Activate the Virtual Environment

macOS / Linux
```bash
source obj-detection/bin/activate
```

Windows (PowerShell)
```bash
obj-detection\Scripts\Activate.ps1
```


### 3. Install all libraries
```
pip install -r requirements.txt
```

### 4. run the app
```
python app.py
```