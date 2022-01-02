class Yatzy:

    @staticmethod
    def chance(roll_list):
        total = 0
        for roll in roll_list:
            total += roll
        return total


    @staticmethod
    def yatzy(roll_list):
        for roll in roll_list:
            if roll_list[0] != roll:
                return 0
        return 50
    

    @staticmethod
    def ones(roll_list):
        sum = 0
        for roll in roll_list:
            if roll == 1:
                sum += roll
        return sum
    

    @staticmethod
    def twos(roll_list):
        sum = 0
        for roll in roll_list:
            if roll == 2:
                sum += roll
        return sum
    

    @staticmethod
    def threes(roll_list):
        sum = 0
        for roll in roll_list:
            if roll == 3:
                sum += roll
        return sum
    

    @staticmethod
    def fours(roll_list):
        sum = 0
        for roll in roll_list:
            if roll == 4:
                sum += roll
        return sum
    

    @staticmethod
    def fives(roll_list):
        sum = 0
        for roll in roll_list:
            if roll == 5:
                sum += roll
        return sum
    

    @staticmethod
    def sixes(roll_list):
        sum = 0
        for roll in roll_list:
            if roll == 6:
                sum += roll
        return sum


    def count_rolls(roll_list, counts):
        for roll in roll_list:
            counts[roll-1] += 1


    @staticmethod
    def score_pair(roll_list):
        counts = [0] * 6
        
        Yatzy.count_rolls(roll_list, counts)

        score = 0
        for i in range(len(counts)):
            if counts[len(counts) - i - 1] >= 2:
                score += (len(counts) - i) * 2
                return score

        return score


    @staticmethod
    def two_pair(roll_list):
        counts = [0] * 6
        
        Yatzy.count_rolls(roll_list, counts)

        cycles = 0
        score = 0
        for i in range(len(counts)):
            if counts[len(counts) - i - 1] >= 2:
                score += (len(counts) - i) * 2
                cycles += 1

        if cycles == 2:
            return score

        return 0
    

    @staticmethod
    def three_of_a_kind(roll_list):
        counts = [0] * 6
        
        Yatzy.count_rolls(roll_list, counts)

        for i in range(len(counts)):
            if counts[i] >= 3:
                return (i + 1) * 3

        return 0
    

    @staticmethod
    def four_of_a_kind(roll_list):
        counts = [0] * 6
        
        Yatzy.count_rolls(roll_list, counts)

        for i in range(len(counts)):
            if counts[i] >= 4:
                return (i + 1) * 4

        return 0


    @staticmethod
    def smallStraight(roll_list):
        counts = [0]*6
        
        Yatzy.count_rolls(roll_list, counts)
            
        if (counts[0] == counts[1] == counts[2] == counts[3] == counts[4] == 1):
            return 15

        return 0
    

    @staticmethod
    def largeStraight(roll_list):
        counts = [0]*6
        
        Yatzy.count_rolls(roll_list, counts)

        if (counts[1] == counts[2] == counts[3] == counts[4] == counts[5] == 1):
            return 20
            
        return 0
    

    @staticmethod
    def fullHouse(roll_list):
        counts = [0]*6

        Yatzy.count_rolls(roll_list, counts)

        has_pair = False
        num_of_pair = 0
        has_trio = False
        num_of_trio = 0
        for i in range(len(counts)):
            if (counts[i] == 2): 
                has_pair = True
                num_of_pair = i+1
            if (counts[i] == 3): 
                has_trio = True
                num_of_trio = i+1

        if (has_pair and has_trio):
            return (num_of_pair * 2) + (num_of_trio * 3)
        else:
            return 0