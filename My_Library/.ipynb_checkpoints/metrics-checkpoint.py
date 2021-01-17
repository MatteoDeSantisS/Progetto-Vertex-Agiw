
# metrics.py
import pickle
import os

def key_with_max_val(_dict):
        values = list(_dict.values())
        keys = list(_dict.keys())

        return keys[values.index(max(values))]
    
def pages_covered(clusters, ground_truth):

        truth_count = {}
        pages_covered = []

        for key in clusters.keys():
            for truth_class in ground_truth:
                truth_count[truth_class] = 0

            for page_name in clusters[key]:

                for truth_class in ground_truth:
                    if truth_class in page_name:
                        truth_count[truth_class] += 1
                        break

            _class = key_with_max_val(truth_count)
            pages_covered.append((key,_class,truth_count[_class],(len(clusters[key]))))

        return pages_covered

    
def total_pages_covered(cluster_name,ground_truth):
        total_pages_covered={}
        for elem in ground_truth:
            for e in cluster_name:
                if (elem==e[1]):
                    if(elem in total_pages_covered.keys()):
                        total_pages_covered[elem]=total_pages_covered[elem]+e[2]
                    else:
                        total_pages_covered[elem]=0
                        total_pages_covered[elem]=total_pages_covered[elem]+e[2]
        return total_pages_covered

    
def accuracy(path):
        folder=os.getcwd()+"\\Files"
        name_file=os.path.basename(os.path.dirname(path))
        
        file_counter = open(folder+"/"+name_file+"_file_counter.pkl","rb")
        file_counter=pickle.load(file_counter)
        
        ground_truth=open(folder+"/"+name_file+"_ground_truth.pkl","rb")
        ground_truth=pickle.load(ground_truth)
        
        clusters=open(folder+"/"+name_file+"_clusters.pkl","rb")
        clusters=pickle.load(clusters)
                      
   
        pages_covered=pages_covedered(clusters, ground_truth)
        total_pages_covered=total_pages_covered(pages_covered,ground_truth)
        accuracy={}
        for key in file_counter.keys():
            for elem in total_pages_covered.keys():
                if(key==elem):
                    accuracy[key]=total_pages_covered[elem]/file_counter[key]

        return accuracy
    
def recall(path):
    folder=os.getcwd()+"\\Files"
    name_file=os.path.basename(os.path.dirname(path))
    
    ground_truth=open(folder+"/"+name_file+"_ground_truth.pkl","rb")
    ground_truth=pickle.load(ground_truth)
        
    clusters=open(folder+"/"+name_file+"_clusters.pkl","rb")
    clusters=pickle.load(clusters)    
    
    cluster_name=pages_covered(clusters,ground_truth)
    recall={}
    for elem in ground_truth:
        count=0
        for key in cluster_name:
            if (key[1]==elem):
                count+=1
                if(elem in recall.keys()):
                    recall[elem]+=key[2]/key[3]
                else:
                    recall[elem]=0
                    recall[elem]+=key[2]/key[3]
        recall[elem]=recall[elem]/count 
    return recall

def f1_score(path):
  
    acc=accuracy(path)
    rec=recall(path)
    f1_score={}
    for elem in acc.keys():
        f1_score[elem]=(2*(acc[elem]*rec[elem]))/(acc[elem]+rec[elem])
    return f1_score      