# -*- coding: utf-8 -*-
from flask import request
from tdg_fb_group.api.groups import group_add
from tdg_fb_group.schema.groups import group_schema
from tdg_fb_group.models.groups import Groups
from tdg_fb_group import app
from flask import Response
import json


@app.route("/group", methods=['POST', 'GET'])
def add_group():
    if request.method == 'POST':
        data = request.get_json()
        jsondata = group_add(data)
        return jsondata
    else:
        per_page = int(request.args.get('per_page', 10))
        page = int(request.args.get('page', 1))
        groups = Groups.query.order_by(Groups.id.desc()).offset((page - 1) * per_page).limit(per_page).all()

        return group_schema.jsonify(groups)

