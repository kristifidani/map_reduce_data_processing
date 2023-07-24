# Project Overview
In this project I have used MapReduce in order to solve several tasks including: counting, reverse web-graph link, KNN algorithm and matrix multiplication.  
Each of the tasks has its own dataset and requirements, as explained in the project description file.  
MapReduce is a programming model and implementation which, allows us to process and generate large amounts of data, by splitting them in smaller chunks and performing parallel operations on a cluster e.g., Hadoop.  
All the code is written in Python, by using MRJob framework, which allows us to program with MapReduce.
- Mapper: Takes an input and processes a logical key-value pair to generate a set of intermediate key-values.
- Combiner: Serves as a local reducer for each map.
- Reducer: Merges all intermediate values, associated with the same intermediate key and outputs the result.

The code for the mapper and reducer functions can be written in one single class. We can specify multiple steps that consist of at least one of the functions.

### Task 1
1. Dataset

   For this task I have been working on the Movie Lens dataset. The dataset file name in the project folder is movies.csv. It consists of over sixty thousand rows and three columns: movieId, title and genres.
2. Task description

   As specified in the project description, the goal in this task is to find the top 10 most common keywords in the titles, for each unique genre. Additionally, title words should be filtered to avoid numbers (years), auxiliary verbs, conjunctions, prepositions, and articles as keywords. The output should be each genre and its associated list of the top 10 most used keywords and their counter.
3. Dependencies

   - MRJob and MRStep – Python library for writing MapReduce.
   - RE – Regular Expression Operations.
   - NLTK – Library for human language data processing.
   - SimpleJSON – JSON serializer.
4. Run project command

   - Python main.py movies.csv
5. Solution

   I have created a python class MovieLens that imports MRJob library as a parameter. Inside this class are written all the map and reduce functions needed for this task.
   1. First step:
      - Mapper
        takes as a parameter key: None, and value: each line of the input file. In this case movies.csv.
        Since the data in the dataset has not a fixed format, I have accessed each data of the row according to their columns, by splitting the line. Most of the data have a comma separation between them, so I have split the line with comma. Some other data have nested quotations or other special characters. Therefore, I checked the length of line with split by comma and if it is not three (each column), I split the line by quotes. In this way I have access equally to all the data in the dataset, regardless of their format and I unpacked each line according to the columns: movieId, title, genres.
        Afterwards, I filtered the genres with a regular expression that matches only letters, spaces, and lines. Additionally, I needed to also filter the titles. I made another regular expression that matches only letters and I used NLTK library stop words as suggested in the project task description. It ignores all the common words in English such as: “the”, “a”, “in” etc. I also used the function isalnum, which removes the
special characters. Furthermore, I filtered only the title words that have a length of higher than two, so that I could pick up more significant keywords.
This mapper yields a list of genres and title words as key, and a count of 1 for each as value. The format is: [genre, title], 1.
    2. Second step:

       - Reducer takes as a parameter key: all the unique genres obtained from the first step and as value [word, sum]. This reducer unpacks the values and sorts dhe list.
Since the value is of type generator, I have used simplejson, in order to serialize it as JSON and perform the sorting in descending order, according to the count. I have outputted only the top 10 most common title keywords in descending order for each genre.
Reducer Final Output

### Task 2
1. Dataset

   For this task I have worked with the Google Web Graph dataset. In the project folder it has the name web-Google.txt. This dataset consists of a very large number of rows that have unordered node pairs: FromNodeId – ToNodeId. In total there are 875713 Nodes and 5105039 Edges. Nodes represent web pages and edges represent hyperlinks between them.
2. Task description

   As specified in the project description, the goal is to reverse the web-link graph from the given dataset. The output should be each node and its corresponding list of other nodes linking to them.
3. Dependencies
   - MRJob and MRStep – Python library for writing MapReduce.
4. Run project command
   - Python main.py web-Google.txt
5. Solution

   I have created a python class ReverseGraph that imports MRJob library as a parameter. Inside this class are written all the map, reduce functions needed for this task. It has only one step.
   1. Mapper takes as a parameter key: None, and value: each line of the input file. In this case web-Google.txt.
The data format is really simple. There are only two columns divided by empty spaces. Therefore, I split each line by the empty spaces and skipped the first couple of lines that describe the dataset. I got a good understanding of the functions input and output by looking at the hand notes that professor Deligiannis has posted on canvas.
This mapper yields in reverse order: toNode as key and fromNode as value.
   2. Reducer takes as parameter key: toNode and as a value: fromNode generated from the mapper.
