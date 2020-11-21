import os
import requests
from dotenv import load_dotenv
from todoist.api import TodoistAPI

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Set API URL paths and headers
path = "https://api.todoist.com/rest/v1/"
project_path = f"{path}projects"
section_path = f"{path}sections"
task_path = f"{path}tasks"
api_header = {"Authorization": "Bearer %s" % API_KEY}

def main():
    bid_list()

def bid_list():
    """
    Call Todoist API and return all task in the "Bids" section of "Schnabel" project
    Returns list of task objects
    Task name can be accessed by obj["content"]
    """
    # Grab all projects
    projects = request_api(project_path)

    # Parse and find "Schnabel" project id
    sfc_id = None
    for project in projects:
        if project["name"] == "Schnabel":
            sfc_id = project["id"]
            break

    # Grab all sections in "Schnabel" project
    params = {"project_id": sfc_id}
    sections = request_api(section_path, params=params)

    # Determine "Bids" section id
    bidding_id = None
    for section in sections:
        if section["name"] == "Bids":
            bidding_id = section["id"]
            break
        
    # Grab all tasks in "Schnabel" project
    params = {"project_id": sfc_id}
    tasks = request_api(task_path, params=params)

    # Filter tasks based on section id
    bid_tasks = []
    for task in tasks:
        if task["section_id"] == bidding_id:
            bid_tasks.append(task)

    # Sort and return bid_tasks
    bid_tasks_sorted = quicksort(bid_tasks)
    return bid_tasks_sorted

def request_api(url, params=None):
    try:
        response = requests.get(
            url,
            headers = api_header,
            params = params
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def quicksort(array):
    l = len(array)
    if l <= 1:
        return array
    else:
        pivot_index = l - 1
        array_index = 0
        while pivot_index > array_index:
            while array[array_index]["order"] > array[pivot_index]["order"]:
                if array_index == pivot_index - 1:
                    element = array.pop(array_index)
                    array.insert(pivot_index, element)
                else:
                    prev_elem = array.pop(pivot_index - 1)
                    element = array.pop(array_index)
                    array.insert(array_index, prev_elem)
                    array.insert(pivot_index, element)
                pivot_index -= 1
            array_index += 1
        first_half = quicksort(array[:pivot_index])
        second_half = quicksort(array[pivot_index + 1:])
        return first_half + [array[pivot_index]] + second_half

if __name__ == "__main__":
    main()
