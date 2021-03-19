import argparse
import random

warmups = [
    "Roll out joints",
    "Ankle raises",
    "Leg swings",
    "90 degree lifts",
    "Wrist warm-up",
    "Reverse balance",
    "Full squat twists",
]

workouts = [
    "Bear twists",
    "Plank knee to elbow",
    "Sumo squats",
    "Push-ups",
    "Hollow hold",
    "Bowlers",
    "Reverse plank lifts",
    "Star abs",
    "Single leg bridge",
    "Side lunges",
    "Ab marches",
    "Toe touches",
    "Tacos",
    "Get-ups",
    "Russian twists",
    "Pistol squats",
    "Kossak squats",
]

parser = argparse.ArgumentParser(description="Create randomized workouts.")
parser.add_argument(
    "-n",
    action="store",
    required=False,
    default="7",
    help="The number of exercises and warmups to generate",
)
args = parser.parse_args()

random_warmups = random.choices(warmups, k=int(args.n))
random_workouts = random.choices(workouts, k=int(args.n))

print("Warmups for today:")
for warmup in random_warmups:
    print("- {}".format(warmup))

print("Workouts for today:")
for workout in random_workouts:
    print("- {}".format(workout))
