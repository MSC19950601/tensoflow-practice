import tensorflow as tf
import numpy as np

a = tf.placeholder(np.int32, shape=[2], name="my_input")
b = tf.reduce_prod(a, name="prod_b")
c = tf.reduce_sum(a, name="sum_c")

d = tf.add(b, c, name="add_d")

sess = tf.Session()

input_dict = {a: np.array([5, 3], dtype=np.int32)}
print(sess.run(d, feed_dict=input_dict))

writer = tf.summary.FileWriter('./tmp/tensorflow_logs', graph=sess.graph)
