"""
Count poker hands

Sample program to count poker hands and thus estimate the probability of a given hand occurring .
The file contains 1 million records randomly distributed and is, therefore, statistically valid.

The data looks like this:

1,1,1,13,2,4,2,3,1,12,0
3,12,3,2,3,11,4,5,2,5,1
1,9,4,6,1,4,3,2,3,9,1
1,4,3,13,2,13,2,1,3,6,1

A hand in poker consists of five cards. Each pair of numbers represents a card giving its suit and value.
Suits are 1-spades, 2-hearts, 3-diamonds, 4-clubs
Values go from Ace (13) highest to 2 (shown as 1) lowest.
Ranks are 0-nothing, 1-pair, 2-two pair, 3-three of a kind, 4-flush, 5-straight, 6-full house, 7-four of a kind,
8-straight flush, 9-royal flush

In our example above the first line represents the hand, 2 of spades, ace of spades, 5 of hearts, 4 of hearts,
king of clubs, The last column is the rank
"""


def main():
    # 1. Open file for reading

    try:
        with open("poker-hand-testing.data", 'r') as fh:
            poker_file = fh.read()
            poker_file = poker_file.split("\n")
    except IOError as e:
        print(e)
        quit()

    # 2. Create and initialize variables to hold the counts

    total_count = 0
    rank_counts = {}
    rank_list = ['nothing', 'pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind',
                 'straight flush', 'royal flush']

    # 3. Loop through each line of the file

    for line in poker_file:
        # Get hand rank: split on comma, get last item as int
        try:
            hand_rank = int(line.split(',')[-1])

            # At each valid line increment the counter
            total_count += 1
        except ValueError as e:
            print(e)
            continue

        # If rank already in dictionary, increment it otherwise add it and set to 1
        if hand_rank in rank_counts:
            rank_counts[hand_rank] += 1
        else:
            rank_counts[hand_rank] = 1

    # 4. Print the results

    print(f"Total hands in file: {total_count:,d}")
    print("Count and probability of hands:")

    for i in range(10):
        print(f"  {rank_list[i]:18s}:{rank_counts[i]:10,d}{rank_counts[i] / total_count:10.4%}")


if __name__ == "__main__":
    main()
