import collections

from gym.utils import colorize as gym_colorize


def colorize(string, color, bold=False, highlight=False):
    if color:  # If not empty
        return gym_colorize(string, color, bold, highlight)
    else:
        return string


def deep_update(d, u=None, fixed=False, **kwargs):  # noqa: C901
    """Updates a dictionary recursively (deep update). This function takes a update
    dictionary and/or keyword arguments. When a keyword argument is supplied, the
    key-value pair is changed if it exists somewhere in the dictionary.

    Args:
        d (dict): Dictionary you want to update.
        u (dict, optional): The update dictionary.
        fixed (bool, optional): Whether you want the input dictionary to be fixed
            (i.e. only change keys that are already present). Defaults to ``False``.

    Returns:
        dict: The updated dictionary.

    .. seealso::
        Based on the answer given by `@alex-martelli <https://stackoverflow.com/users/95810/alex-martelli>`_
        on `this stackoverflow question <https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth>`_.
    """  # noqa: E501
    # Update dict based on input dictionary
    if u:
        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                if k in d.keys() or not fixed:
                    d[k] = deep_update(d.get(k, {}), v, fixed=fixed)
            else:
                if k in d.keys() or not fixed:
                    d[k] = v

    # Update dict based on keyword arguments
    for key, val in kwargs.items():
        for k, v in d.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = deep_update(v, fixed=fixed, **{key: val})
            else:
                if k == key and key in d.keys():
                    d[k] = val

    if not kwargs and not u:
        print(
            colorize(
                "WARNING: Returning original dictionary since no update dictionary or "
                "keyword argument was supplied.",
                color="yellow",
                bold=True,
            )
        )
    return d


if __name__ == "__main__":

    test_dict = {"One": 1, "test2": {"One": 1, "test4": False}}
    update_dict = {"jan": "test", "false": True, "test2": {"test4": True}}
    updated_dict = deep_update(test_dict, update_dict, One=2, test4=4)
    print(updated_dict)