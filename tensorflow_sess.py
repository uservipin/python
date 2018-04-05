import tensorflow as tf

x1=tf.constant(4)
x2=tf.constant(6)

#result= x1*x2
result = tf.matmul(x1*x2)
print(result)
