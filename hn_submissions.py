from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

import requests

# Make an API call and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:  # Loop through top 30 submissions.
    # Make a separate API call per submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict.get(
            "title", "No title available"
        ),  # Return a default value of "No title available" if the title key is not present.
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get(
            "descendants", 0
        ),  # Return default value of 0 if the descendants key is not present.
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Extract data for visualization.
titles = [submission["title"] for submission in submission_dicts]
hn_links = [submission["hn_link"] for submission in submission_dicts]
comments = [submission["comments"] for submission in submission_dicts]

# Create clickable links for the x-axis.
clickable_links = [
    f'<a href="{link}" target="_blank">{title}</a>'
    for link, title in zip(hn_links, titles)
]

# Make visualization.
data = [
    {
        "type": "bar",
        "x": clickable_links,
        "y": comments,
        "hovertext": titles,
        "marker": {  # Marker settings affect bar designs.
            "color": "rgb(60, 100, 150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
        },
        "opacity": 0.6,
    }
]
my_layout = {
    "title": "Most Active Discussions on Hacker News",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Topic",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
        "tickangle": -45,  # Rotate the x-axis labels to be horizontal towards the right.
    },
    "yaxis": {
        "title": "Number of comments",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="hn_discussions.html")
