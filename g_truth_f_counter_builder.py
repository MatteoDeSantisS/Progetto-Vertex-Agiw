import sys
import os

from My_Library import extract_data

def ground_truth_builder(path: str) :
    
    extract_data.ground_truth_data(path)
      
def file_counter_builder(path: str) :
    
    extract_data.extract_data(path)

    
c=ground_truth_builder(sys.argv[1])
p=file_counter_builder(sys.argv[1])