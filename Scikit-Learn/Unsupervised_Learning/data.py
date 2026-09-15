#In unsupervised Learning - Clustering is a common technique used to group similar data 
# points together based on their features. The goal is to identify patterns or structures 
# in the data without any prior labels or classifications.
"""
Supervised Vs Unsupervised Learning:

Supervised learning involves training a model on labeled data, where the input features 
are paired with corresponding output labels. The model learns to make predictions based on 
this labeled data. 

In contrast, unsupervised learning deals with unlabeled data, where the 
model tries to find patterns or structures in the data without any predefined labels.

In supervised learning, the model is provided with input-output pairs, and the goal is to 
learn a mapping from inputs to outputs. 

In unsupervised learning, the model is given only input data and must discover hidden patterns
 or relationships within the data.

Common Techniques in Unsupervised Learning:
1. K-Means Clustering
2. Hierarchical Clustering
3. Principal Component Analysis (PCA)
4. Independent Component Analysis (ICA)
5. Autoencoders
"""


"""
Centroid  method is a popular clustering algorithm that partitions data into K clusters 
based on the mean of the data points in each cluster. The algorithm iteratively assigns 
data points to the nearest cluster centroid and updates the centroids until convergence 
is achieved. K-Means is widely used for its simplicity and efficiency in clustering 
large datasets. It is particularly effective when the clusters are well-separated 
and spherical in shape. However, it may struggle with clusters of varying sizes and 
densities, and it is sensitive to the initial placement of centroids. Despite these 
limitations, K-Means remains a fundamental technique in unsupervised learning for 
clustering tasks.
"""


"""
PCA (Principal Component Analysis) is a dimensionality reduction technique that transforms
high-dimensional data into a lower-dimensional space while preserving as much variance as
possible.

PCA solves :

1.Overfitting: By reducing the number of features, PCA can help mitigate overfitting, especially
when the dataset has a large number of features relative to the number of samples.

2. Slow Training: PCA can speed up the training process of machine learning models by reducing the
dimensionality of the input data. With fewer features, models can be trained faster and require
less computational resources.

3. Visualization: PCA can be used for data visualization by projecting high-dimensional data onto a
lower-dimensional space (e.g., 2D or 3D). This allows for better

Dimensionality reduction: PCA reduces the number of features in the dataset while retaining
the most important information. It identifies the principal components, which are linear 
combinations of the original features that capture the most variance in the data. By selecting
a subset of these components, PCA can effectively reduce the dimensionality of the data, 
making it easier to analyze and visualize.
"""

"""
ML Project Workflow:
1. load and understand data
2. preprocess data : handle missing values, data types
3. encode categorical features(columns) using label encoding or one hot encoding
4. train test split data into train and test set
5. scale data using standardscaler or minmaxscaler
6. train model using logistic regression or random forest classifier
7. evaluate model using accuracy, precision, recall, f1 score and confusion matrix
8. save model using joblib or pickle
9. visualize results using matplotlib or seaborn
"""