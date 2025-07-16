**Task Description**

   - Goal: Calculate the Frobenius norm of the matrix using a MapReduce approach. The norm is calculated by summing the squares of elements in the same row in one reducer and computing the Frobenius norm in another reducer.
   - Output Frobenius norm

**Dataset**

   Used matrix dataset `A.txt` with 1000 rows and 50 columns.

**Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.
   - `Math`: Built-in function for mathematical operations.

**Solution**

   Implemented a Python class `FrobeniusNorm` with map and reduce functions.

   - **Step 1: Mapper**

      Split each line into elements using empty spaces. Emit row items as key, None as value.

   - **Step 1: Reducer**

      Calculate the sum of absolute values of elements in a row, raised to power 2. Emit None as key and row sum.

   - **Step 2: Reducer**

      Calculate the square root of the sum of squared row sums (Frobenius norm). Emit Frobenius norm.

   This MapReduce approach efficiently computes the Frobenius norm of the matrix.

**Execute**  
Please run the following command:

`python main.py A.txt`
