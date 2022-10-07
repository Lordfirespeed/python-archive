from collections import defaultdict


class Biathlon:

    @staticmethod
    def find_winners(track, miss_penalty, competitors):
        total_distance = sum(track)
        numToShoot = 5 * (len(track) - 1)

        times = defaultdict(list)

        for competitor in competitors:
            competitorSplit = competitor.split(",")
            competitorID, competitorSpeed, competitorAccuracy = competitorSplit
            competitorMisses = numToShoot // int(competitorAccuracy)
            competitorDistance = total_distance + (competitorMisses * miss_penalty)
            competitorTime = competitorDistance / float(competitorSpeed)
            times[competitorTime].append(int(competitorID))

        winningTime = min(times.keys())
        return sorted(times[winningTime])
