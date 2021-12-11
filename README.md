# STEM Model for 2021

A Python model for graphing the data produced by our 2021 STEM prototype.

## main.py
All executable code (primarily graphing) can be run directly from here.

## model.py
Functions needed for the processing data, which include the rudimentary predictions and time differential methods.

## data_gen.py
All data collected during the course of our experimentation. This data is free to use with an understanding of the project scope, limitations/challenges. This data is defined by NumPy arrays, saved to .npz files, and can be accessed by calling attributes of the Data class.

## data_management.py
Functions defined to help in data management when dealing with changing .npz files; i.e. modifying present data, verifying integrity, and loading them for method accesss.

## graphs.py
A file for defining all graphs necessary to the project. Called by main.

## universal39.yml
Environment file used for Conda to ensure all package requirements are met. If Conda isn't present, use pip or your preferred package manager to install the following:
  * Python 3.9+
  * numpy
  * matplotlib
