""" AI vs ML vs DL 
AI is the broader concept of machines being able to carry out tasks in a way that we would consider “smart”.
AI is the process of making a machine intelligent.

ML is a current application of AI based around the idea that we should really just be able to 
give machines access to data and let them learn for themselves.
Limitation of ML is that it requires human intervention to learn and improve from data.
ML is a Tool to make predictions based on data. It is a subset of AI that uses statistical techniques to enable machines to improve at tasks with experience.

Whereas DL is a subset of ML that uses neural networks with three or more layers.

DL is a subset of ML that uses neural networks with three or more layers. 
These neural networks attempt to simulate the behavior of the human brain—albeit far from matching 
its ability—allowing it to “learn” from large amounts of data. While a neural network with a single layer 
can make approximate predictions, additional hidden layers can help optimize accuracy.
DL is more powerful than ML, but requires a lot of data and computational power. 
It is a tool to make predictions based on data. It is a subset of ML that uses neural networks with three or more 
layers.

Neural networks are a set of algorithms, modeled loosely after the human brain, that are designed to recognize 
patterns.

PyTorch is an open-source machine learning library based on the Torch library, used for applications such as 
computer vision and natural language processing, primarily developed by Facebook's AI Research lab (FAIR).

Tensors are a specialized data structure that PyTorch uses to store data. They are similar to NumPy's ndarrays,
but can also be used on GPUs to accelerate computing.

Autograd is PyTorch's automatic differentiation engine that powers neural network training. It records a graph of 
all the operations that produce your data, and then it replays it to compute gradients.
require_grad = True is a flag that tells PyTorch to track all operations on the tensor. When you set require_grad = True,
PyTorch will start to track all operations on that tensor, allowing you to compute gradients for backpropagation.
 This is essential for training neural networks, as it enables the model to learn from the data by adjusting its 
 weights based on the computed gradients.

Computational graphs are a way to represent mathematical expressions as a graph, where nodes represent operations 
and edges represent the flow of data. In PyTorch, the computational graph is dynamically created as operations are
performed on tensors, allowing for flexible model building and automatic differentiation.

Training Loop is the process of iteratively updating the model's parameters based on the computed gradients and the loss function.
Steps:
1. make a prediction
2. calculate the loss
3. backpropagate the loss
4. compute the gradients
5. update the model's parameters (clear the gradients after updating the parameters)


CNN stands for Convolutional Neural Networks, is a class of deep neural networks, most commonly applied to analyzing visual imagery.
stride is the number of pixels by which we slide the filter matrix over the input image. It controls how much we move the filter at each step.
padding is the process of adding extra pixels around the border of an image. It is used to control the spatial dimensions of the output feature map after applying a convolution operation.
kernel size is the dimensions of the filter matrix used in the convolution operation. It determines the size of the region in the input image that the filter will cover at each step.
in_channels is the number of channels in the input image (e.g., 1 for grayscale, 3 for RGB).
out_channels is the number of channels produced by the convolution operation, which corresponds to the number of filters applied to the input image.

pooling is a downsampling operation that reduces the spatial dimensions of the input feature map, helping to reduce the number of parameters and computation in the network. Common pooling operations include max pooling and average pooling.
basically pooling selects the most important features from the feature map, allowing the network to focus on the most relevant information while discarding less important details.

CNN Flow:
image->conv layer->activation function->pooling layer->fully connected layer->flattening->Linear->output layer
"""