from mrjob.job import MRJob
from mrjob.step import MRStep


class ReverseGraph(MRJob):

    def mapper_get_nodes(self, _, line):
        '''
        this mapper yields toNode as key, and fromNode as value.
        :param _: None
        :param line: one line from the input file
        :return: toNode, fromNode
        '''
        #skips the description lines in the beginning
        nodes = line.split()
        if nodes[0] == '#':
            pass
        else:
            yield nodes[1], nodes[0]

    def reducer_return_nodes(self, toNode, fromNode):
        '''
        this reducer yields toNode as key, and a list of all fromNodes corresponding to key as value
        :param toNode: toNode key from mapper
        :param fromNode: fromNode value from mapper
        :return: toNode, list(fromNodeId)
        '''
        yield toNode, list(fromNode)

    def steps(self):
        return [
            MRStep(
                   mapper=self.mapper_get_nodes,
                   reducer=self.reducer_return_nodes
                   )
        ]


if __name__ == '__main__':
    ReverseGraph.run()