Yields toNode as a key and its corresponding list of all nodes linking to it as value. Yield: toNode, list(fromNode). In simpler terms, all the nodes in the list are links to the node in the key.

### Task 3
1. Dataset

   For this task I have worked with the Iris dataset, which in the project folder has the name Iris.csv. This dataset consists of four features that were measured for three Iris species. In total there are 150 rows and 6 columns: Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm and Species classification.
2. Task description

   There are some Iris in the dataset that are not classified. As specified in the project description, the goal is to classify those unknown species based on the four features, by implementing the k-nearest neighbours (KNN) algorithm with K=15. To measure the distance in KNN we will use the Euclidian distance.
The output should be the Id of the unknown species associated by our result classification.
3. Dependencies
   - MRJob and MRStep – Python library for writing MapReduce.
   - Math (sqrt) – built in function to calculate the mathematical operations.
   - Sklearn (preprocessing) – Library for normalizing dhe dataset.
   - Pandas – Popular library for reading .csv file.
4. Run project command
   - Python main.py Iris.csv
5. Solution

   I have created a python class KNN that imports MRJob library as a parameter. Inside this class are written all the map and reduce functions needed for this task.
   1. Constructor

      As a starter, I have created a class constructor in order to read the csv file with pandas and store them in constructor variables. This way I can access the data anywhere in the code. Pandas returns a data frame that makes it easier to access the data, either by rows or columns. With Pandas you need to specify the absolute file path in order to access it. Therefore, you need to put your own device’s absolute file path in order to work. Since, I don’t need to normalize all the columns, I selected only the feature columns and passed them to sklearn pre-processing MinMaxScaler function, to normalise the dataset. All the data now are scalable from 0 to 1, where 0 is the minimum value and 1 is the maximum value.
      Finally, I have split the data into training and testing set. Testing data consists of the Iris species that are not classified, while training data consists of the Iris species that are already classified.

    2. First step:
       1. Mapper takes as parameter key: None and as parameter value: line but in this case I have not used it, since I read the dataset with Panda’s library.
         This mapper calculates the Euclidian distance by iterating over the test and train data.
         Returns (test data id, train data id, train data species) as key and Euclidian distance as value.

        2. Reducer takes as parameter keys and values coming from the mapper. It removes data repetitions and returns them in a different format.
         Yield: test data id as key, (train data id, train data species, Euclidian distance) as value.

     3. Second step:

        Reducer takes as parameter key and value coming from the first step. It sorts the data according to the distance in ascending order and gets top 15 neighbours, since it was specified in the task that K=15.
        Yield: test data id as key and (train data id, train data species, Euclidian distance) as value.

     5. Third step:

        Reducer takes as parameter key and value coming from the second step. It classifies the unknown species by finding the mode of the neighbours list.
        I have iterated over the list of neighbours, and I have counted which of the species type is repeated the most. Therefore, the feature with the highest count number will be the classification for the unknown data. Yield: test data id, classification.


### Task 4
1. Dataset

   For this task I have worked with a matrix dataset, which in the project folder has the name A.txt. This dataset consists of 1000 rows and 50 columns.
2. Task description

   As specified in the project description, the goal of this task is te calculate the Frobenius norm of the matrix with the given formula:
   We are required to calculate the sum of the squares of the elements on the same row in one reducer and calculate the Frobenius norm in another reducer.
3. Dependencies  
    - MRJob and MRStep – Python library for writing MapReduce.
    - Math – built in function to perform mathematical operations.
4. Run project command

    - Python main.py A.txt
5. Solution

I have created a python class, FrobeniusNorm that imports MRJob library as a parameter. Inside this class are written all the map and reduce functions needed for this task.  
  1. First step:
     - Mapper - takes as parameter key: None and as parameter value: each line of the dataset.
       Each of the data is separated by an empty space. Therefore, I have split the line into empty spaces in order to access each element.
       Yield: row items, None.
     - Reducer takes as parameters key: row items coming from the mapper and as value: none. Sums the absolute value of all elements in a row, in power of 2.
       Yield: None, row sum

   2. Second step:

      Reducer – takes as parameter key: none and as a value: sum of the absolute values of all elements in a row, in power of 2.  
      Returns: ‘Forbenius Norm is: ‘, Frobenius Norm.
