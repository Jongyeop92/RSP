# -*- coding: utf8 -*-

import random


ROCK     = 1
SCISSORS = 2
PAPER    = 3

WIN  = "win"
LOSE = "lose"
DRAW = "draw"


def getResultList(handList):

    countList = [0, 0, 0]

    for hand in handList:
        if   hand == ROCK:     countList[0] += 1
        elif hand == SCISSORS: countList[1] += 1
        elif hand == PAPER:    countList[2] += 1

    handCount = len(handList)

    if handCount in countList \
       or all(c > 0 for c in countList):
        return [DRAW] * handCount

    if   countList[0] > 0 and countList[1] > 0:
        winHand  = ROCK
        loseHand = SCISSORS
    elif countList[1] > 0 and countList[2] > 0:
        winHand  = SCISSORS
        loseHand = PAPER
    else:
        winHand  = PAPER
        loseHand = ROCK

    resultList = []

    for hand in handList:
        if hand == winHand: result = WIN
        else:               result = LOSE

        resultList.append(result)

    return resultList


def test():

    assert getResultList([ROCK, ROCK])           == [DRAW, DRAW]
    assert getResultList([SCISSORS, SCISSORS])   == [DRAW, DRAW]
    assert getResultList([PAPER, PAPER])         == [DRAW, DRAW]
    assert getResultList([ROCK, SCISSORS,PAPER]) == [DRAW, DRAW, DRAW]

    assert getResultList([ROCK, SCISSORS])  == [WIN, LOSE]
    assert getResultList([SCISSORS, PAPER]) == [WIN, LOSE]
    assert getResultList([PAPER, ROCK])     == [WIN, LOSE]

    assert getResultList([ROCK, ROCK, PAPER])      == [LOSE, LOSE, WIN]
    assert getResultList([SCISSORS, PAPER, PAPER]) == [WIN, LOSE, LOSE]

    print "success"


def main():

    handStrList = ["", u"바위", u"가위", u"보"]

    beforeResult = None
    continueCount = 0

    while True:
        print "가위바위보 게임(바위: 1, 가위: 2, 보: 3). 종료는 -1 입력"

        hand = raw_input("입력: ")

        if hand not in ["-1", str(ROCK), str(SCISSORS), str(PAPER)]:
            print "잘못된 입력입니다."
            print
            continue

        if hand == "-1":
            break

        hand = int(hand)
        computerHand = random.randint(1, 3)

        resultList = getResultList([hand, computerHand])

        print "당신:", handStrList[hand], "컴퓨터:", handStrList[computerHand]
        
        if resultList[0] == WIN:
            print "승리!"
        elif resultList[0] == LOSE:
            print "패배!"
        else:
            print "무승부"

        if beforeResult == resultList[0]:
            continueCount += 1
        else:
            beforeResult = resultList[0]
            continueCount = 1

        if continueCount > 1:
            if beforeResult == WIN:
                resultStr = "승"
            elif beforeResult == LOSE:
                resultStr = "패"
            else:
                resultStr = "무"

            print "%d연%s" % (continueCount, resultStr)

        print


if __name__ == "__main__":
    #test()
    main()
