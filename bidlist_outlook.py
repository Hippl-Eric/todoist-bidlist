import win32com.client as client
from sfcbidlist import bid_list, tasksJSON
from print_bid_list import printHTML

# MS Outlook
# https://www.youtube.com/watch?v=ZvmFHwAjXHI&feature=youtu.be

def main():
    
    # Get HTML formatted tasks for email body
    tasks = bid_list()
    json_list = tasksJSON(tasks)
    html_body = printHTML(json_list.tasks)
    
    # Launch outlook email
    outlook = client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.Display()
    message.Subject = "Upcoming Bids - "
    message.HTMLBody = html_body

if __name__ == "__main__":
    main()