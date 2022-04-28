"""Blackjack, (c) Denis Balako denisarius2000s@gmail.com
Classic card game, with alternative name "21"
Tags: big, game, card game"""

import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Denis Balako denisarius2000s@gmail.com

    Rules:
        Try to get close to 21 without going over.
        Kings, Queens and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 trough 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your betavariate
        but must hit exactly one more time before standing.
        In case of a tie, the bet returned to the player.
        The dealer stops hitting at 17.\n''')

    money = 5000
    while True:  # main game cycle
        # Check player's money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # Give player an opportunity to make a bet
        print('Money:', money)
        bet = getBet(money)

        # Give dealer and player 2 cards from deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Processing player actions
        print('Bet:', bet)
        while True:
            # perform cycle until player don't say "enough" or he have a blast
            displayHands(playerHand, dealerHand, False)
            print()

            # Check for player blast
            if getHandValue(playerHand) > 21:
                break

            # Get player move: H, S or D:
            move = getMove(playerHand, money - bet)

            if move == 'D':
                # player doubles, he can raise a bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('\nBet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # 'More' or 'double': player take one more card
                newCard = deck.pop()
                rank, suit = newCard
                print('\nYou drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # player blast
                    continue

            if move in ('S', 'D'):
                break

        # Processing dealer actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # dealer takes another card
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # blast
                input('Please Enter to continue...')
                print('\n\n')

        # Displays final cards on hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Check the player win, lose or time
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


def getBet(maxBet):
    """Asks player how much he bets on this round"""
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Return list of tuples (rank, suit) for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Display player's and dealer's hand."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """Return cards cost"""
    value = 0
    numberOfAces = 0

    # Adds card cost - not ace
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card  # card type - tuple
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Asks which move player want to choose,
    return 'H', if he want to take a card
    'S', if that's enough
    and 'D', if he doubled"""
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Gets the player move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


if __name__ == '__main__':
    main()
