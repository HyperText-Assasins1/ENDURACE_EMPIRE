from App.database import db
from .exercise import Exercise

class ExerciseSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercises = db.relationship('Exercise', backref='exercise_set', lazy="dynamic")
    # exercise = db.relationship('Exercise')

    def __init__(self, user_id, exercise, name):
        self.user_id = user_id
        self.exercises.append(exercise)
        self.name = name

    def __repr__(self):
        return f'<ExerciseSet {self.id} : {self.name} user {self.user.username}>'

    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'exercises': [exercise.get_json() for exercise in self.exercises],
            'user_id': self.user_id,
        }


