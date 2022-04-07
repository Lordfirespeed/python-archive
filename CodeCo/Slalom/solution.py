class Slalom:
    def __init__(self):
        self.offsets = []
        self.width = None
        self.halfWidth = None

    @staticmethod
    def round_value_to_4dp(value):
        return round(value, 4)

    def get_closest_side_of_gate(self, skiierOffset, gateCentreOffset):
        if abs(skiierOffset - gateCentreOffset) <= self.halfWidth:
            return skiierOffset
        elif skiierOffset < gateCentreOffset:
            return gateCentreOffset - self.halfWidth
        else:
            return gateCentreOffset + self.halfWidth

    def find_lowest_displacement_through_gates(self):
        skiierOffset = 0
        totalSkiierDisplacement = 0
        for gate in self.offsets:
            newSkiierOffset = self.get_closest_side_of_gate(skiierOffset, gate)
            totalSkiierDisplacement += abs(newSkiierOffset - skiierOffset)
            skiierOffset = newSkiierOffset
        return totalSkiierDisplacement

    def total_displacement(self, offsets, width):
        # Your code goes here
        self.offsets = offsets
        self.width = width
        self.halfWidth = self.width / 2

        result = self.find_lowest_displacement_through_gates()
        roundedResult = self.round_value_to_4dp(result)

        return roundedResult
