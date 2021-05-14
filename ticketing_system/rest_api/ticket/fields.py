import rest_api.models as models

def impact_field_to_internal_value(value):
    impact_int_value = None
    for a, b  in models.Ticket.Impact.choices:
        if b == value:
            impact_int_value = a
            break
    return impact_int_value

def impact_field_to_representation(value):
    choices_dict = dict(models.Ticket.Impact.choices)
    if value not in choices_dict:
        return None
    return choices_dict[value]
