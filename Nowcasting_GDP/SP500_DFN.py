#  Copyright 2018 Rafael Rockenbach da Silva Guimaraes.
#  https://www.deepeconomics.net
#  All Rights Reserved.
#  Based on 'Predict House Prices Regression' by The TensorFlow Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from sklearn import model_selection
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.models import Sequential
import xlrd
import matplotlib.pyplot as plt
print(tf.__version__)

def main(unused_argv):
  # Load dataset and prepare data
  excel = xlrd.open_workbook('SP500_1995_2018.xls') #upload xls
  sheet_0 = excel.sheet_by_index(0) #index 0 = first sheet
  all_data = [[]] #temporary file
  for row_index in range(sheet_0.nrows): #read all rows
    row = []
    for col_index in range(sheet_0.ncols): #read all columns
        value = sheet_0.cell(rowx=row_index,colx=col_index).value
        row.append(value)
    all_data.append(row)
  # Convert to array
  all_raw_data = []
  for f0 in range(1,len(all_data)):
    raw_data = []
    for row in range(len(all_data[f0])):
        value = (all_data[f0])[row]
        raw_data.append(value)
    all_raw_data.append(raw_data)
  dataset = np.array(all_raw_data)
  print("Data shape: {}".format(dataset.shape))

  # Target and Features
  y = dataset[:,0] #target
  print("Target shape: {}".format(y.shape))
  x = dataset[:,1:dataset.shape[1]] #features
  print("Features shape: {}".format(x.shape))

  # Split dataset into train(70%) / test(30%)
  #seed=1
  x_train, x_test, y_train, y_test = model_selection.train_test_split(
    x, y, test_size=0.3)#, random_state=seed)

  # Shuffle the training set
  order = np.argsort(np.random.random(y_train.shape))
  x_train = x_train[order]
  y_train = y_train[order]

  # Model
  def build_model():
      model = Sequential([
          keras.layers.Dense(150, kernel_regularizer=keras.regularizers.l1(0.001),
                             activation=tf.nn.relu, input_shape=(x_train.shape[1],)),
          keras.layers.Dense(100, kernel_regularizer=keras.regularizers.l1(0.001), activation=tf.nn.relu),
          keras.layers.Dense(50, kernel_regularizer=keras.regularizers.l1(0.001), activation=tf.nn.relu),
          keras.layers.Dense(20, kernel_regularizer=keras.regularizers.l1(0.001), activation=tf.nn.relu),
          keras.layers.Dense(1)
      ])

      optimizer = tf.train.ProximalAdagradOptimizer(0.001)

      model.compile(loss='mse',
                   optimizer=optimizer,
                   metrics=['mape'])
      return model

  model = build_model()
  print(model.summary())

  # Train
  print("Training...")
  class PrintDot(keras.callbacks.Callback):
      def on_epoch_end(self,epoch,logs):
          if epoch % 100 == 0: print('')
          print('.', end='')

  EPOCHS = 2500

  #Store training stats
  history = model.fit(x_train, y_train, epochs=EPOCHS,
                     validation_split=0.3, verbose=0,
                     callbacks=[PrintDot()])
  print("Training ends.")

  #Learning curves
  def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('MAPE')
    plt.plot(history.epoch, np.array(history.history['mean_absolute_percentage_error']),
            label='Train Loss')
    plt.plot(history.epoch, np.array(history.history['val_mean_absolute_percentage_error']),
            label='Val Loss')
    plt.legend()
    plt.ylim([0,5])

  plot = plot_history(history)
  plt.savefig('DFN_SP500_learning_curves.png')
  plt.close()

  #MAPE
  [loss, mape] = model.evaluate(x_train, y_train, verbose=0)
  print("Training set Mean Absolute Percentage Error: {:7.2f}".format(mape))
  [loss, mape] = model.evaluate(x_test, y_test, verbose=0)
  print("Testing set Mean Absolute Percentage Error: {:7.2f}".format(mape))

  #graph Output Model X Target
  y_predictions = model.predict(x).flatten()
  time_axis = range(0,y.shape[0])
  plt.xlabel('Time')
  plt.ylabel('Points')
  plt.plot(time_axis, y.T, '-', label='S&P500') #target
  plt.plot(time_axis, y_predictions.T, '-', label='DFN') #model
  plt.legend()
  plt.savefig('DFN_SP500_outputmodel_X_target.png')
  plt.close()

  #graph error
  error = y_predictions - y
  plt.xlabel('Time')
  plt.plot(error, '-', label='error')
  plt.legend()
  plt.savefig('DFN_SP500_error.png')
  plt.close()

  #output model to csv file
  a = np.asarray(y_predictions)
  np.savetxt("DFN_SP500_output.csv", a, delimiter=",")

  print("It is done. Check current directory for saved files.")

if __name__ == '__main__':
  tf.app.run()
