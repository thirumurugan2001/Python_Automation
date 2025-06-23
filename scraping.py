from playwright.sync_api import sync_playwright

def automate_azure_pricing(data):
    try : 
        productName =data['productName']
        region=data['region']
        tier=data['tier']
        instance=data['instance']
        preWarmedCount_input=data['preWarmedCount_input']
        preWarmedCountHoursFactor=data['preWarmedCountHoursFactor']
        preWarmedCountHoursFactor_input=data['preWarmedCountHoursFactor_input']
        additionalUnitsCount_input=data['additionalUnitsCount_input']
        additionalUnitsCountHoursFactor=data['additionalUnitsCountHoursFactor']
        additionalUnitsCountHours_input=data['additionalUnitsCountHours_input']
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://azure.microsoft.com/en-in/pricing/calculator")
            page.wait_for_selector('input[data-testid="product-search-input"]')
            page.fill('input[data-testid="product-search-input"]', productName)
            page.click('button[data-testid="functions-picker-item"]')
            page.wait_for_selector('select[name="region"]')
            page.select_option('select[name="region"]', value=region)
            page.wait_for_selector('select[name="tier"]')
            page.select_option('select[name="tier"]', value=tier)
            page.wait_for_selector('select[name="instance"]')
            page.select_option('select[name="instance"]', value=instance)
            input_selector = 'input[name="preWarmedCount"]'
            page.wait_for_selector(input_selector)
            min_val = int(page.get_attribute(input_selector, 'min'))
            max_val = int(page.get_attribute(input_selector, 'max'))
            if preWarmedCount_input <= 0:
                final_value = min_val
            elif preWarmedCount_input > max_val:
                final_value = max_val
            else:
                final_value = preWarmedCount_input
            page.fill(input_selector, str(final_value))
            page.wait_for_selector('select[name="preWarmedCountHoursFactor"]')
            page.select_option('select[name="preWarmedCountHoursFactor"]', value=preWarmedCountHoursFactor)
            preWarmedCountHoursFactor_Select = 'input[name="preWarmedCountHours"]'
            preWarmedCountHoursFactor_min_val = int(page.get_attribute(preWarmedCountHoursFactor_Select, 'min'))
            preWarmedCountHoursFactor_max_val = int(page.get_attribute(preWarmedCountHoursFactor_Select, 'max'))
            if preWarmedCountHoursFactor_input <= 0:
                preWarmedCountHoursFactor_final_value = preWarmedCountHoursFactor_min_val
            elif preWarmedCountHoursFactor_input > preWarmedCountHoursFactor_max_val:
                preWarmedCountHoursFactor_final_value = preWarmedCountHoursFactor_max_val
            else:
                preWarmedCountHoursFactor_final_value = preWarmedCountHoursFactor_input
            page.fill(preWarmedCountHoursFactor_Select, str(preWarmedCountHoursFactor_final_value))    
            additionalUnitsCount = 'input[name="additionalUnitsCount"]'
            page.wait_for_selector(additionalUnitsCount)
            additionalUnitsCount_min_val = int(page.get_attribute(additionalUnitsCount, 'min'))
            additionalUnitsCount_max_val = int(page.get_attribute(additionalUnitsCount, 'max'))
            if additionalUnitsCount_input <= 0:
                additionalUnitsCount_final_value = additionalUnitsCount_min_val
            elif additionalUnitsCount_input > additionalUnitsCount_max_val:
                additionalUnitsCount_final_value = additionalUnitsCount_max_val
            else:
                additionalUnitsCount_final_value = additionalUnitsCount_input
            page.fill(additionalUnitsCount, str(additionalUnitsCount_final_value))
            page.wait_for_selector('select[name="additionalUnitsCountHoursFactor"]')
            page.select_option('select[name="additionalUnitsCountHoursFactor"]', value=additionalUnitsCountHoursFactor)
            additionalUnitsCountHoursFactor_Select = 'input[name="additionalUnitsCountHours"]'
            page.wait_for_selector(additionalUnitsCountHoursFactor_Select)
            additionalUnitsCountHours_min_val = int(page.get_attribute(additionalUnitsCountHoursFactor_Select, 'min'))
            additionalUnitsCountHours_max_val = int(page.get_attribute(additionalUnitsCountHoursFactor_Select, 'max'))
            if additionalUnitsCountHours_input <= 0:
                additionalUnitsCountHours_final_value = additionalUnitsCountHours_min_val
            elif additionalUnitsCountHours_input > additionalUnitsCountHours_max_val:
                additionalUnitsCountHours_final_value = additionalUnitsCountHours_max_val
            else:
                additionalUnitsCountHours_final_value = additionalUnitsCountHours_input
            page.fill(additionalUnitsCountHoursFactor_Select, str(additionalUnitsCountHours_final_value))
            upfront_cost = page.inner_text('div.total:has(span.sub-total:text("Upfront cost")) span.text-center')
            monthly_cost = page.inner_text('div.total:has(span.sub-total:text("Monthly cost")) span.text-center')
            browser.close()
            return {
                "status": True,
                "message": "Succssufully Data Scraped",
                "Upfront Cost":upfront_cost,
               "Monthly Cost":monthly_cost
            }
    except Exception as e: 
        print("Error in the automate_azure_pricing function: ", str(e))
        return {
            "status": False,
            "message": "Error in the automate_azure_pricing function: " + str(e),
            "Upfront Cost":0.00,
            "Monthly Cost":0.00
        }