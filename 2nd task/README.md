**Task Description**

   - Goal: Reverse the web-link graph.
   - Output each node along with its linked nodes.

**Dataset**

   Utilized _Google Web Graph_ dataset (`web-Google.txt`) containing `875,713` Nodes and `5,105,039` Edges representing web pages and hyperlinks.

**Dependencies**

   - `MRJob` and `MRStep`: Python libraries for MapReduce.

**Solution**

   I designed a Python class `ReverseGraph` with map and reduce functions for this one-step task.

   - **Mapper**

     Process each line from `web-Google.txt`. The data format is simple with two columns divided by spaces. After splitting, I ignored initial dataset description lines. The mapper emits reversed key-value pairs: `toNode` as key and `fromNode` as value.

   - **Reducer**

     Process mapper output. For each `toNode`, collect its associated `fromNode` values as a list. The final output presents each `toNode` followed by a list of linked nodes.

This streamlined MapReduce approach effectively reverses the web-link graph.

**Execute**  
Please run the following command:

`python main.py web-Google.txt`
