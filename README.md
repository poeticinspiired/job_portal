# Job Portal and Recruitment Management System

## Overview

The Job Portal and Recruitment Management System is a web application designed to connect employers with job seekers. It features user authentication, job search functionality, job application tracking, and an admin dashboard for managing job listings and candidate applications.

## Features

- **User Authentication:**
  - Employers can create accounts and log in to manage their job postings.
  - Candidates can sign up and log in to apply for jobs.
- **Job Search:**
  - Users can search for jobs by keyword, location, or category.
  - Job listings include relevant information like job title, description, salary range, and application instructions.
- **Application Tracking:**
  - Employers can track candidate applications and manage their hiring process.
  - Candidates can view the status of their job applications.
- **Admin Dashboard:**
  - Employers can manage their job postings and access application data.
  - Administrators can moderate user activity, manage job listings, and monitor system performance.

## Technical Requirements

- **Frontend:**
  - HTML, CSS, JavaScript
- **Backend:**
  - Python, Django
- **Database:**
  - PostgreSQL
- **Version Control:**
  - Git

## Installation

### Prerequisites

- Python 3.6+
- PostgreSQL

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/job_portal.git
   cd job_portal
   ```

2. **Set up a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   Update the `DATABASES` setting in `job_portal/settings.py` with your PostgreSQL credentials.

5. **Create the database and apply migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Open your browser and navigate to `http://127.0.0.1:8000/` to see the application.**

## Usage

- **Registration:**
  - Employers and candidates can register through the `/register` endpoint.
- **Login:**
  - Users can log in through the `/login` endpoint.
- **Profile:**
  - Users can view their profile through the `/profile` endpoint.
- **Job Listings:**
  - Employers can create job listings, and candidates can search for and apply to job listings.

## API Endpoints

- **Job Listings:**
  - `GET /api/joblistings/`: Retrieve a list of job listings.
  - `POST /api/joblistings/`: Create a new job listing (employers only).
  - `GET /api/joblistings/{id}/`: Retrieve a specific job listing.
  - `PUT /api/joblistings/{id}/`: Update a job listing (employers only).
  - `DELETE /api/joblistings/{id}/`: Delete a job listing (employers only).

- **Applications:**
  - `GET /api/applications/`: Retrieve a list of applications.
  - `POST /api/applications/`: Create a new application (candidates only).
  - `GET /api/applications/{id}/`: Retrieve a specific application.
  - `PUT /api/applications/{id}/`: Update an application (employers only).
  - `DELETE /api/applications/{id}/`: Delete an application (employers only).

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

