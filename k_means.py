import random
import matplotlib.pyplot
class KMeans:
    def fit(self, data_iterable, k, distance_function, mean_function, iterations=10):
        #initialize centroids
        centroids = []
        for i in range(k):
            centroids.append(random.choice(data_iterable))
        
        clusters = {i: [] for i in range(k)}
        for iteration in range(iterations):
            clusters = {i: [] for i in range(k)}
            data = data_iterable
            for observation in data:
                nearest_centroid_index = 0
                for c_index in range(k):
                    if distance_function(centroids[c_index], observation) < distance_function(centroids[nearest_centroid_index], observation):
                        nearest_centroid_index = c_index
                clusters[nearest_centroid_index].append(observation)
            
            # update the centroids
            for c_index in range(k):
                cluster = clusters[c_index]
                centroids[c_index] = mean(cluster)
            
            for index in range(k):
                image = random.choice(clusters[index]).reshape(28, 28)
                matplotlib.pyplot.imshow(image, cmap='Greys', interpolation='None')
                matplotlib.pyplot.show()
        return clusters
