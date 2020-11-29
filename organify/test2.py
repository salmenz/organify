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

# Creation of a Comment
comment = Comments(content="Just as Yasmine said.", user_id="0542762f-28f0-45b9-bae6-1bb37a09b8ca", post_id="a8dab4a6-180a-4359-8ce0-f34f37a0ddfd")
comment.save()

models.storage.save()
