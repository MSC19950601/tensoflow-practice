import tensorflow as tf

# initialize variables/model parameters
# todo

# define the training loop operations
def inference(X):
    # todo

    return

def loss(X, Y):
    # todo

    return

def inputs():
    # todo
    return X, Y

def train(total_loss):
    # todo

    return

def evaluate(sess, X, Y):
    # todo

    return

saver = tf.train.Saver()

with tf.Session() as sess:

    tf.global_variables_initializer()

    X, Y = inputs()

    total_loss = loss(X, Y)
    train_op = train(total_loss)

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    train_steps = 1000
    for step in range(train_steps):
        sess.run([train_op])
        if step % 10 == 0:
            print("loss: ", sess.run([total_loss]))
        if step % 1000 == 0:
            saver.save(sess, 'my-model', global_step=step)

    evaluate(sess, X, Y)

    coord.request_stop()
    coord.join(threads)
    saver.save(sess, 'my-model', global_step=train_steps)
    sess.close()





