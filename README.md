
![todo_app](https://github.com/yashpatel1598/todo_app/assets/87722800/0a6485d6-968b-4d16-8cf2-1a6708b6877e)
![todo_register](https://github.com/yashpatel1598/todo_app/assets/87722800/3de09b37-27a9-46de-b335-a97ed633e43d)
![todo_login](https://github.com/yashpatel1598/todo_app/assets/87722800/53041667-79d4-4c18-beac-4d15b790d992)


This Django Todo list is project is a simple web application that allows user to register create , view , update and delete thier to-do task.
it's built using Django web Framwork and as a Froented used Html/Css/Javascript.

Features : 
User Authentication : Users can sign up , log in and logout securely.
Create Task : Users can add new task with in there to-do list.
View tasks: Users can see a list of all their tasks on the dashboard.
Update tasks: Users can edit task details such as title and description.
Delete tasks: Users can remove tasks from their list when they are completed or no longer needed.
Mark tasks as completed: Users can mark tasks as completed to keep track of their progress.

Installation
Clone the repository:
git clone https://github.com/your_username/todo-list.git

Navigate to the project directory:
cd todo-list

Install the required dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser account:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the application at http://localhost:8000/ in your web browser.

Usage
Register a new account or log in with your existing credentials.
Once logged in, you'll be directed to the dashboard where you can:
Create a new task by clicking on the "Add Task" button.
View your existing tasks with options to edit or delete them.
Mark tasks as completed by checking the checkbox next to each task.
Log out when you're done by clicking on the "Log Out" link in the navigation bar.

Learning : 
1st : The task we have with same name can not be added again (it creates issue at time of update)
2nd : Once task is added and then after update the task for that task mark as a completed same issue
3rd : After update or edit the task in to-do list referesh the page (Froented-side it can be challenge)
                             **once we start learning all will be easy** 

Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.
