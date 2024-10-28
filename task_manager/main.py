
from progress_tracking import ProgressTracker
from display_helpers import DisplayHelpers

def main():
    progress_tracker = ProgressTracker()
    display_helpers = DisplayHelpers()

    # Initial display of today's tasks
    today_summary = progress_tracker.get_today_tasks_summary()
    display_helpers.display_main(today_summary, input_prompt="Add or update your tasks here.")

    # Interaction loop for managing tasks
    while True:
        display_helpers.display_message("\n[bold]Please enter a command (add, update, check, modify, remove, exit):[/bold]", style="yellow")
        
        user_input = input().strip().lower()

        if user_input == "exit":
            display_helpers.display_message("[bold green]Exiting the Task Manager. Goodbye![/bold green]")
            break
        elif user_input == "add":
            task_name = input("Enter the task name: ")
            target = float(input("Enter the target amount: "))
            recurring = input("Should the task be recurring? (yes/no): ").strip().lower() == "yes"
            progress_tracker.add_daily_task(task_name, target, recurring)
            display_helpers.display_message(f"[green]Task '{task_name}' added with target {target}.[/green]")
        elif user_input == "update":
            task_name = input("Enter the task name: ")
            progress = float(input("Enter the amount to add to the progress: "))
            if progress_tracker.update_daily_task_progress(task_name, progress):
                display_helpers.display_message(f"[green]Updated '{task_name}' with progress {progress}.[/green]")
            else:
                display_helpers.display_message(f"[red]Task '{task_name}' not found.[/red]")
        elif user_input == "check":
            task_name = input("Enter the task name: ")
            is_completed = progress_tracker.check_daily_task_completion(task_name)
            status = "Completed" if is_completed else "Incomplete"
            display_helpers.display_message(f"[blue]Task '{task_name}' is {status}.[/blue]")
        elif user_input == "modify":
            task_name = input("Enter the task name: ")
            target = input("Enter the new target amount (leave blank to keep unchanged): ")
            recurring = input("Should the task be recurring? (yes/no, leave blank to keep unchanged): ").strip().lower()
            target = float(target) if target else None
            recurring = recurring == "yes" if recurring else None
            if progress_tracker.modify_task(task_name, target_amount=target, recurring=recurring):
                display_helpers.display_message(f"[green]Task '{task_name}' modified successfully.[/green]")
            else:
                display_helpers.display_message(f"[red]Task '{task_name}' not found.[/red]")
        elif user_input == "remove":
            task_name = input("Enter the task name: ")
            if progress_tracker.remove_task(task_name):
                display_helpers.display_message(f"[green]Task '{task_name}' removed.[/green]")
            else:
                display_helpers.display_message(f"[red]Task '{task_name}' not found.[/red]")
        else:
            display_helpers.display_message("[red]Unknown command. Please try again.[/red]")

        # Refresh the task summary and update the display
        today_summary = progress_tracker.get_today_tasks_summary()
        display_helpers.display_main(today_summary, input_prompt="Add or update your tasks here.")

if __name__ == "__main__":
    main()
    