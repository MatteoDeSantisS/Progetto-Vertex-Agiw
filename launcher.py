import sys
import os

from My_Library import algorithm

def launcher(path: str):
    algorithm.cluster_pages(path)
    
    
launcher(sys.argv[1])