from flask_login import UserMixin

from . import db


class Todo(UserMixin, db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('todo_categories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    status = db.Column(db.String(2), nullable=False, default='0')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    category = db.relationship('TodoCategory', backref=db.backref('todos', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'category': {
                'id': self.category.id,
                'name': self.category.name,
                'description': self.category.description
            },
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __repr__(self):
        return f'<Todos {self.name}>'
