# adaboost

> AdaBoost

Adaboost是一种迭代算法, 其核心思想是针对同一个训练集训练不同的分类器(弱分类器), 然后把这些弱分类器集合起来, 构成一个更强的最终分类器(强分类器).

其算法本身是通过改变数据分布来实现的, 它根据每次训练集之中每个样本的分类是否正确, 以及上次的总体分类的准确率, 来确定每个样本的权值. 将修改过权值的新数据集送给下层分类器进行训练, 最后将每次训练得到的分类器最后融合起来, 作为最后的决策分类器.

使用adaboost分类器可以排除一些不必要的训练数据特征, 并将关键放在关键的训练数据上面.
