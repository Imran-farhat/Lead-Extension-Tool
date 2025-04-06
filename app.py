from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    # Get query parameters
    query = request.args.get('query', '')
    location = request.args.get('location', '')
    experience_level = request.args.get('experienceLevel', '')
    work_type = request.args.get('workType', '')
    
    print(f'Searching for: {query} in {location} (Experience: {experience_level}, Work Type: {work_type})')
    
    try:
        # Create LinkedIn URL
        url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={query}&location={location}&f_TPR=r86400&start=0"
        
        # Make request to LinkedIn
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return jsonify({"error": f"Failed to fetch jobs: HTTP {response.status_code}"}), 500
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.find_all('li')
        
        jobs = []
        for li in job_cards:
            try:
                card = li.find('div', class_='job-search-card')
                if card:
                    job_id = card.get('data-entity-urn', '').split(':')[-1] if card.get('data-entity-urn') else ''
                    title = card.find('h3', class_='base-search-card__title').text.strip() if card.find('h3', class_='base-search-card__title') else 'No Title'
                    company = card.find('h4', class_='base-search-card__subtitle').text.strip() if card.find('h4', class_='base-search-card__subtitle') else 'No Company'
                    location = card.find('span', class_='job-search-card__location').text.strip() if card.find('span', class_='job-search-card__location') else 'No Location'
                    
                    job = {
                        'id': job_id,
                        'title': title,
                        'company': company,
                        'location': location,
                        'experienceLevel': 'Entry Level',  # Default value
                        'workType': 'Full-time'  # Default value
                    }
                    jobs.append(job)
            except Exception as e:
                print(f"Error parsing job card: {e}")
        
        # Apply filters
        filtered_jobs = jobs
        if experience_level:
            filtered_jobs = [job for job in filtered_jobs if job['experienceLevel'] == experience_level]
        if work_type:
            filtered_jobs = [job for job in filtered_jobs if job['workType'] == work_type]
        
        print(f"Found {len(filtered_jobs)} jobs for query: '{query}'")
        return jsonify(filtered_jobs)
    
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return jsonify({"error": "Failed to fetch jobs"}), 500

if __name__ == '__main__':
    app.run(debug=True)