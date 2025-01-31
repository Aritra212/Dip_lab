# Digital Image Processing Laboratory

A collection of Jupyter notebooks and Python scripts demonstrating various digital image processing techniques and algorithms. This repository contains implementations of fundamental image processing operations using Python.

## Programs Included

- **Bit Plane Slicing** ([bit_plane_slicing.ipynb](bit_plane_slicing.ipynb)): Decomposing an image into its constituent bit planes
- **Enhancement** ([enhancement.ipynb](enhancement.ipynb)): Various image enhancement techniques
- **Gamma Transformation** ([gama_transformation.ipynb](gama_transformation.ipynb)): Gamma correction for controlling image brightness
- **Histogram Processing** ([histogram.ipynb](histogram.ipynb)): Histogram generation, equalization and specification
- **Intensity Slicing** ([intensity_slicing.py](intensity_slicing.py)): Highlighting specific ranges of intensity values
- **Linear Filters** ([linear_filters.ipynb](linear_filters.ipynb)): Implementation of various linear spatial filters
- **Logarithmic Transformation** ([log_transformation.ipynb](log_transformation.ipynb)): Log transformations for dynamic range compression
- **Morphological Operations** ([morphology.ipynb](morphology.ipynb)): Erosion, dilation, opening, closing operations
- **Negative Transformation** ([neg_transformation.ipynb](neg_transformation.ipynb)): Image negation transformations
- **Noise Handling** ([noise.ipynb](noise.ipynb)): Adding and removing different types of noise
- **Non-linear Filters** ([non_linear_filters.ipynb](non_linear_filters.ipynb)): Median and other non-linear filtering techniques
- **Segmentation** ([segmentation.ipynb](segmentation.ipynb)): Image segmentation algorithms
- **Sharpening Filters** ([sharpening_filters.ipynb](sharpening_filters.ipynb)): Implementations of various image sharpening techniques

## Sample Images

The [`Img_used`](Img_used/) directory contains test images used in demonstrations, including:

- Various test patterns
- Medical images
- Document images
- Images with specific artifacts and challenges

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required libraries: NumPy, Pandas, Matplotlib

### Running the Notebooks

1. Clone this repository
   ```
   git clone https://github.com/YOUR-USERNAME/Dip_lab.git
   cd Dip_lab
   ```
2. Install the required dependencies:
   ```
   pip install numpy pandas matplotlib jupyter
   ```
3. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```
4. Open any of the `.ipynb` files to run specific image processing techniques

## Features

- Each notebook is self-contained with detailed explanations
- Includes functions for reading and writing images
- Visualizations of before and after processing
- Step-by-step implementation of algorithms

## License

This project is open source and available for educational purposes.
