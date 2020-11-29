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
"""
user = User(name="Yasmine", last_name="Hamdi",
        passwd="123456", birth="26-04-1997",
        email="yasmineholb@gmail.com", type="1", pic="../images/yasmine.jpeg", status="student", gender="Female")
user.save()
"""

# Creation of a Post

"""post = Post(content="How do I answer \"Tell me about yourself\"",
       sub_id="c7cd41c9-0cdf-4b63-9f34-1eda3c05e434", u_id="a5f3f5b6-80f5-4a9b-bc83-6a4d13bf4502", cat_id="b1f5cf3a-94c4-4ce8-8d92-d5adcdc53f51")
post.save()
"""
# Creation of a Comment
comment = Comments(content="Speak about yourself as if it was a story to be told", user_id="88609d5d-0f45-4b90-a476-eabce6b66281", post_id="39f5ec2e-8584-4217-8e4f-6ae8fb1c45ca")
comment.save()

models.storage.save()
