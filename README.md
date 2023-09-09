# Data Exploration and Analysis (EDA) Platform

This is a simple data exploration and analysis ([EDA](https://exploratory-data-analysis-tool-xw2p3me3lahc3mu2qgnypc.streamlit.app/)) platform built using Streamlit and Pandas Profiling. The platform allows users to upload a CSV dataset and perform exploratory data analysis on it.

## Prerequisites

Before running the code, make sure you have the following Python packages installed:

- `streamlit`
- `pandas`
- `pandas_profiling`

You can install them using the following command:
> pip install streamlit pandas pandas-profiling


# Usage

1.  Clone this repository to your local machine:
	>   git clone <repository_url>
2. Change into the project directory:
	>cd <project_directory>
3. Run the Streamlit app:
	>streamlit run main.py

Open a web browser and go to `http://localhost:8501` to access the EDA platform.

# How It Works

-   The platform provides two main options: "Upload" and "EDA."
-   If you choose "Upload," you can upload a CSV dataset file (only `.csv` files are accepted). The uploaded file is saved as `dataset.csv`.
-   If you choose "EDA," the platform performs exploratory data analysis on the uploaded dataset using Pandas Profiling and displays the results.

# Image
![Upload](https://github.com/DanielLampa/Exploratory-Data-Analysis-Tool/blob/main/1.jpg)
![EDA](https://github.com/DanielLampa/Exploratory-Data-Analysis-Tool/blob/main/2.jpg)
