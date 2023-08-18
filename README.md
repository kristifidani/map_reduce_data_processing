# MapReduce Solutions for Diverse Data Tasks

### Project Overview

In this project, I've harnessed the power of MapReduce to tackle a variety of tasks:  

1. **Encompass counting**
2. **Reverse web-graph link analysis**
3. **K-Nearest Neighbors (KNN) algorithm**
4.  **Matrix multiplication**.

Each task is associated with its unique dataset and specific requirements, all meticulously detailed in the project description.

Utilizing the MapReduce programming paradigm, I've efficiently processed substantial volumes of data by breaking them into manageable chunks and orchestrating parallel operations on a cluster, exemplified by technologies such as Hadoop. My implementation leverages the MRJob framework, a powerful tool that empowers seamless programming with the MapReduce model in Python.

**Key Aspects:**

- **Mapper**: Transforms input data into logical key-value pairs, generating a collection of intermediate key-values.
- **Combiner**: Acts as a localized reducer for each map operation, optimizing intermediate data processing.
- **Reducer**: Aggregates intermediate values linked with the same key, culminating in the desired outcome.

This project integrates mapper and reducer functions within a unified class, offering a streamlined and coherent approach. The flexibility to define multiple steps, each composed of at least one function, facilitates a comprehensive data processing pipeline that can be tailored to the intricacies of the tasks at hand.

### Task 1

1. **Dataset**

   I worked with the Movie Lens dataset (`movies.csv`), comprising 60,000+ rows and columns `movieId`, `title`, and `genres`.

1. **Task Description**

   - Goal: Find top 10 common title keywords for each genre. Filter out numbers, auxiliary verbs, etc.
   - Output: Genre with its top keywords and counters.

1. **Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.
   - `re` (Regular Expression): Text pattern matching.
   - `NLTK` (Natural Language Toolkit): Human language data processing.
   - `SimpleJSON`: JSON serialization.

1. **Solution**

   I implemented a Python class `MovieLens` with map and reduce functions.

   1. **Step 1: Mapper**

      Process lines from `movies.csv`. Data formats vary, so I accessed `movieId`, `title`, and `genres` through effective splitting, handling commas and quotes. Genres and titles are filtered using regex and NLTK stop words. Emits: `[genre, title]`, 1.

   1. **Step 2: Reducer**

      Takes unique genres from Step 1 as keys, `[word, sum]` as values. Unpacks, sorts, and outputs top 10 keywords with JSON serialization.

   This MapReduce workflow effectively extracts insights from complex data structures.

### Task 2

1. **Dataset**

   Utilized Google Web Graph dataset (`web-Google.txt`) containing 875,713 Nodes and 5,105,039 Edges representing web pages and hyperlinks.

1. **Task Description**

   - Goal: Reverse the web-link graph.
   - Output each node along with its linked nodes.

1. **Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.

1. **Solution**

   I designed a Python class `ReverseGraph` with map and reduce functions for this one-step task.

   - **Mapper**

     Process each line from `web-Google.txt`. The data format is simple with two columns divided by spaces. After splitting, I ignored initial dataset description lines. The mapper emits reversed key-value pairs: `toNode` as key and `fromNode` as value.

   - **Reducer**

     Process mapper output. For each `toNode`, collect its associated `fromNode` values as a list. The final output presents each `toNode` followed by a list of linked nodes.

This streamlined MapReduce approach effectively reverses the web-link graph.

### Task 3

1. **Dataset**

   Used the Iris dataset (`Iris.csv`) with 150 rows and 6 columns, including features like `SepalLengthCm` and species classification.

1. **Task Description**

   - Goal: Classify unknown Iris species using the k-nearest neighbors (KNN) algorithm (K=15).
   - Measure distances with Euclidean distance. Output: Id of unknown species and its predicted classification.

1. **Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.
   - `Math.sqrt`: Built-in function for math operations.
   - `Sklearn.preprocessing`: Library for dataset normalization.
   - `Pandas`: Popular library for CSV reading.

1. **Solution**

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

### Task 4

1. **Dataset**

   Used matrix dataset `A.txt` with 1000 rows and 50 columns.

1. **Task Description**

   - Goal: Calculate the Frobenius norm of the matrix using a MapReduce approach. The norm is calculated by summing the squares of elements in the same row in one reducer and computing the Frobenius norm in another reducer.
   - Output Frobenius norm

1. **Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.
   - `Math`: Built-in function for mathematical operations.

1. **Solution**

   Implemented a Python class `FrobeniusNorm` with map and reduce functions.

   - **Step 1: Mapper**

      Split each line into elements using empty spaces. Emit row items as key, None as value.

   - **Step 1: Reducer**

      Calculate the sum of absolute values of elements in a row, raised to power 2. Emit None as key and row sum.

   - **Step 2: Reducer**

      Calculate the square root of the sum of squared row sums (Frobenius norm). Emit Frobenius norm.

   This MapReduce approach efficiently computes the Frobenius norm of the matrix.

### Conclusion

Utilizing the MapReduce paradigm, this project showcases the power of parallel processing for solving a range of tasks, from keyword extraction to graph analysis and classification. The provided solutions leverage the MRJob framework and Python libraries to efficiently process large datasets, demonstrating the capabilities of MapReduce in a diverse set of applications.

Feel free to explore the code and adapt the provided solutions to your specific needs.

