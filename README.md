<div align="center">
<h1>Django Practice Project</h1>
<em>Personal Cash Management Web App</em>
</div>

### Job : Develop a Personal Cash Management web app

> Develop a Personal Cash Management web app to provide users with a convenient and efficient way to manage their finances. This application helps individuals track their income, expenses, and transactions, allowing them to gain insights into their spending habits, save money, and maintain financial stability.

### Job Specification information:

- Create a new Django project named Name_ID_ManageCash.
- Create a Django app named ManageCash.
- Define the required models for the portfolio app in the models.py file.
  - AddCash (user {many to one User}, source, datetime, amount, description)
  - Expense (many to one User), description, amount, datetime)
- Create views for Login (username/email and password) and Registration (username, email, password, confirm password) pages.
- Create required Django templates:
  - Profile management view.
  - Cash Management Dashboard.
  - Transaction form (AddCash/Expense)
- Define URL Patterns and configure project-level URLs.
- Implement the required Function and Logic in the view.py file.

> [!IMPORTANT]
>
> 1. Create a new Django project. (Naming Convention: Name_ID_ManageCash)
>
> 2. Run migration to create the data tables.
>
> 3. Create a super user. (username: admin, password: 1234)
>
> 4. Register your models to the Django admin.
