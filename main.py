class MetricsProvider:
    def __init__(self):
        pass

    def provideAccuracy(self, confusion_matrix: list)->float:
        true_positive: int = confusion_matrix[0]
        false_positive: int = confusion_matrix[1]
        false_negative: int = confusion_matrix[2]
        true_negative: int = confusion_matrix[3]
        return (
            (true_positive + true_negative) / 
            (true_positive + false_positive + false_negative + true_negative)
            )

    def providePrecision(self, confusion_matrix: list)->float:
        true_positive: int = confusion_matrix[0]
        false_positive: int = confusion_matrix[1]
        return true_positive / (true_positive + false_positive)

    def provideRecall(self, confusion_matrix: list)->float:
        true_positive: int = confusion_matrix[0]
        false_negative: int = confusion_matrix[2]
        return true_positive / (true_positive + false_negative)

    def provideF_score(self, confusion_matrix: list, beta: float = 1)->float:
        return (
            (1 + beta ** 2) * 
            self.providePrecision(confusion_matrix) * 
            self.provideRecall(confusion_matrix) / 
            (beta ** 2 * self.providePrecision(confusion_matrix) + 
            self.provideRecall(confusion_matrix))
            )

    

class MetrixPrinter:
    def __init__(self):
        pass

    def print_all_metrix(self, confusion_matrix: list):
        metricsProvider: MetricsProvider = MetricsProvider()

        accuracy: float = metricsProvider.provideAccuracy(confusion_matrix)
        precition: float = metricsProvider.providePrecision(confusion_matrix)
        recall: float = metricsProvider.provideRecall(confusion_matrix)
        F_score: float = metricsProvider.provideF_score(confusion_matrix)
        print(
            'Accuracy: ' + str(accuracy) + '\n' 
            'Precition: ' + str(precition) + '\n' 
            'Recall: ' + str(recall) + '\n' 
            'F-score: ' + str(F_score) + '\n' 
            )

def main()->int:
    true_positive: int = 50
    false_positive: int = 100
    false_negative: int = 50
    true_negative: int = 900
    confusion: list = [true_positive, false_positive, false_negative, true_negative]

    metrixPrinter: MetrixPrinter = MetrixPrinter()
    metrixPrinter.print_all_metrix(confusion)

    true_positive: int = 1
    false_positive: int = 1
    false_negative: int = 100
    true_negative: int = 998
    confusion: list = [true_positive, false_positive, false_negative, true_negative]

    metrixPrinter.print_all_metrix(confusion)

    return 0

main()
