# -*- coding: utf-8 -*-
from tdg_fb_group import ma


class GroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'group_id', 'group_name', 'privacy', 'created_at', 'updated_at')
        exclude = ('created_at', 'updated_at', 'id')
group_schema = GroupSchema()
group_schema = GroupSchema(many = True)