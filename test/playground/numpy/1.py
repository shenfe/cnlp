import numpy as np

print(np.__version__)

# 创建一维数组
arr = np.arange(10)
print(arr)

# 创建二维布尔数组
arr = np.full((3, 3), True, dtype=bool)
print(arr)

# 数组元素筛选
arr = np.array(range(10))
arr2 = arr[arr % 2 == 1]
print(arr2)

# 数组元素替换
arr = np.array(range(10))
arr[arr % 2 == 1] = -1
print(arr)

# 数组变换
arr = np.arange(10)
arr2 = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(arr2)

# 数组拆分
arr = np.arange(10)
arr2 = arr.reshape(2, -1)
print(arr)
print(arr2)

# 数组堆叠（竖直/水平）
arr = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
arr3 = np.concatenate([arr, arr2], axis=0) # / `axis=1`
arr4 = np.vstack([arr, arr2]) # / `hstack`
arr5 = np.r_[arr, arr2] # / `c_`
print(arr3)
print(arr4)
print(arr5)

# 重复、重叠
arr = np.array([1, 2, 3])
arr2 = np.repeat(arr, 3)
arr3 = np.tile(arr, 3)
print(arr2)
print(arr3)

# 数组交集（无重复，集合都是无重复的，下同）
arr3 = np.intersect1d(arr, arr2)

# 数组差集
arr = np.array([1, 2, 3, 2])
arr2 = np.array([1, 3, 4])
arr3 = np.setdiff1d(arr, arr2)
print(arr3)

# 数组比较，获取所有 元素相同的 索引
arr3 = np.where(arr == arr2)

# 数组索引筛选
arr = np.arange(15)
index = np.where((arr >= 5) & (arr <= 10))
arr2 = arr[index]
index = np.where(np.logical_and(arr >= 5, arr <= 10))
arr3 = arr[index]
print(arr2)
print(arr3)

# 向量化运算
def max_of(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

maxes_of = np.vectorize(max_of, otypes=[float])
arr = np.arange(0, 10)
arr2 = np.arange(9, -1, -1)
arr3 = maxes_of(arr, arr2)
print(arr3)

# 列交换
arr = np.arange(9).reshape([3, 3])
arr2 = arr[:, [1, 0, 2]]
print(arr2)

# 行交换
arr = np.arange(9).reshape([3, 3])
arr2 = arr[[1, 0, 2], :]
print(arr2)

# 竖直翻转
arr2 = arr[::-1]
print(arr2)

# 水平翻转
arr2 = arr[:, ::-1]
print(arr2)

# 随机
arr2 = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
print(arr2)
arr3 = np.random.uniform(5, 10, size=(5, 3))
print(arr3)

# 保留制定小数位打印
arr = np.random.uniform(5, 15, size=(3, 3))
np.set_printoptions(precision=3)
print(arr)

# 科学记数法打印
np.random.seed(100)
arr = np.random.random([3, 3]) / 1e3
np.set_printoptions(suppress=True, precision=6)
print(arr)

# 打印时限制元素数量？
arr = np.arange(15)
np.set_printoptions(threshold=10) # `threhold=np.nan`为不限制
print(arr)

# 