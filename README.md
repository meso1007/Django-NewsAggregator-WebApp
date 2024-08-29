# News Aggregator

This project is a news carousel application that fetches the latest headlines from BBC News and displays them in a stylish and interactive carousel format. It uses Python for web scraping, HTML for structure, CSS for styling, and JavaScript for functionality.

## Features

- **Fetch Latest News:** Scrapes the latest headlines from the BBC News homepage.
- **Carousel Display:** Shows news items in a visually appealing carousel with navigation controls.
- **Responsive Design:** Adapts to different screen sizes for a seamless experience on various devices.
- **Image and Date Extraction:** Retrieves article images and publication dates for each news item.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Django (Web framework)
- An environment to run HTML, CSS, and JavaScript (e.g., a web browser)

### Setup

1. **Clone the Repository**

   ```bash
   ・git clone https://github.com/meso1007/Django-NewsAggregator-WebApp.git
   ・git clone git@github.com:meso1007/Django-NewsAggregator-WebApp.git
   cd newsaggregators
   ```

2. **Set Up a Virtual Environment**

   ````bash
   env\Scripts\activate #Windows
   source env/bin/activate #macOS/Linux   ```
   ````

3. **Install Dependencies**
   ```bash
   pip install requests beautifulsoup4 Django
   ```
4. **Start the Django Development Server**

   ```bash
   python manage.py runserver
   ```

## Usage

### Viewing News

The carousel will automatically rotate through the latest news articles. Use the arrows to navigate between news items manually.

### Customization

- **Styling:** Modify `styles.css` to change the appearance of the carousel.
- **Functionality:** Adjust `app.js` for different carousel behaviors or animations.
- **Scraping:** Update `scraper.py` to change the news source or format.

## File Structure

- `scraper.py`: Python script to scrape news data.
- `index.html`: Main HTML file for the web page.
- `styles.css`: CSS file for styling the carousel and layout.
- `app.js`: JavaScript file for carousel functionality.
- `data.json`: (Optional) File where the scraped news data is stored.
- `manage.py`: Django management script.
- `news_aggregator/`: Directory containing Django project files.
  - `news_aggregator/settings.py`: Django settings file.
  - `news_aggregator/urls.py`: Django URL configuration file.
  - `news_aggregator/wsgi.py`: WSGI entry point for the Django project.

## References

- [BBC News](https://www.bbc.com) - News source for the carousel.
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - For web scraping.
- [Django Documentation](https://docs.djangoproject.com/en/stable/) - For Django framework information.
- [Poppins Font](https://fonts.google.com/specimen/Poppins) - Font used in the design.

## Contact

- **Email:** diegoshoya2017@gmail.com
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/shoya-horiuchi-83b785278/)
- **GitHub:** [GitHub Profile](https://github.com/meso1007)
