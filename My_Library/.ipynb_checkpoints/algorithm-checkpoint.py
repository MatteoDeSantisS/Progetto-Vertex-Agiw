import hashlib
import numpy as np
from numpy import nan
from random import randrange
from My_Library import my_utils
import pickle
import os

def cluster_pages(path):
    
    folder=os.getcwd()+"\\Files"
    name_file=os.path.basename(os.path.dirname(path))
    
 
    file_to_read = open(folder+'/'+name_file+".pkl","rb")
    pages= pickle.load(file_to_read)
    #..dizionario che ha per chiave la firma della pagina e valore il conteggio
    hash_table = {}
    list_signature_hash = []
    
    # Primo passaggio
    for page in pages:
        
        #..masked shingle vector 8/8..
        signature_hash = page[1]
        #..calcolo tutti i possibili masked shingle vector per page
        masked_sv = my_utils.masked_shingle_vectors(signature_hash[:])
        
        #..masked shingle vector 6/8 e 7/8
        msv_6, msv_7 = masked_sv['v6'], masked_sv['v7']
        
        #..per efficenza, memorizzo la firma di page in una lista di firme
        list_signature_hash.append(signature_hash)
        
        if(tuple(signature_hash) in hash_table.keys()):
            hash_table[tuple(signature_hash)] = hash_table[tuple(signature_hash)]+1
        else:
            hash_table[tuple(signature_hash)] = 1
            
        for elem in msv_6:
            if(elem in hash_table.keys()):
                hash_table[elem] = hash_table[elem]+1
            else:
                hash_table[elem] = 1
                
        for elem in msv_7:
            if(elem in hash_table.keys()):
                hash_table[elem] = hash_table[elem]+1
            else:
                hash_table[elem] = 1  
   
    # Secondo passaggio
    
    for page in pages:
        signature=page[1]
        max_count = my_utils.get_shingle_max_count(signature,hash_table)
        keys = my_utils.get_shingles_covering_signature(signature,hash_table)
        
        for key in keys:
            if(key != max_count):
                   if(hash_table[key] > 0):
                        hash_table[key] = hash_table[key]-1
                   
    #Delete masked shingle vectors with counts less than threshold from H;
    keys_hash_table=list(hash_table.keys())
    for elem in keys_hash_table:
            if(hash_table[elem]<10):
                del hash_table[elem]
     
    # Terzo passaggio 
  
  
    clusters = {}
    
    for page in pages:
        page_path = page[0]
        signature = page[1]
        v_primo = my_utils.get_shingle_max_count(signature,hash_table)
        if(v_primo != None and hash_table[v_primo]>=10):
            if (v_primo in clusters.keys()):
                clusters[v_primo].append(page_path)
            else:
                clusters[v_primo] = []
                clusters[v_primo].append(page_path)
        cluster_data = open(folder+'/'+name_file+"_clusters.pkl", "wb")
        pickle.dump(clusters,cluster_data)
        cluster_data.close()