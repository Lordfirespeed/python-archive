from statistics import mean


class invalidScorecardException(Exception):
    pass


class ScoreCard:
    def __init__(self, scoreCardString: str, technicalSectionLength: int, expectedScoreCardLength: int):
        self.scores = [float(num) for num in scoreCardString.split(",")]
        if len(self.scores) != expectedScoreCardLength:
            raise invalidScorecardException

        self.scores = dict(enumerate(self.scores))

        for checkTechnicalIndex in range(technicalSectionLength):
            if not (-5 <= self.scores[checkTechnicalIndex] <= 5):
                del self.scores[checkTechnicalIndex]

        for checkProgramIndex in range(technicalSectionLength, expectedScoreCardLength):
            if not (0.25 <= self.scores[checkProgramIndex] <= 10):
                del self.scores[checkProgramIndex]

        self.scores = {scoreIndex: self.round_to_neartest_quarter(score) for scoreIndex, score in self.scores.items()}

    def __getitem__(self, item):
        return self.scores[item]

    @staticmethod
    def round_to_neartest_quarter(floatNumber: float):
        return round(floatNumber * 4) / 4


class FigureSkating:
    def __init__(self):
        self.technicalSectionLength = None
        self.totalExpectedScorecardLength = None
        self.scoreCardObjects = []
        self.baseScores = []

    def evaluate_score_cards(self, scorecards: [str], base_scores: [float]):
        self.technicalSectionLength = len(base_scores)
        self.totalExpectedScorecardLength = self.technicalSectionLength + 4
        self.create_score_card_objects(scorecards)
        self.baseScores = base_scores

        return self.sum_total_score()

    def sum_total_score(self):
        totalScore = 0
        for elementIndex in range(self.totalExpectedScorecardLength):
            totalScore += self.score_element_index(elementIndex)
        return round(totalScore, 4)

    def create_score_card_objects(self, scoreCardStrings: [str]):
        for scoreCardString in scoreCardStrings:
            try:
                self.scoreCardObjects.append(ScoreCard(scoreCardString, self.technicalSectionLength, self.totalExpectedScorecardLength))
            except invalidScorecardException:
                pass

    def score_element_index(self, elementIndex):
        judgeScores = []
        for judgeScoreCard in self.scoreCardObjects:
            try:
                judgeScores.append(judgeScoreCard[elementIndex])
            except KeyError:
                pass

        self.remove_highest_and_lowest(judgeScores)

        notInTechnicalSection = elementIndex >= self.technicalSectionLength
        baseScore = 0 if notInTechnicalSection else self.baseScores[elementIndex]

        if len(judgeScores) == 0:
            if notInTechnicalSection:
                return 5
            else:
                return baseScore

        return baseScore + mean(judgeScores)

    @staticmethod
    def remove_highest_and_lowest(scoreArray: [float]):
        if len(scoreArray) > 2:
            scoreArray.sort()
            scoreArray.pop(0)
            scoreArray.pop(-1)

        return scoreArray
