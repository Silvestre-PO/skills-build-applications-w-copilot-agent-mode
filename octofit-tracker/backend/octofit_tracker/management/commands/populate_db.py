from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', username='thundergod', first_name='Thor', last_name='Odinson'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', username='metalgeek', first_name='Tony', last_name='Stark'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', username='zerocool', first_name='Elliot', last_name='Alderson'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', username='crashoverride', first_name='Dade', last_name='Murphy'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', username='sleeptoken', first_name='Sleep', last_name='Token'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling', description='Cycling training', points=50),
            Workout(_id=ObjectId(), name='Crossfit', description='Crossfit training', points=70),
            Workout(_id=ObjectId(), name='Running', description='Running training', points=40),
            Workout(_id=ObjectId(), name='Strength', description='Strength training', points=60),
            Workout(_id=ObjectId(), name='Swimming', description='Swimming training', points=80),
        ]
        Workout.objects.bulk_create(workouts)

        # Create activities
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

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))