class JSON_List(object):
    def __init__(self, tasks=[], orphan_tasks=[]):
        self.tasks = tasks
        self.orphan_tasks = orphan_tasks

    def find_task(self, find_id):
        task = self.find_task_helper(find_id, self.tasks)
        return task

    def find_task_helper(self, find_id, task_list):
        for task in task_list:
            if task.val.get("id") == find_id:
                return task
            else:
                if task.sub_tasks:
                    self.find_task_helper(find_id, task.sub_tasks)
        return None

    # Returns a sorted list of orphaned tasks who's parent_id matches par_id
    def find_orphan_tasks(self, par_id):
    
        # Get all tasks for parent
        orphans = [task for task in self.orphan_tasks if task.val["parent_id"] == par_id]

        # Sort based upon order
        if orphans:
            def get_order(task):
                return task.val.get("order")
            orphans.sort(key=get_order)

        return orphans

    # Assumes sorted list
    def insert_task(self, task):
        task = Task(task)
        if task.val.get("parent_id"):
            par_id = task.val["parent_id"]
            par_task = self.find_task(par_id)
            par_task.sub_tasks.append(task)
        else:
            self.tasks.append(task)

    # Can handle unsorted list
    def insert_task_unsort(self, task):
        task = Task(task)

        # Task has parent
        if task.val.get("parent_id"):
            par_id = task.val["parent_id"]
            par_task = self.find_task(par_id)

            # Parent task is found
            if par_task:
                par_task.sub_tasks.append(task)

            # Parent task not found yet
            else:
                self.orphan_tasks.append(task)

        # Task is a parent
        else:
            self.tasks.append(task)

            # Check if there are orphan tasks
            if self.orphan_tasks:
                orphans = self.find_orphan_tasks(task.val["id"])
                if orphans:
                    task.sub_tasks = task.sub_tasks + orphans

class Task(object):
    def __init__(self, task):
        self.val = task
        self.sub_tasks = []
