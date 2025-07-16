**Task Description**

   - Goal: Find the top 10 common title keywords for each genre. Filter out numbers, auxiliary verbs, etc.
   - Output: Genre with its top keywords and counters.

**Dataset**

   I worked with the _MovieLens_ dataset (`movies.csv`), comprising 60,000+ rows and columns: `movieId`, `title`, and `genres`.

**Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce operations.
   - `re` (Regular Expression): Text pattern matching.
   - `NLTK` (Natural Language Toolkit): Human language data processing.
   - `SimpleJSON`: JSON serialization.

**Solution**

   I implemented a Python class `MovieLens` with map and reduce functions.

   1. **Step 1: Mapper**

      Process lines from `movies.csv`. Data formats vary, so I accessed `movieId`, `title`, and `genres` through effective splitting, handling commas and quotes. Genres and titles are filtered using regex and NLTK stop words. Emits: `[genre, title]`, 1.

   1. **Step 2: Reducer**

      Takes unique genres from Step 1 as keys, `[word, sum]` as values. Unpacks, sorts, and outputs top 10 keywords with JSON serialization.

   This MapReduce workflow effectively extracts insights from complex data structures.

**Execute**  
Please run the following command:

`python main.py movies.csv`
