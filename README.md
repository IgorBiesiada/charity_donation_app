# 🎁 Charity Donation - Portfolio Lab

## 📌 Project Overview
This application is a **Portfolio Lab** project developed as part of the **Python Developer** course at **Coders Lab**. It is a platform designed to connect donors with verified organizations and local collections. Users can donate items like clothes or toys, while the system tracks total bags donated and supported institutions.

## 🛠 Tech Stack
* **Language:** Python 3.12+
* **Framework:** Django 4.2
* **Database:** PostgreSQL (with `psycopg2-binary`)
* **Frontend:** HTML5, CSS3, JavaScript (PortfolioLab Layout)

---

## ✅ Completed Tasks

### 🏗️ 1. Project & Environment Setup
* **Virtual Environment**: Set up a dedicated `venv` and installed required packages: `django` and `psycopg2-binary`.
* **Database Setup**: Created a **PostgreSQL** database named `charity-donation`.
* **Django Configuration**: Properly modified project settings, executed initial migrations, and registered the core application.
* **Verification**: Confirmed server stability and successful initial launch.

### 📊 2. Data Modeling
* **Category Model**: Created with a `name` attribute.
* **Institution Model**: Implemented with `name`, `description`, `type` (*Foundation, NGO, Local Collection*), and Many-to-Many relationship with categories.
* **Donation Model**: Developed with fields for `quantity` (bags), `categories`, `institution`, `address`, `phone_number`, `city`, `zip_code`, `pick_up_date`, `pick_up_time`, and a Nullable `user` foreign key.

### 🎨 3. Frontend & Template Architecture
* **Layout Integration**: Imported and configured the PortfolioLab HTML layout within the Django environment.
* **DRY Principles**: Implemented template inheritance using `base.html` with `{% extends %}` and `{% include %}` tags for modularity.
* **Static Management**: Set up static folders and converted all asset paths to use the Django `{% static %}` tag.
* **Partials**: Reorganized the frontend into a `partials/` directory for better maintainability (e.g., `header.html`, `help.html`, `statsContainer.html`).

### ⚡ 4. View Logic & Dynamic Content
* **Functional Views**: Created views for `LandingPage`, `AddDonation`, `Login`, and `Register`.
* **Live Statistics**: Implemented dynamic counters for total donated bags (using ORM `Sum` aggregation) and the total number of supported organizations.
* **Dynamic Help Section**: Integrated the "Who do we help?" section to pull real-time data for Foundations, NGOs, and Local Collections directly from the database.
* **Persistent Navigation**: Fixed anchor links (`#id-sections`) in the menu to ensure they correctly redirect to the main page sections from any view (e.g., from the login or registration pages).

---

## 🚀 Installation & Running

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/IgorBiesiada/charity_donation_app.git](https://github.com/IgorBiesiada/charity_donation_app.git)