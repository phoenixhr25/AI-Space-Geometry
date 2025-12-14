
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
$$
\vec{v_i} = (dx_i, dy_i) = (x_{end} - x_{start}, y_{end} - y_{start})
$$


方向相似度由 **余弦相似度** 衡量：
$$
\cos(\theta_{ij}) = \frac{\vec{v_i} \cdot \vec{v_j}}{\|\vec{v_i}\|\|\vec{v_j}\|}
$$


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
8119,v_0002,0.0,2.2,7.8,2.1,7.8,-0.1,90.0
8119,v_0003,0.0,9.2,6.9,8.1,6.9,-1.1,180.0
