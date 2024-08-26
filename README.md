# Cube Detection and Processing

This project is designed to detect and process the squares in an image, specifically focusing on identifying squares that may represent a face of a Rubik's Cube. The script leverages OpenCV to perform image processing tasks such as contour detection, edge detection, and filtering to find square-like shapes.

## Features

- **Square Detection**: Identify squares in an image that could correspond to a Rubik's Cube face.
- **Contour Filtering**: Filter out contours based on shape and size to ensure accuracy.
- **Image Processing**: Convert images to grayscale, blur, and apply Canny edge detection.
- **Customizable Parameters**: Easily adjust parameters like contour approximation accuracy and closeness factor to improve detection.

## Installation

**1. Clone the Repository**:
```bash
git clone https://github.com/efitz11/cube.git
```

**2. Access the script folder:**
```bash
cd src
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

## Usage

**1. Run the Script:**
```bash
python main.py
```

**2. View Output**: The script will display several intermediate images including:
* Grayscale Image
* Blurred Image
* Canny Edge Detection Output
* Final Image with Detected Squares Highlighted
* These images help visualize each step of the processing pipeline.

## Contributing:
Contributions are welcome! If you'd like to contribute:
* Fork the repository.
* Create a new branch with your feature or bug fix.
* Submit a pull request with a description of your changes.
