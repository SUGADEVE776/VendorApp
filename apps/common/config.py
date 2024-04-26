_COMMON_MESSAGES = {
    "null_blank": "Please fill this field. This field cannot be left empty."
}

CUSTOM_ERRORS_MESSAGES = {
    "Others": {
        "blank": _COMMON_MESSAGES["null_blank"],
        "null": _COMMON_MESSAGES["null_blank"],
    },
    "ManyRelatedField": {
        "empty": "Please select one or more options. At least one is required.",
    },
    "PrimaryKeyRelatedField": {
        "does_not_exist": "Please select a valid option. The selected option is invalid or does not exist.",
        "incorrect_type": "The given name/value is invalid or the expected data "
        "does not belong to the corresponding filtering hierarchy.",
    },
}
