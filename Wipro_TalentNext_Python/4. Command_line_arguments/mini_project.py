import sys

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} <like_numbers> <dislike_numbers> <given_numbers>")
else:
    like = set(sys.argv[1].split('-'))
    dislike = set(sys.argv[2].split('-'))
    given = sys.argv[3].split('-')

    happiness = 0

    for num in given:
        if num in like:
            happiness += 1
        elif num in dislike:
            happiness -= 1

    print(happiness)
