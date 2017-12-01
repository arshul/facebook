# -*- coding: utf-8 -*-
from datetime import datetime
from flask_script import Command
from tdg_fb_group.constants.groups import KEYWORDS
from tdg_fb_group.api.groups import group_add
from tdg_fb_group.utils.groups import search

class AddGroup(Command):
    def run(self):
        print("Adding Groups")
        for keyword in KEYWORDS:
            print(keyword)
            groups = search(keyword)
            groupsList = groups["data"]
            for gr in groupsList:
                group_add(gr)
