# Sports Tournament Scoreboard

scores = [
    ("Team A", 3),
    ("Team B", 5),
    ("Team C", 2)
]

def update_score(team_name, points):
    for i, (team, score) in enumerate(scores):
        if team.lower() == team_name.lower():
            scores[i] = (team, score + points)
            print(f"Updated {team}'s score to {score + points}")
            return
    print("Team not found.")

def show_scores():
    print("\nScoreboard:")
    for team, score in scores:
        print(f"{team}: {score} points")

show_scores()
update_score("Team C", 4)
show_scores()
