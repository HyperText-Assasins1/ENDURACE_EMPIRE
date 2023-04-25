from App.models import Exercise
from App.database import db

def get_data():
    # add all the exercises here
    url = 'https://wger.de/api/v2/exercise/?format=json&limit=800'

    # https://wger.de/api/v2/exercise/?format=json&limit=200 sets the amount of exercises
    # to a limit of 200, the limit can be altered or removed
    
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        
        data = response.json()
        # this loops through th size of the data['results'] and if the language == 2 (english)
        # then print the exercise name
        for i in range (len(data['results'])):
            
            if(data['results'][i]['id']) == 91:
                    print(data['results'][i]['description'])


            if(data['results'][i]['language'] == 2):
                create_exercise(data['results'][i]['name'], data['results'][i]['description'], data['results'][i]['category'])

        


    user = get_user_by_username('bob')
    user = user.get_json()

    exerciseSetName = "oogabooga"

    testExerciseID = get_exercise_by_id(1)
    testExerciseID = testExerciseID.get_json()

    add_exerciseSet(exerciseSetName ,user['id'], testExerciseID['id'])
    
def create_exercise(name, description, category):
    newExercise = Exercise(name=name, description=description, category=category)
    db.session.add(newExercise)
    db.session.commit()
    return newExercise

def update_exercise(id, name):
    cise = get_exercise_by_id(id)
    if cise:
        cise.name = name
        db.session.add(cise)
        db.session.commit()
        return True
    return False

def get_exercise_by_name(name):
    return Exercise.query.filter_by(name=name).first()

def get_exercise_by_id(id):
    return Exercise.query.get(id)

def get_exercise_by_exerciseid(exercise_id):
    return Exercise.query.filter_by(exercise_id=exercise_id).first()

def get_all_exercises():
    return Exercise.query.all()

def get_all_exercises_json():
    exercises = Exercise.query.all()
    if not exercises:
        return[]
    exercises = [exercise.get_json() for exercise in exercises]
    return exercises


