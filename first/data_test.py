import tensorflow as tf

IRIS_TRAINING = 'iris_training.csv'

# dataset = tf.data.experimental.CsvDataset(filenames=IRIS_TRAINING,
#                                           record_defaults=[tf.float32],)
feature_types = [tf.string, tf.string, tf.int32, tf.int32]  # Example feature types
default_values = [1.011241, 2.02, 3.03]  # Example default values

column_defaults = default_values * 2
record_defaults = [tf.constant(0, dtype=tf.int32),         # Column 1 (int)
                   tf.constant(0.0, dtype=tf.float32),      # Column 2 (float)
                   tf.constant(0.0, dtype=tf.float32),      # Column 3 (float)
                   tf.constant(0.0, dtype=tf.float32),      # Column 3 (float)
                   tf.constant(0.0, dtype=tf.float32)]

select_cols = [0,1,2,3]
# Create a dataset from the CSV file
dataset = tf.data.experimental.CsvDataset(IRIS_TRAINING, record_defaults, header= True)

# Iterate over the dataset
print(dataset)
print(type(dataset))

for el in dataset.as_numpy_iterator():
    print(el)