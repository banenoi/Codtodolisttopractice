import datetime
import json
import os

class DailyTasks:
    def __init__(self):
        self.tasks = {}
        self.data_file = 'tasks_data.json'
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = {}
        else:
            # Create the file if it doesn't exist
            with open(self.data_file, 'w', encoding='utf-8') as file:
                json.dump({}, file)

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, indent=4)

    def get_current_date(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def get_current_month(self):
        return datetime.datetime.now().strftime("%Y-%m")

    def add_task(self, task_name, task_percentage):
        today = self.get_current_date()

        if today not in self.tasks:
            self.tasks[today] = {
                'tasks': {},
                'completed': 0,
                'total_percentage': 0
            }

        self.tasks[today]['tasks'][task_name] = {
            'percentage': task_percentage,
            'completed': False
        }
        self.save_data()

    def complete_task(self, task_name):
        today = self.get_current_date()

        if today in self.tasks and task_name in self.tasks[today]['tasks']:
            if not self.tasks[today]['tasks'][task_name]['completed']:
                self.tasks[today]['tasks'][task_name]['completed'] = True
                self.tasks[today]['completed'] += 1
                self.tasks[today]['total_percentage'] += self.tasks[today]['tasks'][task_name]['percentage']
                self.save_data()
                return True
        return False

    def get_daily_progress(self):
        today = self.get_current_date()

        if today in self.tasks:
            total_tasks = len(self.tasks[today]['tasks'])
            completed_tasks = self.tasks[today]['completed']
            total_percentage = self.tasks[today]['total_percentage']

            return {
                'date': today,
                'total_tasks': total_tasks,
                'completed_tasks': completed_tasks,
                'total_percentage': total_percentage,
                'tasks': self.tasks[today]['tasks']
            }
        return None

    def get_monthly_progress(self):
        current_month = self.get_current_month()
        monthly_data = {
            'month': current_month,
            'days': 0,
            'total_percentage': 0,
            'daily_average': 0,
            'details': {}
        }

        for date in self.tasks:
            if date.startswith(current_month):
                daily = self.tasks[date]
                monthly_data['days'] += 1
                monthly_data['total_percentage'] += daily['total_percentage']
                monthly_data['details'][date] = {
                    'completed_tasks': daily['completed'],
                    'total_percentage': daily['total_percentage']
                }

        if monthly_data['days'] > 0:
            monthly_data['daily_average'] = monthly_data['total_percentage'] / monthly_data['days']

        return monthly_data

    def show_menu(self):
        while True:
            print("\n===== Daily Tasks Program =====")
            print("1. Add a New Task")
            print("2. Complete a Task")
            print("3. View Today's Progress")
            print("4. View Monthly Progress")
            print("5. Exit")

            choice = input("Select an option: ")

            if choice == '1':
                task_name = input("Enter the task name: ")
                try:
                    task_percentage = float(input("Enter the task percentage (e.g., 10 for 10%): "))
                    self.add_task(task_name, task_percentage)
                    print(f"Task '{task_name}' with {task_percentage}% added successfully.")
                except ValueError:
                    print("Error! Please enter a valid number for the percentage.")

            elif choice == '2':
                task_name = input("Enter the name of the completed task: ")
                if self.complete_task(task_name):
                    print(f"Task '{task_name}' marked as completed.")
                else:
                    print("Task not found or already completed.")

            elif choice == '3':
                progress = self.get_daily_progress()
                if progress:
                    print(f"\nProgress for {progress['date']}:")
                    print(f"- Total Tasks: {progress['total_tasks']}")
                    print(f"- Completed Tasks: {progress['completed_tasks']}")
                    print(f"- Total Percentage: {progress['total_percentage']}%")

                    print("\nTask Details:")
                    for task, details in progress['tasks'].items():
                        status = "Completed" if details['completed'] else "Incomplete"
                        print(f"- {task}: {details['percentage']}% ({status})")
                else:
                    print("No tasks recorded for today.")

            elif choice == '4':
                progress = self.get_monthly_progress()
                print(f"\nProgress for {progress['month']}:")
                print(f"- Recorded Days: {progress['days']}")
                print(f"- Total Percentage: {progress['total_percentage']}%")
                print(f"- Daily Average: {progress['daily_average']:.2f}%")

                print("\nDaily Details:")
                for date, details in progress['details'].items():
                    print(f"- {date}: {details['total_percentage']}% ({details['completed_tasks']} tasks completed)")

            elif choice == '5':
                print("Saving data and exiting...")
                self.save_data()
                break

            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = DailyTasks()
    app.show_menu()