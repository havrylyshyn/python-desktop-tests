from model.group import Group


def test_add_group(app, excel_groups):
    group = excel_groups
    old_groups = app.group.get_group_list()
    app.group.add_new_group(group)
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
