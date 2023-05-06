# Importing the desired library
import tensorflow as tf

class Basic(object):

    def __init__(self):
        # Initializing the variagble and constants
        self.a1 = tf.constant([4, 3, 2, 1])
        self.a2 = tf.constant([1, 3, 4, 7])

        # Placeholders for performing the computation
        self.res = tf.multiply(self.a1, self.a2)

    def step1(self):
        #Initializing a Session on CPU or GPU
        sess = tf.Session()
        #Performing the computation
        result = sess.run(self.res)
        #Display result
        print(result)
        #Close Session
        sess.close()

    def step2(self):
        #Initializing a Session on CPU or GPU, Performing the computation, Display result, Close Session.
        with tf.Session() as sess:
            finalOutput = sess.run(self.res)
            print(finalOutput)

if __name__ == "__main__":
    obj = Basic()
    obj.step1()
    obj.step2()