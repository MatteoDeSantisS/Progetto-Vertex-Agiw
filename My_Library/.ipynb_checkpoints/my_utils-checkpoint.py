
import hashlib
import numpy as np
from numpy import nan
from random import randrange

max_shingle_id = 2**32-1
#TODO-valutare prestazione cambiando maxShingleSign = 2**32-1, và cambiato anche nextPrime

#Crea un shingle-vector utilizzando k diverse funzioni hash
#   shingle_set è l'insieme di shingle..
#   coeffA e coeffB sono liste di k-coefficenti
#   k è la lunghezza del shingle_vector..
#   maxShingleSign è il valore massimo delle firme hash
#   nextPrime è il successivo numero primo a maxShingleSign
def shingle_vector(shingle_set, coeff_a, coeff_b, k=8, max_shingle_hash=2**32-1, next_prime=4294967311):
    
    shingle_vector = []
    
    #..per ogni coefficente i-esimo
    for i in range(0, k):
        min_hash_code = next_prime + 1
        
        #..per ogni shingle in shingle_set
        for shingle in shingle_set:
            
            #..si utilizza l'iesima funzione di hash hi(x) = (ai*x + bi) % c
            hash_code = (coeff_a[i] * hash(shingle) + coeff_b[i]) % next_prime
            
            #..si seleziona il minimo valore di hash
            if hash_code < min_hash_code:
                min_hash_code = hash_code 
                
        shingle_vector.append(min_hash_code)
    return shingle_vector

#Crea un shingle set da un documento
def get_shingle_set(document, shingle_lenght=10):
    #...tokenizzazione del testo del documento...
    tokens = document.split()
    
    #...ritorno di k shingle aventi lunghezza pari all'attributo shingle_lenght
    return set([' '.join(tokens[i:i+shingle_lenght])
                     for i in range(len(tokens) - shingle_lenght + 1)])

#Crea una lista di k numeri random unici
def pick_random_coeffs(k=8):
    
    rand_list = []
    while k > 0:
        rand_index = randrange(0,max_shingle_id)
        while rand_index in rand_list:
            rand_index = randrange(0,max_shingle_id)
        rand_list.append(rand_index)
        k = k-1
    return rand_list
    
#Calcolo dei masked shingle vectors 6/8 e 7/8, quelli da 8/8 sono banalmente dei shingle vector
def masked_shingle_vectors(shingle_vector):
    
    masked_vectors = {}
    
    masked_vectors_7_8 = []
    masked_vectors_6_8 = []
    
    #..ciclo per la creazione dei 7/8 masked shingle vectors
    for wildcard in range(len(shingle_vector)):
        
        #..copio il contenuto del vettore in uno nuovo
        mv_7_8 = shingle_vector[:]
        
        #..imposto il byte corrente come wildcard
        mv_7_8[wildcard] = np.nan
        masked_vectors_7_8.append(tuple(mv_7_8))
        wildcard += 1
        
        #..ciclo per la creazione dei 6/8 masked shingle vectors
        for elem in range(wildcard,len(shingle_vector)):
            
            #..eseguo lo stesso procedimento 
            mv_6_8 = mv_7_8[:]
            mv_6_8[elem] = np.nan
            
            masked_vectors_6_8.append(tuple(mv_6_8))
    
    masked_vectors["v6"] = masked_vectors_6_8
    masked_vectors["v7"] = masked_vectors_7_8
    
    return masked_vectors 

def get_shingle_max_count(elemV,listH):
    elemH = [*listH]
    c = np.array(elemV)
    key = []
    x = 0
    for elem in elemH:
        if(np.sum(c==np.array(elem)) >= 6):
            if(listH[elem] > x):
                x = listH[elem]
                key = elem
    if(x==0):
        return(None)
    return key

def get_shingles_covering_signature(elemV,listH):
    elemH = [*listH]
    c = np.array(elemV)
    keys = []
    for elem in elemH:
        if(np.sum(c==np.array(elem)) >= 6):
            keys.append(elem)
            
    return keys