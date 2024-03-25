# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        pattern = re.compile(r"\,\s|\s|\,")
        new_list = pattern.split(self.email_string)
        validated_list = []
        for email in new_list:
            pattern = re.compile(r"^\S+@\S+\.\S+$")
            if pattern.fullmatch(email) is not None:
                validated_list.append(email)
        return sorted(validated_list)