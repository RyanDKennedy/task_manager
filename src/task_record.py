"""
Ryan Kennedy, Gabriel Walder
Cmdr. Schenk
Cloud Computing
7th Period
May 5, 2025
"""

class TaskRecord:

    def __init__(self):
        self.id = -1
        self.user_id = -1
        self.short_name = "blank"
        self.description = "blank"

    def fill(self, id, user_id, short_name, description):
        self.id = id
        self.user_id = user_id
        self.short_name = short_name
        self.description = description

    def to_string(self):
        result = "id: {}".format(self.id)
        result += "\nuser_id: {}".format(self.user_id)
        result += "\nshort_name: {}".format(self.short_name)
        result += "\ndescription: {}".format(self.description)
        return result





