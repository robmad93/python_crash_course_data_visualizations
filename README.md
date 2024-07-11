# Python crash course data visualizations
My attempts at the exercises provided within the data visualizations project section (chapters 15–17) of the incredible resource "Python Crash course" by Eric Matthes. The functions of the python files are summarized below.

## cubes.py
The code generates a scatter plot using Matplotlib, plotting the cubes of numbers from 1 to 5000. Each point's position corresponds to a number and its cube, with the color intensity of the points mapped to their cube values on a blue color scale. The plot is titled "Cubed Numbers," and the axes are labeled "Value" and "Cube of Value." The plot's tick labels are customized for better readability, and the axes' ranges are set to cover the values from 0 to 5000 for the x-axis and 0 to 130,000,000,000 for the y-axis.
![cubed_numbers_graph](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/fc06f835-a9a4-4e80-b1b6-24dbd86730be)

## death_valley_highs_lows.py
The code reads temperature data from a CSV file and plots the daily high and low temperatures for Death Valley in 2018 using Matplotlib. It first changes the working directory, opens the CSV file, and extracts the dates, high temperatures, and low temperatures. Missing data points are handled by printing a message. It then plots the high and low temperatures on the same graph, with high temperatures in red, low temperatures in blue, and the area between them shaded lightly. The plot is formatted with a title, labeled axes, and formatted date labels for clarity, and finally, the graph is displayed.

![temps_death_valley_2018](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/c74f7208-7c77-45bd-a7eb-1ac704012245)

## die.py
This code defines a Die class to simulate a die roll. The class has an initializer method that defaults to a six-sided die but can accept any number of sides. The roll method returns a random integer between 1 and the number of sides, simulating the roll of the die.

## die_visual.py
This code simulates rolling a six-sided die (D6) and a ten-sided die (D10) together 50,000 times, and then visualizes the frequency of each possible sum using Plotly. It imports necessary modules (including Die from die.py), creates the two dice, performs the rolls while storing the results, calculates the frequency of each possible result, and then generates a bar chart displaying these frequencies. The chart is saved as an HTML file named "d6_d10.html" with appropriate axis labels and a title.
![die_visual](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/a8665848-0a36-4e9b-80e1-3d2717023733)

## eq_explore_data.py
This code reads earthquake data (eq_data_1_day_m1.json) and extracts the magnitudes, longitudes, and latitudes of each earthquake. It starts by importing the json module and opening the specified JSON file. The data is then loaded into a dictionary, and the relevant earthquake data is accessed through the "features" key. The code iterates over each earthquake's data, extracting and storing the magnitude, longitude, and latitude in separate lists. Finally, it prints the first ten magnitudes and the first five longitudes and latitudes for inspection.

## eq_world_map.py
This code visualizes global earthquake data using Plotly. It begins by importing necessary modules and opening a JSON file containing earthquake data. After loading the JSON data and accessing earthquake dictionaries under the "features" key, it iterates through each earthquake to extract magnitude, longitude, latitude, and title information. These values are stored in separate lists (mags, lons, lats, hover_texts). It then maps the earthquake data onto a Scattergeo plot, where each earthquake is represented by a marker whose size and color reflect its magnitude. The resulting interactive plot is saved as an HTML file named "global_earthquakes.html".

![global_eqs](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/96058ba3-d849-4113-9676-15797db9c434)

## hn_article.py
This code makes an API call to retrieve data from a specific Hacker News item and stores the response. It prints the status code of the response, converts the response to a JSON dictionary, and then writes this data to a file named readable_hn_data.json in a readable format with an indentation of 4 spaces.

## hn_submissions.py
This code retrieves the top 30 stories from Hacker News using their API, processes each story to extract the title, link, and number of comments, and then sorts the stories by the number of comments. It creates a bar chart visualization using Plotly, where each bar represents a story with clickable links on the x-axis oriented horizontally, showing the number of comments on the y-axis, and finally saves the chart as an HTML file named hn_discussions.html.

![most_active_discussions_on_Hacker_News](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/26c11204-c157-481e-ab3d-bf99bf436257)


## javascript_repos.py
This code makes an API call to GitHub to search for Javascript repositories sorted by stars, then prints the status code of the request. It stores the JSON response in a variable and prints the total number of repositories found. The code processes the response to explore information about the repositories, specifically printing out selected details such as name, owner, stars, URL, creation date, last update, and description for each repository returned by the search.

