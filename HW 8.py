import BMY

user_data = BMY.get_user_data()
valid_name = BMY.validate_name(user_data["name"])
valid_height = BMY.validate_height(user_data["height"])
valid_weight = BMY.validate_weight(user_data["weight"])
bmi = BMY.calc_BMI(valid_weight,valid_height)
bmi_category = BMY.calc_BMI_category(bmi)
BMY.print_results(bmi_category)