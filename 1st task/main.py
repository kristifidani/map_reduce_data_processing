from mrjob.job import MRJob
from mrjob.step import MRStep

import re
from nltk.corpus import stopwords #remove certain words

import simplejson as json #JSON serializer

WORD_RE = re.compile(r"[a-zA-Z]+")  # match only letters 
GENRE_RE = re.compile(r"[a-zA-Z\s\-]+") #match letters, spaces and -


class MovieLens(MRJob):
    
    def mapper_get(self, _, line):
        '''
        this mapper yields a list of genres and titles as key, and a list of count = 1 for each as value
        :param _: None
        :param line: one line from the input file
        :return: [genre, title], 1
        '''
        #line split with , or "" according to the line format
        if len(line.split(',')) == 3:
            movieId, title_list, genres = line.split(',')
        else:
            movieId, title_list, genres = line.split('"')

        #match genres 
        genre_list = GENRE_RE.findall(genres)

        #iterate through genres and titles
        for genre in genre_list:
            if genre.lower() == "genres": #avoid 1st line (label) 
                continue
            else:
                for title in WORD_RE.findall(title_list): #match titles
                    if title.casefold() not in set(stopwords.words("english")) and title.isalnum() and len(title) > 2: #filter titles (stopwords, special characters, length)
                        yield [genre, title], 1

    def combiner_count(self, genres, counts):
        '''
        this combiner sums locally the title words we've seen so far for each genre
        :param genres: [genre, title] obtained from the mapper
        :param counts: 1
        :return: ([genre, title], sum)
        '''
        yield genres, sum(counts)

    def reducer_count(self, genres, counts):
        '''
        this reducer sums the title words we've seen so far for each genere
        :param genres: [genre, title] obtained from the combiner
        :param counts: the number of occurrences of the word from the result of the combiner
        :return: genre[0]-genre, (genres[1]-word, sum)
        '''
        yield genres[0], (genres[1], sum(counts))

    def reducer_sort(self, genres, counts):
        '''
        2nd step reducer. Unpacks the values and sorts list
        :param genres: all genres obtained from 1st step
        :param counts: [word, sum]
        :return: genre, [[word, sum]]
        '''
        #JSON serializer of generator
        yield genres, json.dumps(
            #unpack values and sort the array in descending order. Returns only the first ten elements
            ((title, count) for title, count in sorted(counts, key=lambda x: x[-1], reverse=True)[:10]),
            iterable_as_array=True
        )

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_get,
                combiner=self.combiner_count,
                reducer=self.reducer_count
            ),
            MRStep(
                reducer=self.reducer_sort
            )
        ]


if __name__ == '__main__':
    MovieLens.run()
