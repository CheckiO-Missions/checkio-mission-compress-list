"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]],
            "answer": [5, 4, 5, 6, 5, 7, 8, 0],
        },
        {
            "input": [[1, 1, 1, 1, 2, 2, 2, 1, 1, 1]],
            "answer": [1, 2, 1],
        },
        {
            "input": [[7, 7]],
            "answer": [7],
        },
        {
            "input": [[]],
            "answer": [],
        },
        {
            "input": [[1, 2, 3, 4]],
            "answer": [1, 2, 3, 4],
        },
        {
            "input": [[9, 9, 9, 9, 9, 9, 9]],
            "answer": [9],
        },
        {
            "input": [[9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9]],
            "answer": [9, 0, 9],
        }
    ],
    "Extra": [
        {
            "input": [[1, 1, 1, 1, 1, 1]],
            "answer": [1],
        },
        {
            "input": [[2, 1, 5, 5, 5, 5, 5, 5]],
            "answer": [2, 1, 5],
        },
        {
            "input": [[1, 2, 3, 4, 4, 4, 4, 4, 3, 2, 1]],
            "answer": [1, 2, 3, 4, 3, 2, 1],
        },
        {
            "input": [[3]],
            "answer": [3],
        },
        {
            "input": [[10, 10, 10]],
            "answer": [10],
        },
        {
            "input": [[4, 4, 4, 4, 4, 5, 6, 5, 5, 5, 5, 5, 5]],
            "answer": [4, 5, 6, 5],
        },
        {
            "input": [[1, 2, 3, 4, 5, 5, 5, 6, 6, 6]],
            "answer": [1, 2, 3, 4, 5, 6],
        },
    ]
}
