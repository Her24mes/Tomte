## Intent class
# purpose: Enum
# content: String[]
###########
from enum import Enum # for enum34
class Intent:
    """the Intent class used to capture a requests intent"""
    purpose = Enum('purpose', 'AddUser, AddFlat, AddTask, RemoveUser, RemoveFlat, RemoveTask')
    content = []