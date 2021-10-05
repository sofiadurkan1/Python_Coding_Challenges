
# You are keeping score for a baseball game with strange rules. The game consist of several rounds, where the
# scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where
# ops[i] is the ith operation you must apply to the record and is one of the following:
# An integer x - Record a new score of x,
# "+" - Record a new score that is the sum of the previous scores. It is guaranteed there will always be
# two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a
# previous score.
# "C" - Invalidate the pevious score, removing it from the record. It is guaranteed there will always be a
# previous score.
# Return the sum of all the scores on the record

# example
# Input: ops = ["5", "2", "C", "D", "+"]
# Output: 30


record = []
ops = ["5", "2", "C", "D", "+"]
def score_sum (ops):
    for i in ops:
        if "C" == i and len(record)>0:
            record.pop()

        elif "D" == i and len(record)>0:
            record.append(record[-1]*2)
        
        elif "+" == i and len(record)>1:
            record.append(record[-1] + record[-2])

        elif (isinstance(i, int)):
            record.append(i)
    return(sum(record))     


# print(score_sum([4,2,"+"]))
# print(score_sum([]))
print(score_sum("null"))
# print(score_sum([4,"+"]))
# print(score_sum([4,"C"]))
# print(score_sum([4,2,"D"]))
# print(score_sum([4]))
# print(score_sum([4,"D"]))
# print(score_sum(["A","D"]))





