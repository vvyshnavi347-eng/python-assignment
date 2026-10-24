
# Multi-Event Sports Scheduling and Scoring

# Event schedule using tuples inside a list
schedule = [
    ("Cricket", "Team A", "Team B", 9, 11),
    ("Football", "Team C", "Team D", 10, 12),
    ("Volleyball", "Team A", "Team C", 13, 14),
    ("Basketball", "Team B", "Team D", 9, 10),
    ("Badminton", "Team A", "Team D", 15, 16)
]

# Store scores as (team, points scored)
scores = [
    ("Cricket", "Team A", 3, "Team B", 1),
    ("Football", "Team C", 2, "Team D", 0),
    ("Volleyball", "Team A", 1, "Team C", 3),
    ("Basketball", "Team B", 2, "Team D", 2),
    ("Badminton", "Team A", 3, "Team D", 0)
]

print("===== SPORTS EVENT SCHEDULE =====")

for event in schedule:
    print(event[0], "-", event[1], "vs", event[2],
          "| Time:", str(event[3]) + ":00 to",
          str(event[4]) + ":00")

# Identify scheduling conflicts
print("\n===== SCHEDULING CONFLICTS =====")

conflict_found = False

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        event1 = schedule[i]
        event2 = schedule[j]

        # Check whether time periods overlap
        overlap = (event1[3] < event2[4] and
                   event2[3] < event1[4])

        # Check whether any team plays both events
        common_teams = set(event1[1:3]) & set(event2[1:3])

        if overlap and common_teams:
            print(event1[0], "and", event2[0],
                  "conflict for", ", ".join(common_teams))
            conflict_found = True

if not conflict_found:
    print("No scheduling conflicts found.")

# Calculate points for each team
team_points = {}
team_wins = {}

for result in scores:
    event, team1, score1, team2, score2 = result

    for team in (team1, team2):
        team_points.setdefault(team, 0)
        team_wins.setdefault(team, 0)

    if score1 > score2:
        team_points[team1] += 3
        team_wins[team1] += 1
    elif score2 > score1:
        team_points[team2] += 3
        team_wins[team2] += 1
    else:
        team_points[team1] += 1
        team_points[team2] += 1

# Generate final rankings
rankings = sorted(
    team_points.items(),
    key=lambda item: (-item[1], -team_wins[item[0]], item[0])
)

print("\n===== FINAL TEAM RANKINGS =====")
print("Rank | Team   | Points | Wins")

for rank, (team, points) in enumerate(rankings, start=1):
    print(rank, "|", team, "|", points, "|", team_wins[team])
