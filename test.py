import numpy as np
from k_means import KMeans
from distance import euclidean
from mean import mean
import pickle

DATA_PATH = 'D:\datasets\mnist\large_dataset\mnist_train.csv'

print('Loading Data')
f = open(DATA_PATH, 'r')
data_list = []
for line in f.readlines():
    observation = np.asfarray(line.split(',')[1:])
    data_list.append(observation/255)
f.close()
print('Finished Loading')

print('Fitting Started')
model = KMeans()
clusters = model.fit(data_list, 10, euclidean, mean)
print('Fitting Finished')

print('Saving Clusters to ./clusters.pkl')
f = open('./clusters.pkl', 'wb')
pickle.dump(clusters, f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()
