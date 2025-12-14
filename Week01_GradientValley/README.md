# Week 1 · 梯度的山谷 (The Valley of Gradient)

> 📅 2025.12.02 – 12.08  
> 🎯 概念：学习是沿着能量面下滑的过程（Learning as Gradient Descent）

---

🧮 数学核心  
神经网络的训练，就像在一张起伏的能量地形图上“下山”。  
模型参数 θ 的每一次更新，都是在能量面上沿梯度方向下降：

![Gradient descent](https://latex.codecogs.com/svg.image?\theta_{t+1}=\theta_t-\eta\nabla_{\theta}L(\theta_t))

其中：  
- L(θ)：损失函数（能量）  
- ∇₍θ₎ L：梯度（坡度方向）  
- η：学习率（步长）

---

## 🧭 几何直觉

- 高能量点：模型预测错误多、Loss 高。  
- 低能量谷：模型逼近真实分布。  
- 局部极小值：暂时稳定但非最优。  

学习的目标是找到“最深的谷底”，  
也就是在信息空间中最小化损失的点。

---

## 📊 Python 示例：二维能量面

```python
import numpy as np
import matplotlib.pyplot as plt

# 构造能量函数
def loss_surface(x, y):
    return (x**2 + y**2) + 0.5*np.sin(3*x)*np.cos(3*y)

# 网格
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = loss_surface(X, Y)

plt.figure(figsize=(6,5))
cp = plt.contourf(X, Y, Z, levels=40)
plt.colorbar(cp)
plt.title("Loss Surface Landscape")
plt.xlabel("Parameter x")
plt.ylabel("Parameter y")
plt.show()
