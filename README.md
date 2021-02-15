# Naïve K-Means

This is a simple implementation of the naïve K-Means clustering algorithm. The following will explain modules in this repo and thier roles.

## Modules
### k_means.py
Contains the actual implemention of the K-Means algorithm. One can start fitting by invoking the fit() method in the KMeans class.

The fit method takes 4 positional arguments and 1 keyword argument:

- **data_iterable:** An iterable of of d-dimensional vectors (the dataset).

- **k**: The number of clusters.

- **distance_function**: The desired distance function to be used by the algorithm.

- **mean_function**: The desired mean function to be used by the algorithm.

<<<<<<< HEAD
- **iterations**: The number of needed iterations. Default: 10. Of course it is better to implement a mechanism that watches the convergence of our model and stops training when the model has converged enough (Feel free to implement that and Pull request).
=======
- **iterations**: The number of needed iterations. Default: 10. Of course it is better to implement a mechanism that watches the convergence of our model and stops training when the model has converged enough.
>>>>>>> eea9afef61e777d22410401b25e9b6cc0ddf7ee0

- **Returns**: A dictionary with keys from 0 to k-1, each key maps to a cluster (an iterable of d-dimensional vectors).

### distance.py
Contains the deffinitions of our distance funcitons. A distance function takes two points (two d-dimensional vectors) and returns the distance between these two points. By default the Euclidean distance is the only implemented distance function in distance.py.

### mean.py
Contains the deffinitions of our mean functions. A mean function takes the cluster (an iterable of d-dimensional vectors) and returns the mean of that cluster (a d-dimensional vector). By default the mean.py module contains only one mean function.

### test.py

This module was not a part of the repository. But I decided to keep it there as a usage example.
