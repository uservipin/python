import tensorflow as tf
x1 = tf.constant(3)
x2 = tf.constant(4)

result=x1*x2
#res = tf.mul(x1,x2)
#sess=tf.Session()
#print(sess.run(result))
print(result)

with tf.Session() as sess:
	output = sess.run(result)
	print(output)

print(output)