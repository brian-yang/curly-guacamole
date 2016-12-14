def get_list_of_food_nutrients(fooddata):
    for search_result in fooddata.items():
        for section in search_result:
            if isinstance(section, list):
                for table in section:
                    print table["nutrient"]
            else:
                print section
            print ""

def parse_sections(section):
    nutrient_names = ["Total lipid (fat)", "Calcium, Ca", "Iron, Fe", "Energy", "Fiber, total dietary"]

    entries = {}

    for table in section:
        if table["nutrient"] in nutrient_names:
            entries[table["nutrient"]] = entries[table["value"] + table["unit"]]

    return entries

def show_nutrients(fooddata):
    for section in search_result:
        if isinstance(section, list):
            return parse_sections(section)
