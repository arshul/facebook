
from tdg_fb_group.models.groups import Groups
from flask import jsonify

def group_add(group):
    group_info = Groups.query.filter_by(group_id=group['id']).first()
    if not group_info:
        group_info = Groups(group)
        group_info.save()

    else:
        group_info.group_name = group['name']
        group_info.update()
    return jsonify({'success': 'group added'})