## javascriptn_repos_visual.py
This code makes an API call to GitHub to search for Javascript repositories sorted by stars and prints the status code of the request. It processes the response to extract repository names, URLs, star counts, and labels that include the owner's login and the repository description. Using this data, it creates a bar chart visualization with Plotly. The chart displays the most-starred Javascript projects on GitHub, where each bar represents a repository with hovertext showing additional details. The chart's appearance is customized with specific title fonts, axis labels, bar colors, and opacity settings, and the resulting plot is saved to an HTML file.

![most_starred_js_projects_github](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/0ca72c7f-b948-4761-9c91-ab0758d8540c)

## mpl_squares.py
This code uses Matplotlib to create a line plot of squared numbers. It begins by importing Matplotlib and setting a specific style ("fivethirtyeight"). It defines input_values as a list of x-axis values and squares as their corresponding squared values. The code then creates a figure and axis object, plots input_values against squares with a specified linewidth, and sets the title and labels for the chart. Finally, it adjusts the tick label sizes and displays the plot using plt.show().

## python_repos.py
Similar to javascript_repos.py. This code makes an API call to GitHub to search for Python repositories sorted by stars, then prints the status code of the request. It stores the JSON response in a variable and prints the total number of repositories found. The code processes the response to explore information about the repositories, specifically printing out selected details such as name, owner, stars, URL, creation date, last update, and description for each repository returned by the search.

## python_repos_visual.py
This code makes an API call to GitHub to search for Python repositories sorted by stars and prints the status code of the request. It processes the response to extract repository names, URLs, star counts, and labels that include the owner's login and the repository description. Using this data, it creates a bar chart visualization with Plotly. The chart displays the most-starred Python projects on GitHub, where each bar represents a repository with hovertext showing additional details. The chart's appearance is customized with specific title fonts, axis labels, bar colors, and opacity settings, and the resulting plot is saved to an HTML file.

![most_starred_python_projects_github](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/3bb5e3f3-0ceb-4c63-8cec-6cb56aa11af4)


## random_walk.py
This code defines a class RandomWalk that generates random walks in a 2D plane. Upon initialization, it sets the number of points for the walk (num_points) and initializes starting coordinates ((0, 0)). The get_step method randomly determines the direction and distance of a step. The fill_walk method calculates each point of the walk by continuously generating steps until the specified number of points (num_points) is reached. It ensures that steps do not result in the walker staying in place (x_step == 0 and y_step == 0), discarding such moves and recalculating new positions.

## rw_visual.py
This code continuously generates and displays random walks using Matplotlib until the user decides to stop. Inside the infinite loop (while True), it creates a RandomWalk object with 50,000 points and fills it using the fill_walk method. Matplotlib is then used to plot the points of the walk on a scatter plot, adjusting the plot style (plt.style.use("classic")) and customizing the figure size (figsize=(15, 9)). The starting point of the walk is highlighted in green (ax.scatter(0, 0, c="green", edgecolors="none", s=100)), and the ending point is highlighted in red (ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)). The axes are hidden (ax.get_xaxis().set_visible(False) and ax.get_yaxis().set_visible(False)) to focus solely on the walk's path. After displaying the plot, the program asks the user if they want to generate another random walk (keep_running = input("Make another random walk? (y/n): ")). If the user enters "n", the loop breaks, ending the program.

![rw_visual](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/c49eb5ca-32b4-4e0e-b4ed-21c886bb588f)

## scatter_squares.py
This code uses Matplotlib to create a scatter plot of the squares of numbers from 1 to 1000. It initializes x_values and y_values to represent the range of numbers and their squares, respectively. The plot is styled with a classic style (plt.style.use("classic")) and each point is plotted with a size of 10 (s=10) and color mapped according to its y-value (c=y_values, cmap=plt.cm.Blues). The plot's title ("Square Numbers") and axes labels ("Value" and "Square of Value") are set, and tick labels are adjusted for readability (ax.tick_params(axis="both", which="major", labelsize=14)). The axis ranges are specified to fit the data appropriately (ax.axis([0, 1100, 0, 1100000])), and the plot is displayed using plt.show().

## show_color_scales.py
This code iterates through all the keys in the PLOTLY_SCALES dictionary provided by Plotly's colors module and prints each key.

