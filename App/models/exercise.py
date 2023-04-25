from App.database import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    set_id = db.Column(db.Integer, db.ForeignKey('exercise_set.id'))
    description = db.Column(db.String, nullable=True)
    category = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    # get_json function
    def get_json(self):
        return{
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "category":self.category
        }