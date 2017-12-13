from daak1.daak.daak.decorators import jsonPost

# @jsonPost()
# def test():
#     return 'hello iran'


@jsonPost()
class a:
    @jsonPost()
    def b(self):
        return 'hello class'


# import os
# import re
#
# x = 11
# imports = "os","re"
#
# for vars in dir():
#     # if vars.startswith("__") == 0 and vars not in imports:
#         print vars