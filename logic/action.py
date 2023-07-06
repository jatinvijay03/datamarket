import ckan.plugins.toolkit as tk
import ckanext.datamarket.logic.schema as schema


@tk.side_effect_free
def datamarket_get_sum(context, data_dict):
    tk.check_access(
        "datamarket_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.datamarket_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'datamarket_get_sum': datamarket_get_sum,
    }
