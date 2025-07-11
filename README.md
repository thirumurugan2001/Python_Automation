# Azure Pricing Calculator Automation

A Flask-based web service that automates Azure pricing calculations by scraping the Azure Pricing Calculator website using Playwright.

## Overview

This application provides a REST API endpoint that accepts Azure service configuration parameters and returns pricing information by automating interactions with the Azure Pricing Calculator website.

## Features

- **Automated Pricing Retrieval**: Scrapes Azure pricing calculator for real-time pricing data
- **REST API**: Simple POST endpoint for pricing calculations
- **Input Validation**: Comprehensive validation of required fields
- **Error Handling**: Robust error handling with detailed error messages
- **Flexible Configuration**: Supports various Azure service configurations

## Project Structure

```
├── main.py           # Flask application entry point
├── controller.py     # Request validation and routing logic
├── scraping.py       # Playwright automation for Azure pricing calculator
└── README.md         # Project documentation
```

## Requirements

- Python 3.7+
- Flask
- Playwright
- Chromium browser (installed via Playwright)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thirumurugan2001/Python_Automation.git
```

2. Navigate to the project directory:
```bash
cd Python_Automation
```

3. Install required dependencies:
```bash
pip install flask playwright
```

4. Install Playwright browsers:
```bash
playwright install chromium
```

## Usage

### Starting the Server

Run the Flask application:
```bash
python main.py
```

The server will start on `http://0.0.0.0:8080` with debug mode enabled.

### API Endpoint

**POST** `/automate_azure_pricing`

#### Request Body

```json
{
    "productName": "Azure Functions",
    "region": "us-east",
    "tier": "premium",
    "instance": "ep1-payg",
    "preWarmedCount_input": 5,
    "preWarmedCountHoursFactor": "24",
    "preWarmedCountHoursFactor_input": 730,
    "additionalUnitsCount_input": 1000000,
    "additionalUnitsCountHoursFactor": "24",
    "additionalUnitsCountHours_input": 730
}
```

#### Required Fields

- `productName`: Azure service name
- `region`: Azure region
- `tier`: Service tier
- `instance`: Instance type
- `preWarmedCount_input`: Number of pre-warmed instances
- `preWarmedCountHoursFactor`: Time factor for pre-warmed instances
- `preWarmedCountHoursFactor_input`: Hours for pre-warmed instances
- `additionalUnitsCount_input`: Additional units count
- `additionalUnitsCountHoursFactor`: Time factor for additional units
- `additionalUnitsCountHours_input`: Hours for additional units

#### Response

**Success Response:**
```json
{
    "status": true,
    "message": "Successfully Data Scraped",
    "Upfront Cost": "$0.00",
    "Monthly Cost": "$12.34"
}
```

**Error Response:**
```json
{
    "status": false,
    "message": "Missing or empty field: productName",
    "status_code": 400
}
```

### Example Usage

```bash
curl -X POST http://localhost:8080/automate_azure_pricing \
  -H "Content-Type: application/json" \
  -d '{
    "productName": "Azure Functions",
    "region": "us-east",
    "tier": "consumption",
    "instance": "standard",
    "preWarmedCount_input": 5,
    "preWarmedCountHoursFactor": "monthly",
    "preWarmedCountHoursFactor_input": 730,
    "additionalUnitsCount_input": 1000000,
    "additionalUnitsCountHoursFactor": "monthly",
    "additionalUnitsCountHours_input": 730
  }'
```

## How It Works

1. **Request Validation**: The controller validates all required fields in the incoming request
2. **Browser Automation**: Playwright launches a Chromium browser and navigates to the Azure Pricing Calculator
3. **Form Interaction**: The script fills out the pricing calculator form with the provided parameters
4. **Data Extraction**: Pricing information is extracted from the results page
5. **Response**: The pricing data is returned as a JSON response

## Error Handling

The application includes comprehensive error handling:

- **Input Validation**: Checks for missing or empty required fields
- **Browser Automation**: Handles web scraping errors and timeouts
- **Value Constraints**: Automatically adjusts input values to stay within min/max limits
- **Exception Handling**: Catches and reports all exceptions with detailed error messages

## Configuration

### Browser Settings

The application runs with `headless=False` by default for debugging purposes. To run in headless mode for production, modify the browser launch settings in `scraping.py`:

```python
browser = p.chromium.launch(headless=True)
```

### Server Configuration

Server settings can be modified in `main.py`:
- **Port**: Default is 8080
- **Host**: Default is 0.0.0.0 (all interfaces)
- **Debug**: Enabled by default

## Limitations

- Depends on Azure Pricing Calculator website structure
- Requires internet connection
- May break if Azure changes their website layout
- Currently supports Azure Functions pricing specifically

## Support

For issues, questions, or contributions, please contact:
- **Email**: thirusubramaniyan2001@gmail.com
- **Repository**: https://github.com/thirumurugan2001/Python_Automation.git

## License

This project is open source. Please check the repository for license details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Disclaimer

This tool is for educational and automation purposes. Please ensure compliance with Azure's terms of service when using automated tools to access their pricing calculator.
