from statistics import mean


class invalidScorecardException(Exception):
    pass


class ScoreCard:
    def __init__(self, scoreCardString: str, technicalSectionLength: int, expectedScoreCardLength: int):
        self.scores = [float(num) for num in scoreCardString.split(",")]
        if len(self.scores) != expectedScoreCardLength:
            raise invalidScorecardException

        self.scores = dict(enumerate(self.scores))

        self.scores = {scoreIndex: self.round_to_neartest_quarter(score) for scoreIndex, score in self.scores.items()}

        for checkTechnicalIndex in range(technicalSectionLength):
            if not (-5 <= self.scores[checkTechnicalIndex] <= 5):
                del self.scores[checkTechnicalIndex]

        for checkProgramIndex in range(technicalSectionLength, expectedScoreCardLength):
            if not (0.25 <= self.scores[checkProgramIndex] <= 10):
                del self.scores[checkProgramIndex]

    def __getitem__(self, item):
        return self.scores[item]

    def __repr__(self):
        return f"<ScoreCard{self.scores}>"

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
            thisElementScore = self.score_element_index(elementIndex)
            totalScore += thisElementScore
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


if __name__ == "__main__":
    solver = FigureSkating()

    scorecards = ['-5.0,1.5,-0.75,-1.5,3.75,1.5,8.0,4.5,5.0', '-4.5,2.5,-1.25,-2.75,3.25,1.75,9.25,3.75,7.75', '-3.75,-0.25,0.25,-4.0,4.25,0.25,8.5,3.0,6.0', '-5.0,0.75,-0.75,0.0,3.75,1.5,10.0,2.25,6.0', '-4.5,1.25,-2.0,-1.0,4.75,0.25,10.0,4.5,8.0']
    base_scores = [7.25, 4.75, 5.25, 4, 1.25]

    result = solver.evaluate_score_cards(scorecards, base_scores)
    print(f"Total score: {result}")
