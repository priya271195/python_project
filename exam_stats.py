def main_of_examstats():
    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

    # for calculating grades
    def print_grades(grades):
        for grade in grades:
            print(grade)
    # for calculating grades_sum
    def grades_sum(grades):
        total = 0
        for grade in grades:
            total += grade
        return total
    # for calculating grades_average
    def grades_average(grades):
        sum_of_grades = grades_sum(grades)
        average = sum_of_grades / float(len(grades))
        return average
    # for calculating grades_variance
    def grades_variance(scores):
        average = grades_average(scores)
        variance = 0
        for score in scores:
            variance += (average-score)**2
        print(variance)

        result = variance/float(len(scores))
        print(result)

        return result

    # for calculating grades_standard_derivation
    def grades_std_deviation(variance):

        return variance **0.5

    print(print_grades(grades))
    print(grades_sum(grades))
    print(grades_average(grades))
    print(grades_variance(grades))
    variance = grades_variance(grades)
    print(grades_std_deviation(variance))
