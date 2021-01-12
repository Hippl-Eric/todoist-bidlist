from sfcbidlist import bid_list

# Simple print to terminal
def simple_print():
    sfc_bids = bid_list()
    for task in sfc_bids:
        print(f"{task['order']}: id={task['id']}, par_id={task.get('parent_id')}, {task['content']}")

# Return HTML ordered list with subtasks as un-ordered list
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
    return output

if __name__ == "__main__":
    simple_print()
