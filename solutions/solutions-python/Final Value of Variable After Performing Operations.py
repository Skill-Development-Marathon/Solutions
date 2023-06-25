def finalValueAfterOperations(operations):
        final = 0
        for i in operations:
            if i == "--X" or i == "X--":
                final -= 1
            elif i == "X++" or i == "++X":
                final += 1
        return final