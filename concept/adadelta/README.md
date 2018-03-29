# adadelta

[Adagrad](../adagrad)算法存在三个问题：

1. 其学习率是单调递减的，训练后期学习率非常小
1. 其需要手工设置一个全局的初始学习率
1. 更新 $x_t$ 时，左右两边的单位不同一

Adadelta针对上述三个问题提出了比较漂亮的解决方案。

首先，针对第一个问题，我们可以只使用adagrad的分母中的累计项离当前时间点比较近的项，如下式：

$$E[g^2]_t = \rho E[g^2]_{t-1} + (1-\rho)g^2_t$$

$$\Delta x_t = - \frac{\eta}{\sqrt{E[g^2]_t+\epsilon}}g_t$$

这里 $\rho$ 是衰减系数，通过这个衰减系数，我们令每一个时刻的 $g_t$ 随之时间按照 $\rho$ 指数衰减，这样就相当于我们仅使用离当前时刻比较近的 $g_t$ 信息，从而使得还很长时间之后，参数仍然可以得到更新。

针对第三个问题，其实sgd跟momentum系列的方法也有单位不统一的问题。sgd、momentum系列方法中：

$${\Delta x 的单位} \propto g的单位 \propto \frac{\partial f}{\partial x} \propto \frac{1}{x的单位}$$