# Progetto-Vertex-Agiw

# Vertex

To create the ground_truth file and the file_counter for the evaluation of the algorithm run:
```
python g_truth_f_counter_builder.py <path-dataset>
```
For instance: 
```
python g_truth_f_counter_builder.py ./dataset/www.study.ue/
```

To execute the algorithm run:
```
python launcher.py <path-dataset> 
```
For instance: 
```
python launcher.py ./dataset/www.study.ue/
```

# Metrics:
To evaluate the algorithm run: 

	python evaluation_metrics.py ./dataset/www.study.ue/

