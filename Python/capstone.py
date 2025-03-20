# Project: Intelligent Study Planner

import heapq
from collections import defaultdict

# User Story 1: Task Prioritization 

class TaskManager:
    """
    Manages student tasks by organizing them based on deadlines and priority.
    """
    def __init__(self):
        self.tasks = []  # Min-heap for automatic priority sorting

    def add_task(self, task_name, days_left, priority):
        """
        Adds a task to the task manager with a given deadline and priority.
        
        Args:
            task_name (str): The name of the task.
            days_left (int): The deadline for the task (positive integer).
            priority (int): The priority level (1 to 5, with 5 being highest).
        
        Raises:
            ValueError: If input values are invalid.
        """
        try:
            if not task_name or not isinstance(task_name, str):
                raise ValueError("Task name must be a non-empty string.")
            if not isinstance(days_left, int) or days_left <= 0:
                raise ValueError("Days must be a positive integer.")
            if not isinstance(priority, int) or priority < 1 or priority > 5:
                raise ValueError("Priority must be an integer between 1 and 5.")
            heapq.heappush(self.tasks, (days_left, -priority, task_name))
        except ValueError as e:
            print(f"Error adding task: {e}")
    
    def get_schedule(self):
        return [f"{task[2]}, Days Left: {-task[1]}, Priority: {task[0]}" for task in sorted(self.tasks)]  # Sorted by deadline, priority

# User Story 2: Performance Tracking 

class PerformanceTracker:
    """
    Tracks student performance by storing scores and calculating averages.
    """
    def __init__(self):
        self.scores = defaultdict(list)

    def add_score(self, subject, score):
        """
        Adds a score for a given subject.
        
        Args:
            subject (str): The name of the subject.
            score (int or float): The score (0-100 range).
        
        Raises:
            ValueError: If input values are invalid.
        """
        try:
            if not subject or not isinstance(subject, str):
                raise ValueError("Subject must be a non-empty string.")
            if not isinstance(score, (int, float)) or score < 0 or score > 100:
                raise ValueError("Score must be a number between 0 and 100.")
            self.scores[subject].append(score)
        except ValueError as e:
            print(f"Error adding score: {e}")
    
    def get_average(self, subject):
        """
        Calculates the average score for a given subject.
        
        Args:
            subject (str): The name of the subject.
        
        Returns:
            float or None: The average score if available, otherwise None.
        
        Raises:
            ValueError: If there are no scores for the subject.
        """
        try:
            if subject not in self.scores or not self.scores[subject]:
                raise ValueError("No scores available for this subject.")
            s = sum(self.scores[subject]) / len(self.scores[subject])
            return f"{subject} Average: {s}"
        except ValueError as e:
            print(f"Error calculating average: {e}")
            return None

# Example usage
task_manager = TaskManager()
task_manager.add_task("Math Homework", 3, 5)
task_manager.add_task("Science Project", 5, 4)
task_manager.add_task("English Essay", 2, 3)
print("Task Schedule:") 
print("\n".join(task_manager.get_schedule()))
print()

performance_tracker = PerformanceTracker()
performance_tracker.add_score("Math", 85)
performance_tracker.add_score("Math", 65)
performance_tracker.add_score("Science", 90)
performance_tracker.add_score("Science", 70)
print(performance_tracker.get_average("Math"))
print(performance_tracker.get_average("Science"))