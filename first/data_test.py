import tensorflow as tf

IRIS_TRAINING = 'iris_training.csv'

# dataset = tf.data.experimental.CsvDataset(filenames=IRIS_TRAINING,
#                                           record_defaults=[tf.float32],)
feature_types = [tf.string, tf.string, tf.int32, tf.int32]  # Example feature types
default_values = [1.011241,2.02,3.03]  # Example default values

column_defaults = default_values * 2

# Create a dataset from the CSV file
dataset = tf.data.experimental.CsvDataset(IRIS_TRAINING, default_values, header=True)

# Iterate over the dataset
for record in dataset:
    print(record)  # Process the record as per your requirements