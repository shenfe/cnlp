# ln norm

> 范数

L0范数(L0 norm), 是指向量中非0的元素的个数.

L1范数, 是指向量中各个元素绝对值之和, 也叫"稀疏规则算子"(Lasso regularization).
例如, 向量A=[1, -1, 3], 那么A的L1范数为 |1|+|-1|+|3|.

L2范数为向量中各个元素平方和的1/2次方, L2范数又称Euclidean范数或Frobenius范数. 在回归里面, 有人把有它的回归叫"岭回归"(Ridge Regression), 有人也叫它"权值衰减weight decay". 它的强大功效是改善机器学习的过拟合问题.

Lp范数为向量中各个元素绝对值p次方和的1/p次方.

在支持向量机学习过程中, L1范数实际是一种对于成本函数求解最优的过程, 因此, L1范数正则化通过向成本函数中添加L1范数, 使得学习得到的结果满足稀疏化, 从而方便人类提取特征.

L1范数可以使权值稀疏, 方便特征提取. L2范数可以防止过拟合, 提升模型的泛化能力.

L1正则先验服从拉普拉斯分布, L2正则先验服从高斯分布.

