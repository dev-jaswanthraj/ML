import tensorflow as tf
import numpy as np

matrix1 = [[1,3,4],[3,5,3],[4,5,3]]
matrix2 = [[2,5,7],[3,6,8],[2,6,9]]

tf_mat1 = tf.convert_to_tensor(matrix1, dtype='float64')
tf_mat2 = tf.convert_to_tensor(matrix2, dtype='float64')

a = tf.Variable(tf_mat1,)
b = tf.Variable(tf_mat2,)
init = tf.global_variables_initializer()

final_mat1 = tf.matmul(a, b)
determinant1 = tf.matrix_determinant(final_mat1)

b_inv = tf.transpose(b)
final_mat2 = tf.matmul(a, b_inv)

determinant2 = tf.matrix_determinant(final_mat2)
text_file = open("Output.txt", "w")
with tf.Session() as sess:
    sess.run(init)
    with open("Output.txt", "w") as text_file:
        text_file.write("determinant1 %f\n" % sess.run(determinant1))
        text_file.write("determinant2 %f" % sess.run(determinant2))    