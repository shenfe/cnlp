# momentum

[SGD](../sgd)方法的一个缺点是，其更新方向完全依赖于当前的batch，因而其更新十分不稳定。解决这一问题的一个简单的做法便是引入momentum。

momentum即动量，它模拟的是物体运动时的惯性，即更新的时候在一定程度上保留之前更新的方向，同时利用当前batch的梯度微调最终的更新方向。

这样一来，可以在一定程度上增加稳定性，从而学习地更快，并且还有一定摆脱局部最优的能力：

$$\Delta x_{t}=\rho \Delta x_{t-1} - \eta g_{t}$$

其中，$\rho$ 即momentum，表示要在多大程度上保留原来的更新方向，这个值在0-1之间，在训练开始时，由于梯度可能会很大，所以初始值一般选为0.5；当梯度不那么大时，改为0.9。$\eta$ 是学习率，即当前batch的梯度多大程度上影响最终更新方向，跟普通的SGD含义相同。$\rho$ 与 $\eta$ 之和不一定为1。

