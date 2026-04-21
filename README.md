[![lang ru](https://img.shields.io/badge/lang-ru-blue)](https://github.com/EmilioAugust/Collector/blob/main/README.ru.md)
[![lang en](https://img.shields.io/badge/lang-en-red)](https://github.com/EmilioAugust/QA-of-Sauce)

# Test Automation — SauceDemo

## Project Overview
This project contains automated UI tests for the SauceDemo e-commerce application.

The goal is to demonstrate a structured QA approach including:
- Test planning
- Test design (checklists & test cases)
- UI automation
- Reporting and CI integration

Application under test: https://www.saucedemo.com/

---

## Scope

The following features are covered:

- Login functionality
- Product inventory
- Cart operations
- Checkout process

---

## Tech Stack

- Python
- pytest
- Playwright
- Allure Report
- GitHub Actions (CI)

---

## Framework Architecture

The project follows best practices:

- Page Object Model (POM)
- Pytest fixtures for setup/teardown
- Test data separation
- Parameterized tests
- Modular and scalable structure

---

## Documentation

- Test Plan → `docs/TEST_PLAN.md`
- Checklist → `docs/checklist.md`
- Test Cases → `docs/test_cases.md`

---

## ▶️ How to Run Tests

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
pytest
```

3. Run with Allure:
```bash
pytest --alluredir=reports
allure serve reports
```

---

## Reporting

Test results are generated using Allure Report and include:
- Test execution steps
- Screenshots on failure
- Detailed logs

---

## CI Integration

Tests are automatically executed via GitHub Actions on each push.

---

## Contributing

PRs are welcome!
Feel free to add new sources or improve code structure.

---

## License

MIT — free for all use.