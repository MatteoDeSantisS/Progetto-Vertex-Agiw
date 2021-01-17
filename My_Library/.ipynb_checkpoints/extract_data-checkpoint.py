from My_Library import my_utils
import hashlib
import numpy as np
import os
import sys
from bs4 import BeautifulSoup as bs
import pickle

coeff_a = my_utils.pick_random_coeffs(10)
coeff_b = my_utils.pick_random_coeffs(10)

def ground_truth_data(dir_name: str):
    cwd = os.getcwd()+"\\Files"
    if not os.path.isdir(cwd):
          os.makedirs(mypath)
    
    name_dataset=os.path.basename(os.path.dirname(dir_name))
    ground_truth = []
    path = os.path.abspath(dir_name)
    root_dir = os.scandir(path)
    
    for _dir in root_dir:
        if not _dir.name in ground_truth:
             ground_truth.append(_dir.name) 
                
    file = open(cwd+"/"+name_dataset+"_ground_truth.pkl", "wb")
    pickle.dump(ground_truth,file)   
    file.close()

def extract_data(dir_name: str):
    
    folder=os.getcwd()+"\\Files"
    name_file=os.path.basename(os.path.dirname(dir_name))
    
    if not os.path.isdir(folder):
          os.makedirs(folder)
  
    path = os.path.abspath(dir_name)
    data = []
    entity={}
    
    
    for root, subdirs, files in os.walk(path):
        if len(files) > 0:
            n_files = len(files)
            entity[root.split(os.path.sep)[-1]]=n_files
            for file_name in files:
                file_path = os.path.join(root, file_name)
                dir_name = os.path.basename(os.path.dirname(file_path))
             
                with open(file_path, 'rb') as current_file:
                    soup = bs(current_file, "html.parser")
                    page_data = ""
                    for tag in soup.findAll(True):
                        page_data = page_data + " " + (tag.name)
                    
                    page_data = my_utils.get_shingle_set(page_data, 10)
                    signature = my_utils.shingle_vector(page_data, coeff_a, coeff_b)
                    data.append([os.path.join(dir_name,file_name), signature])
    
    
    file = open(folder+"/"+name_file+".pkl", "wb")
    pickle.dump(data,file)
    file.close()
    name_folder=open(folder+"/"+name_file+"_file_counter.pkl", "wb")
    pickle.dump(entity,name_folder)
    name_folder.close()   