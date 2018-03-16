# linear discriminant analysis

> Linear Discriminant Analysis, 也叫Fisher Linear Discriminant, 线性判别分析, 一种有监督的(supervised)线性降维算法

## lda vs pca

LDA与PCA保持数据信息不同, LDA是为了使得降维后的数据点尽可能地容易被区分.

假设原始数据表示为X, (m*n矩阵, m是维度, n是sample的数量)

既然是线性的, 那么就是希望找到映射向量a, 使得a'X后的数据点能够保持以下两种性质:

1. 同类的数据点尽可能的接近(within class)
1. 不同类的数据点尽可能的分开(between class)

LDA最后也是转化成为一个求矩阵特征向量的问题, 和PCA很像, 事实上很多其他的算法也是归结于这一类, 一般称之为谱(spectral)方法.

