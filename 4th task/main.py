from mrjob.job import MRJob
from mrjob.step import MRStep

import math

class FrobeniusNorm(MRJob):

    def mapper_get_elements(self, _, line):
        '''
        this mapper yields all elements in a row
        :param _: None
        :param line: one line from the input file
        :return: row_items, None
        '''
        row_items = line.split()
        yield row_items, None

    def reducer_row_sum(self, row_items, _):
        '''
        this reducer sums the absolute value of all elements in a row, in power of 2
        :param row_items: all items of each row coming from mapper 
        :param _: None
        :return: None, row_sum
        '''
        row_sum = 0
        for element in row_items:
            row_sum += math.pow(abs(float(element)), 2)
        yield None, row_sum

    def reducer_get_frobenius(self, _, row_sum):
        '''
        this reducer sums the results from the previous reducer and calculates the Frobenius Norm
        :param _: None
        :param row_sum: sum of all elements in a row coming from the previous reducer
        :return: "Frobenius Norm is: ", row_sum
        '''
        f_norm = 0
        for element in row_sum:
            f_norm += element
        yield 'Frobenius Norm is: ', math.sqrt(f_norm)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_elements,
                   reducer=self.reducer_row_sum
                   ),
            MRStep(reducer=self.reducer_get_frobenius,
                   )
        ]


if __name__ == '__main__':
    FrobeniusNorm.run()
