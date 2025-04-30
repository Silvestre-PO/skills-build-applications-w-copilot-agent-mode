from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Create users with unique _id
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', username='thundergod', first_name='Thor', last_name='Odinson'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', username='metalgeek', first_name='Tony', last_name='Stark'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', username='zerocool', first_name='Elliot', last_name='Alderson'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', username='crashoverride', first_name='Dade', last_name='Murphy'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', username='sleeptoken', first_name='Sleep', last_name='Token'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()

        # Create workouts with unique _id
        workouts = [
            Workout(_id=ObjectId(), name='Cycling', description='Cycling training', points=50),
            Workout(_id=ObjectId(), name='Crossfit', description='Crossfit training', points=70),
            Workout(_id=ObjectId(), name='Running', description='Running training', points=40),
            Workout(_id=ObjectId(), name='Strength', description='Strength training', points=60),
            Workout(_id=ObjectId(), name='Swimming', description='Swimming training', points=80),
        ]
        Workout.objects.bulk_create(workouts)

        # Create activities with unique _id
        activities = [
            Activity(_id=ObjectId(), user=users[0], workout=workouts[0], duration=60, team=team1),
            Activity(_id=ObjectId(), user=users[1], workout=workouts[1], duration=90, team=team1),
            Activity(_id=ObjectId(), user=users[2], workout=workouts[2], duration=120, team=team2),
            Activity(_id=ObjectId(), user=users[3], workout=workouts[3], duration=30, team=team2),
            Activity(_id=ObjectId(), user=users[4], workout=workouts[4], duration=75, team=team2),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboards = [
            Leaderboard(_id=ObjectId(), team=team1, total_points=120),
            Leaderboard(_id=ObjectId(), team=team2, total_points=215),
        ]
        Leaderboard.objects.bulk_create(leaderboards)

        # Save users individually to ensure primary keys are assigned
        for user in users:
            user.save()

        # Save teams individually to ensure primary keys are assigned
        team1.save()
        team2.save()

        # Associate users with teams after saving
        team1.members.add(users[0])
        team1.members.add(users[1])
        team2.members.add(users[2])
        team2.members.add(users[3])
        team2.members.add(users[4])

        # Save workouts individually to ensure primary keys are assigned
        for workout in workouts:
            workout.save()

        # Save activities individually to ensure primary keys are assigned
        for activity in activities:
            activity.save()

        # Save leaderboards individually to ensure primary keys are assigned
        for leaderboard in leaderboards:
            leaderboard.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
