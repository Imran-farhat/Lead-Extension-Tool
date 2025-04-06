# LEAD EXTENSION - Job Search Platform

## Overview

LEAD EXTENSION is a modern job search platform that helps users discover job opportunities and company information from various sources. The platform features a clean, dark-themed interface with responsive design and interactive elements.

## Features

- **Job Search**: Search for jobs by title, location, experience level, and work type
- **Company Discovery**: Browse top companies by industry and see detailed company profiles
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Eye-friendly dark mode interface
- **Interactive UI**: Animated cards, hover effects, and smooth transitions
- **Pagination**: Browse through job listings with pagination support

## Technologies Used

- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Bootstrap 5 (Dark theme)
  - Font Awesome icons
  - jQuery
  - Animate.css for animations

- **Backend**:
  - Python
  - Flask web framework
  - BeautifulSoup for web scraping

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lead-extension.git
   cd lead-extension
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
lead-extension/
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   └── img/                 # Image assets
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   ├── jobs.html            # Jobs listing page
│   └── companies.html       # Companies page
├── app.py                   # Flask application
└── README.md                # This file
```

## API Endpoints

- `/api/jobs` - Returns job listings based on search criteria
  - Parameters:
    - `query`: Job title or keyword
    - `location`: Location filter
    - `experienceLevel`: Experience level filter
    - `workType`: Job type filter

## Screenshots

![Home Page](screenshots/home.png)
![Jobs Page](screenshots/jobs.png)
![Companies Page](screenshots/companies.png)

## Future Improvements

- Implement user authentication
- Add job saving/bookmarking functionality
- Enhance company profiles with more detailed information
- Add job application tracking
- Implement more advanced search filters

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For questions or support, please contact [your email].
