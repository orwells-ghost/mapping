import re, requests, bs4
def get_volDict():
	"""
	Function to collate dictionary of US volcanoes with elevation and geo coordinates by scraping wikipedia
	Input: None
	Output: Dictionary with keys as volcano names, int/float dict values in the form: 
	[['elevation'], ['latitude', 'longitude']] for each volcano (dict key)
	"""
	# URL links to wiki with tables of all US volcanoes. Headers required for status check so wikipedia doesn't think script it a bot 
	wiki_url = "https://en.wikipedia.org/wiki/List_of_volcanoes_in_the_United_States"
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

	# Request data from wiki_url using headers
	res = requests.get(wiki_url, headers=headers)
	res.raise_for_status() # Check status, break out of prog if 404

	# Parse html content into soup object
	soup = bs4.BeautifulSoup(res.content, 'html.parser')

	# Find all volcano tables by searching for CSS class wikitable. Len should be 21
	tables = soup.find_all('table', class_="wikitable")

	# Find every row of every table
	rows = tables[0].findAll('tr')

	# Temp vars. 
	skip_words = ["Name", "Elevation", "Location", "Last eruption", "meters", "feet", "Coordinates"]
	i = 0
	volDict = {}

	# Iterate through every table, and every row of every table, and every column of every row of every table
	for table in tables:

		for row in table.find_all('tr'):

			for col in row.find_all('td'):

				if col.text in skip_words: # Don't need column headings
					pass
				elif i == 0: # First iteration after skip words should be volcano name
					mName = col.text
					i += 1
				elif i == 1: # Meters are for commies
					i +=1
				elif i == 2: # Get elevation of volcano
					if len(col.text) <= 1: # Volcano's without elevation data default to 0
						elevation = 0
					elif len(col.text) > 3: # If the number has a comma in it i.e. > 3
						elevation = int(col.text.replace(',', ''))
					else:
						elevation = int(col.text)
					i += 1
				elif i == 3: # This iteration will be the Coordinates column
					t = col.find('span',{'class':'geo'}) # Search for decimal coords in span class geo
					if t: # Should return something like "34.23; 113.98"
						t = t.text.split(";")
						lat = float(t[0])
						lon = float(t[1])
					else: # Volcano's with missing coordinates data default to 0
						lat = 0
						lon = 0
					i += 1
				elif i == 4:
					i = 0
					volDict[mName] = [elevation, [lat,lon]] # Add Volcano and related data to dictionary
	return volDict