## sikta_highs.py
This code reads temperature data from a CSV file ("sitka_weather_07-2018_simple.csv"), located in a specified directory. It starts by importing necessary modules (csv, datetime, os, matplotlib.pyplot). After setting the working directory using os.chdir, it opens the CSV file and reads its contents using csv.reader. The header row, which contains column names, is extracted using next(reader).

The code then iterates through each row in the CSV file, converting the date string (row[2]) to a datetime object and extracting the high temperature (row[5]). It stores these dates and temperatures in lists (dates and highs). After processing all rows, it prints the list of high temperatures (print(highs)).

Using Matplotlib, the code plots the high temperatures (highs) against dates (dates). It styles the plot with the "bmh" style (plt.style.use("bmh")) and specifies red color for the line plot (ax.plot(dates, highs, c="red")). The plot is then formatted with a title ("Daily high temperatures, July 2018"), labeled axes, and adjusted tick labels for clarity (plt.title, plt.xlabel, fig.autofmt_xdate, plt.ylabel, plt.tick_params). Finally, the plot is displayed using plt.show().

![sikta_highs](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/1fc67c6a-0766-40ef-8a91-4d3acf162e67)

## sikta_rainfall.py
This code analyzes and visualizes daily rainfall data from a CSV file ("sitka_weather_2018_simple.csv"). It begins by setting the working directory to where the data file is located. After opening the file and reading its contents with csv.reader, it skips the header row using next(reader) to avoid processing it as data.

The code then iterates through each row of the CSV file, converting the date string (row[2]) to a datetime object. It attempts to convert the rainfall value (row[3]) to a float, handling any potential ValueError exceptions by printing a message for missing data. Valid dates and corresponding rainfall rates are stored in lists (dates and rainfall_rate).

Using Matplotlib, the code plots the daily rainfall data. It sets the plot style to "bmh" (plt.style.use("bmh")), creates a figure and axis object, and plots the rainfall rates against dates (ax.plot(dates, rainfall_rate, c="blue")). The plot is formatted with a title ("Daily rainfall - 2018"), labeled axes, and adjusted tick labels for better readability (plt.title, plt.xlabel, fig.autofmt_xdate, plt.ylabel, plt.tick_params). Finally, the plot is displayed using plt.show().

![sikta_rainfall](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/3e96d9ae-f403-479e-b13a-2e0d18fbd289)

## sikta_highs_lows.py
This code is similar to sikta_highs.py but incorporates both the daily high and low temperatures on the same graph. It sets the plot style to "bmh" (plt.style.use("bmh")), creates a figure and axis object, and plots the high temperatures in red and low temperatures in blue (ax.plot(dates, highs, c="red", alpha=0.5), ax.plot(dates, lows, c="blue", alpha=0.5)). The area between the high and low temperatures is filled with light blue (plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)). The plot is formatted with a title ("Daily high and low temperatures - 2018"), labeled axes, and adjusted tick labels for clarity (plt.title, plt.xlabel, fig.autofmt_xdate, plt.ylabel, plt.tick_params). Finally, the plot is displayed using plt.show().

![sikta_highs_lows_2018](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/9140e37d-c6f7-4abf-8d24-6233ea1e6b49)

## test_python_repos.py
This code defines a unittest test case class TestPythonRepos that tests the GitHub API's response for Python repositories sorted by stars. In the setUp method, it makes an API call to GitHub and stores the response. It includes three tests: test_status_code verifies the API call was successful by checking the status code, test_total_repositories ensures the total number of repositories is greater than a given number (currently set to 50,000), and test_number_of_items checks that the number of items returned in the response is 30. The tests are run when the script is executed.

## wildfires_europe.py
This code reads data from a CSV file named "MODIS_C6_1_Europe_7d.csv" into a pandas DataFrame (df). The CSV file represents recent European wildfire data for the 1st week of July, 2024, obtained from https://firms.modaps.eosdis.nasa.gov/active_fire/. Using Plotly Express, the code creates a density map on a Mapbox map, plotting wildfire data across Europe based on latitude and longitude coordinates. The intensity of each point is represented by the "frp" column (representing "Fire Radiative Power in MW"). The map is centered around latitude 42.83 and longitude -8.35, zoomed to level 8, and styled with an open street map style. Finally, it displays the interactive map.

![wildfires_europe_week_1_july_2024](https://github.com/robmad93/python_crash_course_data_visualizations/assets/131868277/3d3c81a5-5e6d-43c4-bf48-2ab1dec17700)
