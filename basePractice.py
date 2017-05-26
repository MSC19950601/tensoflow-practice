import tensorflow as tf

graph = tf.Graph()

with graph.as_default():

    with tf.name_scope("variable"):
        global_step = tf.Variable(0, dtype= tf.int32, trainable= False, name= "global_step")
        total_output = tf.Variable(0.0, dtype= tf.float32, trainable= False, name= "total_output")

    with tf.name_scope("transformation"):
        with tf.name_scope("input"):
            a = tf.placeholder(tf.float32, shape= [None], name= "input_placeholder_a")

        with tf.name_scope("intermediate_layer"):
            b = tf.reduce_prod(a, name="product_b")
            c = tf.reduce_sum(a, name="sum_c")

        with tf.name_scope("output"):
            output = tf.add(b, c, name="output")

    with tf.name_scope("update"):
        update_total = total_output.assign_add(output)
        increment_step = global_step.assign_add(1)

    with tf.name_scope("summaries"):
        avg = tf.div(update_total, tf.cast(increment_step, tf.float32), name= "average")
        tf.summary.scalar(b'Output', output, name= "output_summary")
        tf.summary.scalar(b'Sum of outputs over time', output, name="total_summary")
        tf.summary.scalar(b'Output', output, name="output_summary")


    with tf.name_scope("global_ops"):

sess = tf.Session(graph=graph)
