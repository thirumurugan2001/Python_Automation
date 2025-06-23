from scraping import automate_azure_pricing

def Controller(data):
    try:
        required_fields = [
            'productName', 'region', 'tier', 'instance',
            'preWarmedCount_input', 'preWarmedCountHoursFactor',
            'preWarmedCountHoursFactor_input', 'additionalUnitsCount_input',
            'additionalUnitsCountHoursFactor', 'additionalUnitsCountHours_input'
        ]
        for field in required_fields:
            if field not in data or data[field] in [None, '', []]:
                return {
                    "status": False,
                    "message": f"Missing or empty field: {field}",
                    "status_code": 400
                }
        return automate_azure_pricing(data)

    except Exception as e:
        return {
            "status": False,
            "message": str(e),
            "status_code": 400
        }
