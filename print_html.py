import pathlib
import webbrowser
from sfcbidlist import bid_list, tasksJSON

def main():
    sorted_list = bid_list()
    json_list = tasksJSON(sorted_list)
    printHTML(json_list.tasks)

def printHTML(tasks):
    output = "<div>Upcoming Bids:<br><ol>"

    for task in tasks:
        output += "<li>"
        output += task.val["content"]
        if task.sub_tasks:
            output += "<ul>"
            for sub_task in task.sub_tasks:
                output += f"<li>{sub_task.val['content']}</li>"
            output += "</ul>"
        output += "</li>"

    output += "</ol></div>"

    with open("bids.html", "w") as html_file:
        html_file.write(output)
        url = str(pathlib.Path(__file__).parent.absolute())
        url += f"\{html_file.name}"
        webbrowser.open(url, new=2)

if __name__ == "__main__":
    main()
