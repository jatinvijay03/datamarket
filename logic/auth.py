import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def datamarket_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "datamarket_get_sum": datamarket_get_sum,
    }