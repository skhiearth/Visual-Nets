import keras
from keras.models import Sequential
from keras.layers import Dense


class SequentialModel:
    model = Sequential()

    def create(self):
        print("Create")

    def addInputLayer(self):
        print("Add")

    @staticmethod
    def removeAllModels():
        print("Clearing Session")
        keras.backend.clear_session()
