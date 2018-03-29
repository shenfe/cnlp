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

针对第三个问题，其实[sgd](../sgd)跟[momentum](../momentum)系列的方法也有单位不统一的问题。sgd、momentum系列方法中：

$$\Delta x \text{的单位} \propto g \text{的单位} \propto \frac{\partial f}{\partial x} \propto \frac{1}{x \text{的单位}}$$

类似的，adagrad中，用于更新$\Delta x$的单位也不是x的单位，而是1。

而对于牛顿迭代法：

$$\Delta x = H^{-1}_t g_t$$

其中H为Hessian矩阵，由于其计算量巨大，因而实际中不常使用。其单位为：

$$\Delta x \propto H^{-1}g \propto \frac{\frac{\partial f}{\partial x}}{\frac{\partial ^2 f}{\partial ^2 x}} \propto x \text{的单位}$$

注意，这里f无单位。因而，牛顿迭代法的单位是正确的。

所以，我们可以模拟牛顿迭代法来得到正确的单位。注意到：

$$\Delta x = \frac{\frac{\partial f}{\partial x}}{\frac{\partial ^2 f}{\partial ^2 x}} \Rightarrow \frac{1}{\frac{\partial ^2 f}{\partial ^2 x}} = \frac{\Delta x}{\frac{\partial f}{\partial x}}$$

这里，在解决学习率单调递减的问题的方案中，分母已经是 $\frac{\partial f}{\partial x}$ 的一个近似了。这里我们可以构造 $\Delta x$ 的近似，来模拟得到 $H^{-1}$ 的近似，从而得到近似的牛顿迭代法。具体做法如下：

$$\Delta x_t = - \frac{\sqrt{E[\Delta x^2]_{t-1}}}{\sqrt{E[g^2]_t+\epsilon}}g_t$$

可以看到，如此一来adagrad中分子部分需要人工设置的初始学习率也消失了，从而顺带解决了上述的第二个问题。

另一篇比较adagrad和adadelta的[文章](https://blog.csdn.net/joshuaxx316/article/details/52062291)。

