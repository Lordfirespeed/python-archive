from datetime import timedelta
from math import hypot


class Ceremony:
    def __init__(self, ceremonyString):
        x, y, timeString = ceremonyString.split(",")
        self.x = int(x)
        self.y = int(y)

        hour, minute = timeString.split(":")
        self.time = timedelta(hours=int(hour), minutes=int(minute))

    def __abs__(self):
        return hypot(self.x, self.y)

    def distance_to(self, otherCeremony):
        if type(otherCeremony) is not Ceremony:
            raise TypeError
        xdiff, ydiff = abs(self.x - otherCeremony.x), abs(self.y - otherCeremony.y)
        return hypot(xdiff, ydiff)


class MedalCeremony:
    interviewDuration = timedelta(minutes=15)
    ceremonyDuration = timedelta(minutes=45)

    def __init__(self):
        self.ceremonies = []
        self.interviews = 0

    def initialise_ceremonies(self, ceremonyStrings):
        self.ceremonies = [Ceremony(ceremonyString) for ceremonyString in ceremonyStrings]

    def count_possible_interviews(self, ceremonies):
        self.initialise_ceremonies(ceremonies)
        self.simulate_ceremonies()

        return self.interviews

    def simulate_ceremonies(self):
        for currentCeremony, nextCeremony in zip(self.ceremonies[:-1], self.ceremonies[1:]):
            currentCeremonyEndTime = currentCeremony.time + self.ceremonyDuration
            timeTakenViaInterviewBuilding = timedelta(minutes=abs(currentCeremony) + abs(nextCeremony))
            timeAllowed = nextCeremony.time - currentCeremonyEndTime

            if timeTakenViaInterviewBuilding < timeAllowed:
                interviewTime = timeAllowed - timeTakenViaInterviewBuilding
                self.interviews += interviewTime // self.interviewDuration


if __name__ == "__main__":
    pass
