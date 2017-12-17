# tensorflow常用函数笔记
>1:创建指定维数的常量填充张量  
tf.fill([row_dim,col_dim],num)  
>2: tf.linespace(start,stop,num)[link](https://www.tensorflow.org/api_docs/python/tf/lin_space)和numpy里的np.linspace()相似。  
>3:tf.range(start,limit,delta)和tf.linespace()相似，不同点是这里指定的是间隔  
>4:random_crop(
    value,
    size,
    seed=None,
    name=None
)张量的随机裁剪  

>5:tf.truncated_normal(
    shape,
    mean=0.0,
    stddev=1.0,
    dtype=tf.float32,
    seed=None,
    name=None
)生成带边界的正态分布随机数  

>6:转换成tensor  
tf.convert_to_tensor(
    value,
    dtype=None,
    name=None,
    preferred_dtype=None
)  
>7:将一个列表转换成矩阵的对角元素  
diag(
    diagonal,
    name=None
)  
>8:求矩阵行列式  
tf.matrix_determinant(
    input,
    name=None
)  
>9:矩阵求逆  
tf.matrix_inverse(
    input,
    adjoint=False,
    name=None
)  
>10:求特征值与特征向量  
tf.self_adjoint_eig(
    tensor,
    name=None
)  
>11:删除张量中维数为1的维度  
tf.squeeze(
    input,
    axis=None,
    name=None,
    squeeze_dims=None
)  
>12:


















