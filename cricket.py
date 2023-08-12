import random

class Player:
    def __init__(self, name, batting_avg, runs):
        self.name = name
        self.batting_avg = batting_avg
        self.runs = runs

class BallOutcome:
    def __init__(self, runs, is_wicket, likelihood, description):
        self.runs = runs
        self.is_wicket = is_wicket
        self.likelihood = likelihood
        self.description = description

###

ball_outcomes = []
ball_outcomes.append(BallOutcome(0, False, 30, "defends for no runs"))
ball_outcomes.append(BallOutcome(1, False, 10, "gets a 1"))
ball_outcomes.append(BallOutcome(2, False, 5, "runs for 2"))
ball_outcomes.append(BallOutcome(3, False, 1, "runs through for 3"))
ball_outcomes.append(BallOutcome(4, False, 5, "hits it for 4️⃣  !"))
ball_outcomes.append(BallOutcome(6, False, 1, "hits it for 6️⃣  !!!"))
ball_outcomes.append(BallOutcome(0, True, 2, "is out!"))

def createPlayer(team, name, batting_avg):
    team.append(Player(name, batting_avg, 0))

england = []
createPlayer(england, 'Zak Crawley', 45)
createPlayer(england, 'Ben Duckett', 37)
createPlayer(england, 'Moeen Ali', 31)
createPlayer(england, 'Joe Root', 55)
createPlayer(england, 'Harry Brook', 50)
createPlayer(england, 'Ben Stokes', 34)
createPlayer(england, 'Johnny Bairstow', 42)
createPlayer(england, 'Chris Woakes', 18)
createPlayer(england, 'Mark Wood', 13)
createPlayer(england, 'Stuart Broad', 11)
createPlayer(england, 'James Anderson', 5)

aus = []
createPlayer(aus, 'Pat Cummins', 11)
createPlayer(aus, 'Mitchell Starc', 5)

###

def ball_outcome():
    # Extract likelihood values from the ball_outcomes list
    likelihood_values = [outcome.likelihood for outcome in ball_outcomes]

    # Select a random outcome based on likelihood values
    outcome = random.choices(ball_outcomes, weights=likelihood_values)[0]

    return outcome

def ball(ball_in_over, batter, bowler):
    print("ball " + str(ball_in_over) + "/6:")
    print(bowler.name + " runs in to bowl...")

    outcome = ball_outcome()
    print(batter.name + " " + outcome.description + "\n")

    return outcome

def rotate_strike(batters):
    # Remove the last item from the list
    last_item = batters.pop()

    # Insert the last item at the beginning of the list
    batters.insert(0, last_item)

    return batters

def over(runs, wickets, batters, bowler, still_to_bat):
    ball_in_over = 1
    runs_in_over = 0
    wickets_in_over = 0

    print('---\n')

    print("✨ Next over!")
    print(bowler.name + " is bowling for Austrailia\n")
    input('press enter to continue...\n')

    for i in range(6):
        on_strike = batters[0]
        outcome = ball(i+1, on_strike, bowler)

        ball_in_over = ball_in_over +1
        runs_in_over = runs_in_over + outcome.runs

        if outcome.is_wicket: 
            wickets_in_over = wickets_in_over + 1

            if len(still_to_bat) == 0:
                return runs_in_over, wickets_in_over, batters, still_to_bat, True

            next_up = still_to_bat[0]
            batters = [next_up, batters[1]]
            still_to_bat = still_to_bat[1:]
            print('next up, ', next_up.name + "...\n")

        on_strike.runs = on_strike.runs + outcome.runs

        if outcome.runs % 2 == 1:
            batters = rotate_strike(batters)



    return runs_in_over, wickets_in_over, batters, still_to_bat, False

def over_summary(players, over_num, runs, wickets, over_limit, runs_in_over, wickets_in_over, batters):
    run_rate = format(runs / over_num, ".2f")

    print('\n')
    print("---")
    print(str(runs_in_over) + " runs from the over")
    print(str(wickets_in_over) + " wickets")
    print("---\n")

    print('📝 england scorecard:')
    for i, p in enumerate(players):
        player_line = str(i+1) + ". " + p.name + " – " + str(p.runs)
        if p in batters:
            player_line = player_line + " ⭐️"
        print(player_line)


    print('\n')
    print("🧮 the score is " + str(runs) + "/" + str(wickets))
    print("run rate: " + str(run_rate))
    print("overs played: " + str(over_num) + "/" + str(over_limit))


def batting(players):
    over_limit = 50
    runs = 0
    wickets = 0
    over_num = 1
    batters = [players[0], players[1]] # the first batter in the list is on strike
    still_to_bat = [item for item in players if item not in batters]
    bowler = aus[0]


    print("🪖  batters:")
    for i, p in enumerate(players):
        print(str(i+1) + ". " + p.name + " | avg: " + str(p.batting_avg))
    print('\n')

    print("👬 " + batters[0].name + " and " + batters[1].name + " are opening the batting\n")

    for o in range(over_limit):
        runs_from_over, wickets_from_over, batters, still_to_bat, is_all_out = over(runs, wickets, batters, bowler, still_to_bat)
        runs = runs + runs_from_over
        wickets = wickets + wickets_from_over


        over_summary(players, over_num, runs, wickets, over_limit, runs_from_over, wickets_from_over, batters)

        if is_all_out:
            print("all out! 💀")
            print("\n")
            return 

        batters = rotate_strike(batters)
        over_num = over_num + 1
        print("\n")

        if bowler == aus[0]:
            bowler = aus[1]
        else:
            bowler = aus[0]

    print("innings complete! ✅")
    print("\n")

###

print('🏏 welcome to cricket 🏏')
input('press enter to continue...\n')

print('🏁 england to batt first')
input('press enter to continue...\n')
print('---\n')
batting(england)

#
# Starting coding the toss, then realised cba
#
# print("it's the toss! 🍀")
# is_heads = input("heads or tails?\n1. heads\n2. tails\n") == "1"

# print('\n')

# print("You've won the toss! 🎉")
# is_batting = input("batt or bowl?\n1. batt\n2. bowl\n") == "1"

# print('\n')

# if is_batting:
    # print("🏏 lets batt\n")
    # batting(england)
# else:
    # print("lets bowl")
    # print("no bowly yet")





