# /usr/bin/env python
# -*- coding: utf-8 -*-
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import math

mnist = input_data.read_data_sets("./MNIST_DATA", one_hot=True)

session = tf.InteractiveSession()

x = tf.placeholder(tf.float32, [None, 784])

w1 = tf.Variable(tf.truncated_normal([784, 100]))
b1 = tf.Variable(tf.zeros([100]))
u1 = tf.matmul(x, w1) + b1
y1 = tf.sigmoid(u1)

w2 = tf.Variable(tf.truncated_normal([100, 10]))
b2 = tf.Variable(tf.zeros([10]))
u2 = tf.matmul(y1, w2) + b2
y2 = tf.nn.softmax(u2)

y = y2
t = tf.placeholder(tf.float32, [None, 10])

loss = tf.reduce_mean(-tf.reduce_sum(t * tf.log(y), reduction_indices=[1]))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train_step = optimizer.minimize(loss)

# 모델 학습
init = tf.initialize_all_variables()
session.run(init)

for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(1000)
  train_step.run({x: batch_xs, t: batch_ys})

# 학습한 모델을 검증
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval({x: mnist.test.images, t: mnist.test.labels}) * 100), '%'
