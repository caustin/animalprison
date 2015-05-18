def add_url_rule(blue_print, path, view_function, methods_list, defaults_dict=None):
    """

    :param blue_print:
    :param path:
    :param view_function:
    :param methods_list:
    :param defaults_dict:
    :return:
    """

    if defaults_dict:
        blue_print.add_url_rule(
            path, view_func=view_function, methods=methods_list,defaults=defaults_dict
        )
    else:
        blue_print.add_url_rule(path, view_func=view_function, methods=methods_list)