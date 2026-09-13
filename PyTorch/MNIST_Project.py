import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

transform=transforms.ToTensor()

train_dataset = MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

class DigitModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net=nn.Sequential(
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        return self.net(x)

model = DigitModel().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
epochs=5

for epoch in range(epochs):
    model.train()
    total_loss=0

    for img,lable in train_loader:
        img=img.view(img.size(0),-1).to(device)
        lable=lable.to(device)

        optimizer.zero_grad()
        output=model(img)
        loss=loss_fn(output,lable)
        loss.backward()
        optimizer.step()

        total_loss+=loss.item()
    print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(train_loader)}")

model.eval()
correct=0
total=0
with torch.no_grad():
    for img,lable in test_loader:
        img=img.view(img.size(0),-1).to(device)
        lable=lable.to(device)

        output=model(img)
        predicted=output.argmax(dim=1)
        total+=lable.size(0)
        correct+=(predicted==lable).sum().item()

print(f"Accuracy: {100*correct/total:.2f}%")

torch.save(model.state_dict(), "mnist_model.pth")
print("Model saved as mnist_model.pth")

index = 0
img, label = test_dataset[index]

plt.imshow(img.squeeze(), cmap='gray')
plt.title(f"True Label: {label}")
plt.axis('off')
plt.show()

image_flat=img.view(1, -1).to(device)
with torch.no_grad():
    output=model(image_flat)
    predicted_label=output.argmax(dim=1).item()

print(f"User picked image index {index}")
print(f"True Label: {label}")
print(f"Predicted Label: {predicted_label}")
