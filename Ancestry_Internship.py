# Isaac Robbins
# Coding Assessment for Ancestry Internship


# Problem 1
# Find the 3rd highest paid player.
"""
SELECT P.FirstName, P.LastName
FROM Players AS P, Salaries AS S
WHERE P.PlayerID = S.PlayerID
ORDER BY S.Amount DESC
LIMIT 2, 1;
"""

# Problem 2
# Find the 3rd lowest paid player.
"""
SELECT P.FirstName, P.LastName
FROM Players AS P, Salaries AS S
WHERE P.PlayerID = S.PlayerID
ORDER BY S.Amount
"""

# Problem 3
# Which position scored the most goals?
"""
SELECT Pos.PositionName
FROM Positions AS Pos, Players AS P, ScoredGoals AS SG
WHERE P.PlayerID = SG.PlayerID AND Pos.PositionID = P.PositionID
GROUP BY P.PositionID
ORDER BY COUNT(SG.GoalID) DESC
LIMIT 1;
"""

# Problem 4
# Which payers never scored?
"""
SELECT P.FirstName, P.LastName
FROM Players AS P, ScoredGoals AS SG
WHERE P.PlayerID NOT IN (
    SELECT SG.PlayerID FROM ScoredGoals AS SG);
"""

# Problem 5
# Which player scored the most goals?
"""
SELECT TOP 1 P.FirstName, P.LastName
FROM Players AS P, ScoredGoals AS SG
WHERE P.PlayerID = SG.PlayerID
GROUP BY P.PlayerID
ORDER BY COUNT(SG.GoalID) DESC;
"""

# Problem 6
# Which player scored the most goals in a single game?
"""
SELECT TOP 1 P.FirstName, P.LastName
FROM Players AS P, ScoredGoals AS SG
WHERE P.PlayerID = SG.PlayerID
GROUP BY P.PlayerID, SG.GameID
ORDER BY COUNT(SG.GoalID) DESC;
"""

# Problem 7
# What is the salary paid per goal per position?
"""
This is a poor question. It is unclear what is actually being asked and as I
understand the question, it is based off of the assumption that players of all
positions are paid by how many goals they score. There may be a strong
correlation between goals scored and salary for offensive players, but for other
positions such as defensive players and goalies, it is unlikely that their
salaries are related to the number of goals they score. Thus not only is this
question irrelevant, but in this calculation, if none of the players of one of
the positions has scored a goal, then the query would have to divide by zero.
Regardless here is a query for the total salary divided by the number of goals
for each position.

SELECT Pos.PositionName, SUM(S.Amount)/COUNT(SG.GoalID)
FROM Position AS Pos, Players AS P, Salaries AS S, ScoredGoals AS SG
WHERE Pos.PositionID = P.PositionID, S.PlayerID = P.PlayerID, SG.PlayerID = P.PlayerID
GROUP BY Pos.PositionID;
"""

# Problem 8
# What is the average minute of scored goals for each game?
"""
Again this question is unclear as to what is being asked. Is the query supposed
to return a single number that is the average minute that goals are scored or a
list of each individual game with its average minute that goals are scored. The
wording of the question leans towards the latter but the first appears to be a
more useful query. It is also important to note that the first is not the
average of the individual averages for each game.
Here is the average minute of goals scored.

SELECT AVG(Minute)
FROM ScoredGoals;

Here is the average minute of goals scored for each game individually.

SELECT AVG(Minute)
FROM ScoredGoals
GROUP BY GameID;
"""

# Problem 9
# What should the Salaries table look like if we needed to track historical
# data?
"""
The Salaries table would need to include columns that contained elements of time
such as StartDate and EndDate because it is very common for player's salaries to
change with time.
"""


# Problem 10
def repeated_string():
    """Prompts the user for an input string and returns the first letter in the
    string that is not repeated as well as the string reordered by number of
    occurrences by character in ascending order.

    Returns
        (str): The first letter in the string that is not repeated
        (str): The reordered string
    """

    # Prompts the user for an input string
    inp_str = str(input("Enter a string: "))
    # Gets length of the string
    n = len(inp_str)
    # Initializes a list of empty strings for each letter
    letters = ['']*26
    # Initializes a list to keep track of the order of letters by appearance
    order = []
    # Sorts the letters
    for j in inp_str:
        if ord(j) >= 97:
            ordinal = ord(j) - 97
        else:
            ordinal = ord(j) - 65
        letters[ordinal] = letters[ordinal] + j
        # Keeps track of the order of appearance of letters
        if ordinal not in order:
            order.append(ordinal)
    # Initializes the two strings to be returned
    ordered_str = ''
    first_non_repeated = ''
    # Iterates through the number of occurrences
    for num_occur in range(1, n + 1):
        # Iterates through the letters by their order of appearance
        for i, j in enumerate(order):
            # Checks for the first letter that is not repeated
            if len(letters[j]) == 1 and first_non_repeated == '':
                first_non_repeated = letters[j][0]
                print(first_non_repeated)
                ordered_str = letters[j][0]
                continue
            # Adds the next shortest group of letters to the string
            elif len(letters[j]) == num_occur:
                ordered_str = ordered_str + letters[j]
    print(ordered_str)
    return first_non_repeated, ordered_str

repeated_string()
