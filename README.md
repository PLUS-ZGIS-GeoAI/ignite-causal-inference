# Causal Graphical Models for Wildfire Ignition Analysis

This repository contains the code and data used in the study on wildfire ignition risk analysis in Austria. The primary goal of the study is to adapt the Fine Fuel Moisture Code (FFMC) by integrating additional factors, using a Graphical Causal Model (GCM) to identify the most influential factors and estimate their direct causal impact on wildfire occurrence. 

## Structure

- `data/`: Contains the wildfire data used in the study.
- `src/`: Python scripts for building the DAG, preprocessing data and util functions for saving and loading the causal model
- `notebooks/`: Contains notebooks for executing the FFMC adjusment study. One notebook consideres FFMC itself in the  study, the does not. 

## Key Features

1. **Graphical Causal Model (GCM)**: 
   - The model is represented as a Directed Acyclic Graph (DAG) that captures the causal relationships between topographical, human, forest, and environmental factors influencing wildfire ignition.
   - We use the `DoWhy` package to estimate causal impacts and Average Causal Effects (ACE).

2. **Causal Inference**:
   - Direct causal impact of factors on wildfire ignition is estimated in "bits" using the arrow strength method.
   - Average Causal Effect (ACE) calculations are used to measure the direct impact of changing factor categories (e.g., forest type, slope) on wildfire probability.

3. **FFMC Adjustment**:
   - FFMC values are adjusted based on the direct causal impact of key factors identified through the GCM. The adjusted FFMC is tested on both wildfire and non-wildfire events.

## Installation

To use this code, clone the repository and install the required Python packages:

```bash
git clone https://github.com/PLUS-ZGIS-GeoAI/ignite-causal-inference.git
conda env create -f env.yml
conda activate causal_inference
