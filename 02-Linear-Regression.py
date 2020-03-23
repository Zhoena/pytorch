
import matplotlib.pyplot as plt
import torch
torch.manual_seed(10)

lr = 0.1  # 学习率

# 创建训练数据（20个数据点）
x = torch.rand(20, 1) * 10  # x data(tensor)  shape=(20, 1) 均匀分布
y = 2*x + (5 + torch.randn(20, 1))  # y data(tensor) shape=(20, 1) 标准正态分布 - 加上了一些噪声

# 构建线性回归参数
w = torch.randn((1), requires_grad=True)
b = torch.zeros((1), requires_grad=True)
print(b)

for iteration in range(1000):

    # 前向传播
    wx = torch.mul(w, x)
    y_pred = torch.add(wx, b)

    # 计算 MSE loss
    loss = (0.5 * (y - y_pred) ** 2).mean()  # .mean()为求均值。前面的0.5是为了求导方便

    # 反向传播
    loss.backward()

    # 更新参数
    b.data.sub_(lr * b.grad)
    w.data.sub_(lr * w.grad)

    # 绘图
    if iteration % 20 == 0:

        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), y_pred.data.numpy(), 'r-', lw=5)
        plt.text(2, 20, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.xlim(1.5, 10)
        plt.ylim(8, 28)
        plt.title("Iteration:{}\nw:{} b:{}".format(iteration, w.data.numpy(), b.data.numpy()))
        plt.pause(0.5)

        if loss.data.numpy() < 1:
            break