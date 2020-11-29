#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
import models
from models.user import User
from models.post import Post
from models.comment import Comments
from models.interview import Interview
from models.answer import Answer
from models.correction import Correction
from models.category import Category
from models.subcategory import Subcategory
from models.sub_follow import Sub_follow
from models.relation import Relation
from models.comm_like import Comm_like
from models.post_like import Post_like
from models.question import Question

# Creation of a user
"""user = User(name="Ines", last_name="Chokri",
        username="cutiepizza", passwd="123456", birth="26-04-1997",
        email="ines.chokri@joli.com", type="1", pic="../images/ines.jpg", status="student", gender="female")
user.save()

user2 = User(name="Salmen", last_name="Zouari", username="salmenz",
        passwd="123456", birth="unknown", email="salmenz@gmail.com",
        type="1", pic="../images/salmen.jpeg", status="Student", gender="Male")
user2.save()"""

# Creation of a category
cat = Category(name="AI")
cat.save()

# Creation of a subcategory
sub = Subcategory(name="Machine learning", sub_id=cat.id)
sub.save()

# Creation of an Interview
interview = Interview(status="Done", submit_date="2020-06-15", type="hakuna batata", user_id=user.id, cat_id=cat.id)
interview.save()

# Creation of a Post

post = Post(content="How do I answer correctly \"tell me about yourself\"?",
        sub_id=sub.id, u_id=user2.id, cat_id=cat.id)
post.save()

# Creation of a Comment
comment = Comments(content="Just tell the story of your life !", user_id=user.id, post_id=post.id)
comment.save()

# Creation of a question 
question = Question(text="Tell me about yourself", type="RH", sub_id=sub.id, int_id=interview.id)
question.save()

# Creation of an Answer

ans = Answer(text="Bla bla bla", audio=None, int_id=interview.id)
ans.save()

models.storage.save()
