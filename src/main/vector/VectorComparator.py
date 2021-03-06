import math

import VectorFileHandler
from main.result_handling import ComparisonResult


class VectorComparator:

    # Compares the vector of every article in the corpus to the vectors contained in the two given paths.
    # Calculates the cosine similarity towards both training vectors and returns the comparison results.
    #
    # corpus: corpus of articles with already calculated vectors
    # path_to_training_file_one: path to training vector one
    # path_to_training_file_two: path to training vector two
    @staticmethod
    def compare_corpus_vectors_to_training_vectors(corpus, path_to_training_file_one, path_to_training_file_two):
        comparison_results = list()

        training_vector_one = VectorFileHandler.VectorFileHandler.read_vector_from_file(path_to_training_file_one)
        training_vector_two = VectorFileHandler.VectorFileHandler.read_vector_from_file(path_to_training_file_two)

        for article in corpus:
            comparison_results.append(
                VectorComparator.build_comparison_result(training_vector_one, training_vector_two, article))
        return comparison_results

    def build_comparison_result(reference_vector_one, reference_vector_two, article):
        comparison_result = ComparisonResult.ComparisonResult()
        comparison_result._article_reference = article.id

        comparison_result._orientation_one_name = reference_vector_one.orientation
        comparison_result._orientation_one_similarity = VectorComparator.compare_vectors(reference_vector_one,
                                                                                         article.vector)

        comparison_result._orientation_two_name = reference_vector_two.orientation
        comparison_result._orientation_two_similarity = VectorComparator.compare_vectors(reference_vector_two,
                                                                                         article.vector)

        return comparison_result

    # Calculates the cosine similarity of two vectors
    def compare_vectors(reference_vector, comparison_vector):

        inner_product = reference_vector.indicator_count * comparison_vector.indicator_count
        inner_product += reference_vector.average_sentence_length * comparison_vector.average_sentence_length
        inner_product += reference_vector.average_number_of_subsentences * comparison_vector.average_number_of_subsentences
        inner_product += reference_vector.token_count * comparison_vector.token_count
        inner_product += reference_vector.stopword_to_remaining_words_ratio * comparison_vector.stopword_to_remaining_words_ratio
        inner_product += reference_vector.left_words_counter * comparison_vector.left_words_counter
        inner_product += reference_vector.right_words_counter * comparison_vector.right_words_counter
        inner_product += reference_vector.paratax_hypotax_count * comparison_vector.paratax_hypotax_count
        inner_product += reference_vector.premise_conclusion_count * comparison_vector.premise_conclusion_count

        length_vector1 = VectorComparator.calculate_vector_length(reference_vector)
        length_vector2 = VectorComparator.calculate_vector_length(comparison_vector)

        return math.acos(inner_product / (length_vector1 * length_vector2))

    # Calculate the length of a vector
    @staticmethod
    def calculate_vector_length(vector):
        return math.sqrt(vector.indicator_count * vector.indicator_count +  vector.average_sentence_length *
             vector.average_sentence_length + vector.average_number_of_subsentences * vector.average_number_of_subsentences
        + vector.stopword_to_remaining_words_ratio * vector.stopword_to_remaining_words_ratio
                + vector.left_words_counter * vector.left_words_counter + vector.right_words_counter * vector.right_words_counter + vector.paratax_hypotax_count * vector.paratax_hypotax_count
                         + vector.premise_conclusion_count * vector.premise_conclusion_count + vector.token_count * vector.token_count)

