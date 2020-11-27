import random
from model.group import Group


def test_delete_group(app):
    if len(app.group.get_group_list()) == 1:
        app.group.add_new_group(Group(name="new group"))
    old_groups = app.group.get_group_list()
    group_to_delete = random.choice(old_groups)
    app.group.delete_group(group_to_delete)
    new_groups = app.group.get_group_list()
    del old_groups[group_to_delete.id-1]
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)