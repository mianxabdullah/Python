"""
5 Steps to Implement K-Means Clustering:
1. Tell machine how many clusters (K) to form
2. Drop K randomly selected points from the dataset as initial centroids (starting points/group leaders)
3. Each data point is assigned to the nearest group leader (centroid) based on a distance metric (e.g., Euclidean distance)
4. Move each group leader (centroid) to the mean of the points assigned to it
5. Repeat until the group leaders (centroids) no longer move significantly or a maximum number of iterations is reached

Elbow Method to Determine Optimal K:
The Elbow Method is a technique used to determine the optimal number of clusters (K) in 
K-Means clustering. It involves plotting the within-cluster sum of squares (WCSS) against 
the number of clusters and identifying the "elbow" point where the rate of decrease in WCSS
slows down. This point indicates a good balance between minimizing WCSS and avoiding 
overfitting by using too many clusters.



"""
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

sample_data = {
    'customers': ['Ali', 'Ahmed', 'Ayesha', 'Fatima', 'Hassan', 'Hina', 'Imran', 'Javed', 'Kiran', 'Nida'],
    'age': [25, 30, 22, 28, 35, 27, 31, 29, 24, 26],
    'income': [50000, 60000, 45000, 70000, 80000, 55000, 65000, 72000, 48000, 52000]
}
df = pd.DataFrame(sample_data)

X=df[['age', 'income']]
model = KMeans(n_clusters=3, random_state=42, n_init=10) #n_clusters=3 means we want to create 3 clusters, random_state=42 ensures reproducibility, and n_init=10 specifies the number of times the algorithm will run with different centroid seeds.
df['group']=model.fit_predict(X)

plt.figure(figsize=(6,5))
for group in df['group'].unique():
    group_data = df[df['group'] == group]
    plt.scatter(group_data['age'], group_data['income'], label=f'Group {group}')

plt.title('K-Means Clustering of Customers')
plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()
plt.grid(True)
plt.savefig("Unsupervised_Learning/kmeans_clustering.png")
plt.show()

print("Clustered Data:\n",df)


