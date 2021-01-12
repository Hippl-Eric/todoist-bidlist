import pathlib
import webbrowser
from sfcbidlist import bid_list, tasksJSON
from print_bid_list import printHTML

def main():
    
    # Get list of tasks and format into HTML ordered list
    tasks = bid_list()
    json_list = tasksJSON(tasks)
    html_input = printHTML(json_list.tasks)
    
    # Write input to HTML file and launch in default webbrowser
    with open("bids.html", "w") as html_file:
        html_file.write(html_input)
        url = str(pathlib.Path(__file__).parent.absolute())
        url += f"\{html_file.name}"
        webbrowser.open(url, new=2)

if __name__ == "__main__":
    main()
