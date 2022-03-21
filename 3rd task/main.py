from mrjob.job import MRJob
from mrjob.step import MRStep
from math import sqrt  # calculate euclidian distance
from sklearn import preprocessing  # normalize dataset
import pandas as pd  # read csv


class KNN(MRJob):

    def __init__(self, args=None):
        super().__init__(args=args)
        '''
        this constructor reads the csv file, normalizes the data with min-max, and splits them into train set and test set
        : reads file using pandas library
        : normalize data using sklearn preprocessing
        : test data: data that we want to classify
        : train data: data that are already classified
        '''
        self.data = pd.read_csv(r"D:\Users\Enxhi\Desktop\Kristi_Fidani_DCSA Project\3rd task\Iris.csv")  # read csv file

        features = self.data[["SepalLengthCm","SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]] # select only feature columns
        feature_scaled = preprocessing.MinMaxScaler().fit_transform(features)  # min-max normalization of features
        self.data[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]] = pd.DataFrame(feature_scaled)  # update data with normalized ones

        # train set
        self.train_data = self.data[self.data['Species'].isnull() == False]
        # test set
        self.test_data = self.data[self.data['Species'].isnull() == True]

    def mapper_get_distance(self, _, line):
        '''
        this mapper calculates the euclidian distance
        :param _: None
        :param line: not used as we read data with pandas
        :return: (test data id, train data id, train data species type) as key , euclidian distance as value
        '''
        for index, row in self.test_data.iterrows():
            for index1, row1 in self.train_data.iterrows():
                euc_dist = ((sqrt(pow((row[1]-row1[1]), 2) + pow((row[2]-row1[2]), 2) + pow((row[3]-row1[3]), 2) + pow((row[4]-row1[4]), 2))))  # euclidian distance formula
                yield (row[0], row1[0], row1[5]), (euc_dist)

    def reducer_get_distance(self, key, val):
        '''
        this reducer removes repetition of data and yield in a different format
        :param key: key coming from the mapper
        :param val: values coming from the mapper
        :return: test data id as key, (train data id, train data species type, euclidian distance) as value
        '''
        yield key[0], (key[1],  key[2],  list(set(val)))

    def reducer_get_neighbors(self, key, val):
        '''
        this reducer sorts the data according to the distance in ascending order and gets top 15 (because for KNN we use K=15)
        :param key: key coming from the reducer
        :param val: values coming from the reducer
        :return: test data id as key, (train data id, train data species type, euclidian distance) as value
        '''
        neighbors = dict()
        neighbors[key] = sorted(val, key=lambda x: x[2], reverse=False)[:15]  # sort by distance in ascending order and get K=15
        yield key, neighbors[key]

    def reducer_classification(self, key, val):
        '''
        this reducer classifies the data by finding the mode of the neighbors list
        :param key: key coming from the reducer
        :param val: values coming from the reducer
        :return: data id as key, classification as value
        '''
        votes = dict()
        for elements in val:
            for el in elements:
                if el[1] not in votes.keys():
                    votes[el[1]] = 1  # assign elements a counter 1
                else:
                    count = votes.get(el[1])
                    # count increments when elements are repeated
                    votes[el[1]] = count+1

        # classified as elements with the highest count in the neighbor list
        yield key, max(votes, key=votes.get)

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_get_distance,
                reducer=self.reducer_get_distance
            ),
            MRStep(
                reducer=self.reducer_get_neighbors
            ),
            MRStep(
                reducer=self.reducer_classification
            )
        ]


if __name__ == '__main__':
    KNN.run()
