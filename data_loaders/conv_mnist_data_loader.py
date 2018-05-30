from base.base_data_loader import BaseDataLoader
import numpy as np

class ConvMnistDataLoader(BaseDataLoader):
    def __init__(self, config):
        super(ConvMnistDataLoader, self).__init__(config)
        (self.X_train, self.y_train), (self.X_test, self.y_test) = np.load("data/mnist.npy")
        self.X_train = self.X_train.reshape((-1, 28, 28, 1))
        self.X_test = self.X_test.reshape((-1, 28, 28, 1))

    def get_train_data(self):
        return self.X_train, self.y_train

    def get_test_data(self):
        return self.X_test, self.y_test
