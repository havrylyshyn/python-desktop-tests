def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.add_new_group("name")
    new_groups = app.group.get_group_list()
    old_groups.append("name")
    assert sorted(new_groups) == sorted(old_groups)
