import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = {
    'age': [25, 30, 22, 28, 35, 27, 31, 29, 24, 26],
    'income': [50000, 60000, 45000, 70000, 80000, 55000, 65000, 72000, 48000, 52000],
    'spending': [60, 70, 50, 80, 90, 65, 75, 85, 55, 68],
    'savings': [10000, 15000, 8000, 20000, 25000, 12000, 18000, 22000, 9000, 11000]
}
df = pd.DataFrame(data)

# Standardize the data before applying PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components=2) #n_components=2 means we are reducing the data to 2 dimensions
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(data=pca_result, columns=['PCA1', 'PCA2'])

explained_variance = pca.explained_variance_ratio_
print("Variance Captured at each component:\n", np.round(explained_variance*100, 2))

plt.figure(figsize=(6,5))
plt.scatter(pca_df['PCA1'], pca_df['PCA2'],color='black', s=100)
plt.title('PCA Projection (2D View):')
plt.xlabel('PCA1 Main Pattern')
plt.ylabel('PCA2 Minor Pattern') 
plt.grid(True)
plt.savefig("Unsupervised_Learning/pca_projection.png") 
plt.show()

print("new data with 2 features PCA1 PCA2:\n", pca_df)