import sys
import os

from My_Library import metrics


def evaluation(path: str):
    accuracy=metrics.accuracy(path)
    recall=metrics.recall(path)
    f1_score=metrics.f1_score(path)
    
    return accuracy,recall,f1_score





accuracy,recall,f1_score=evaluation(sys.argv[1])
print("\nEvaluation Results:")
print("Accuracy: "+ str(accuracy))
print("Recall:" +str(recall))
print("F1_score: "+ str(f1_score))