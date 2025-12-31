
# Week 2 · 顾客路径的向量空间 (Vector Field of Customer Paths)

> 📅 2025.12.09 – 12.15  
> 📍 AI Space Geometry 系列｜Geometry × Retail × AI  
> 🎯 主题：如何通过向量场理解顾客的“流动意图”

---

## 🧭 几何视角（Geometry View）

顾客在门店内的行走路径并非杂乱无章，而是一个可以被建模的**向量场（Vector Field）**。  
每条路径都代表了方向、目标和能量损耗。  
当大量顾客沿着相似方向移动时，就出现了「主流线」（Flow Line）——  
那是**人类注意力在空间中的梯度下降轨迹**。

---

## 🧮 数学定义

顾客路径向量定义：

![Path vector definition](https://latex.codecogs.com/svg.image?\vec{v_i}%20=%20(dx_i,%20dy_i)%20=%20(x_{end}%20-%20x_{start},%20y_{end}%20-%20y_{start}))

方向相似度由 **余弦相似度** 衡量：

![Cosine similarity](https://latex.codecogs.com/svg.image?\cos(\theta_{ij})%20=%20\frac{\vec{v_i}\cdot\vec{v_j}}{\left\Vert\vec{v_i}\right\Vert\left\Vert\vec{v_j}\right\Vert})

当 cos(θ) ≈ 1，表示两条路径方向几乎相同。



当 cos(θ) ≈ 1，表示两条路径方向几乎相同。

---

## 🧠 零售落地视角（Space Geometry View）

| 步骤 | 操作 | 说明 |
|------|------|------|
| 1️⃣ | 收集顾客动线数据 | 可来自传感器、热力摄像或 POS 时序 |
| 2️⃣ | 聚合路径向量 | 计算起止点 `(start_x, start_y)` → `(end_x, end_y)` |
| 3️⃣ | 计算方向相似度 | 使用 Cosine Similarity |
| 4️⃣ | 聚类主流路径 | KMeans 或 DBSCAN |
| 5️⃣ | 输出主流动线图 | 使用 Matplotlib `quiver` / `streamplot` |

输出模板（飞书 Pro 版）👉 [《顾客路径聚合分析》](https://ai.feishu.cn/sheets/xxxx)

---

## 🧰 示例数据

```csv
store_id,path_id,start_x,start_y,end_x,end_y,dx,dy,basket_sales
8119,v_0001,0.0,5.2,6.5,7.8,6.5,2.6,120.0




## Python 示例（Vector Field + Flow Families）

目标：
1）把每条顾客路径变成方向向量
2）用方向聚类得到 Flow Families
3）用 不同颜色在图上展示不同 Flow
4）画出每个 Flow 的 主流线（Flow Line）

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# ----------------------------
# 1) Input: path-level data
# ----------------------------
# Replace this demo with: df = pd.read_csv("your_paths.csv")
df = pd.DataFrame({
    "store_id":[8119, 8119, 8119, 8119],
    "path_id":["v_0001","v_0002","v_0003","v_0004"],
    "start_x":[0.0, 0.0, 0.0, 0.0],
    "start_y":[5.2, 2.2, 9.2, 6.0],
    "end_x":[6.5, 7.8, 6.9, 7.2],
    "end_y":[7.8, 2.1, 8.1, 5.2],
    "basket_sales":[120.0, 90.0, 180.0, 110.0],
})

# ----------------------------
# 2) Path vectors
# ----------------------------
df["dx"] = df["end_x"] - df["start_x"]
df["dy"] = df["end_y"] - df["start_y"]

# ----------------------------
# 3) Direction-normalize (key!)
#    We cluster "direction", not "distance"
# ----------------------------
vec = df[["dx","dy"]].values
norm = np.linalg.norm(vec, axis=1, keepdims=True)
df["ux"] = vec[:, 0] / norm[:, 0]
df["uy"] = vec[:, 1] / norm[:, 0]

# ----------------------------
# 4) Cluster by direction
# ----------------------------
k = 2  # tune: 2~6 typical
kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
df["flow"] = kmeans.fit_predict(df[["ux","uy"]])

# ----------------------------
# 5) Plot: colored vector field + flow line
# ----------------------------
colors = {
    0: "#1f77b4",  # blue
    1: "#d62728",  # red
    2: "#2ca02c",
    3: "#ff7f0e",
    4: "#9467bd",
    5: "#8c564b",
}

plt.figure(figsize=(8,5))

for c in sorted(df["flow"].unique()):
    sub = df[df["flow"] == c]

    # (a) individual vectors (direction-only)
    plt.quiver(
        sub["start_x"], sub["start_y"],
        sub["ux"], sub["uy"],
        angles="xy",
        scale_units="xy",
        scale=0.35,
        width=0.006,
        alpha=0.80,
        color=colors.get(c, "black"),
        label=f"Flow {c}"
    )

    # (b) flow line = mean direction at mean start point (thicker arrow)
    mx, my = sub["start_x"].mean(), sub["start_y"].mean()
    mux, muy = sub["ux"].mean(), sub["uy"].mean()
    plt.arrow(
        mx, my,
        mux, muy,
        width=0.020,
        alpha=0.90,
        color=colors.get(c, "black"),
        length_includes_head=True
    )

plt.title("Customer Path Vector Field (Direction-Normalized)")
plt.xlabel("Store Width (X)")
plt.ylabel("Store Depth (Y)")
plt.axis("equal")       # preserve geometry
plt.legend()
plt.tight_layout()

plt.savefig("customer_vector_field.png", dpi=200)
plt.show()

# ----------------------------
# 6) Output table for Feishu template
# ----------------------------
df.to_csv("customer_paths_with_flow.csv", index=False)
print("Saved: customer_vector_field.png, customer_paths_with_flow.csv")



8119,v_0002,0.0,2.2,7.8,2.1,7.8,-0.1,90.0
8119,v_0003,0.0,9.2,6.9,8.1,6.9,-1.1,180.0
