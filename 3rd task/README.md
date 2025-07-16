**Task Description**

   - Goal: Classify unknown Iris species using the k-nearest neighbors (KNN) algorithm (K=15).
   - Measure distances with Euclidean distance. Output: Id of unknown species and its predicted classification.

**Dataset**

   Used the Iris dataset (`Iris.csv`) with 150 rows and 6 columns, including features like `SepalLengthCm` and species classification.

**Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.
   - `Math.sqrt`: Built-in function for math operations.
   - `Sklearn.preprocessing`: Library for dataset normalization.
   - `Pandas`: Popular library for CSV reading.

**Solution**

   I implemented a Python class `KNN` with map and reduce functions.

   - **Constructor**

      Read CSV file using Pandas, store data for access, and normalize feature columns with `MinMaxScaler`. Split data into training and testing sets.

   - **Step 1: Mapper**

      Calculate Euclidean distance between test and train data. Emit `(test_id, train_id, train_species)` as key and distance as value.

   - **Step 1: Reducer**

      Remove data repetitions and emit `(test_id, train_id, train_species, distance)`.

   - **Step 2: Reducer**

      Sort data by distance, get top 15 neighbors. Emit `(test_id, train_id, train_species, distance)`.

   - **Step 3: Reducer**

      Classify unknown species by finding mode of neighbors' species. Emit `test_id, classification`.

This MapReduce approach efficiently classifies unknown Iris species.

**Execute**  
Please run the following command:

`python main.py Iris.csv`

Before running:

With Pandas you need to specify the absolute file path that you are trying to access. Therefore, you need to put your own device’s absolute file path in order to run without errors.
