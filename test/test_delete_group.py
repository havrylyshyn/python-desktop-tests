import random


def test_delete_group(app):
    if len(app.group.get_group_list()) == 1:
        app.group.add_new_group("group to delete")
    old_groups = app.group.get_group_list()
    group_to_delete = random.choice(old_groups)
    app.group.delete_group(group_to_delete)
    new_groups = app.group.get_group_list()
    old_groups.remove(group_to_delete)
    assert sorted(new_groups) == sorted(old_groups)