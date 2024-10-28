from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.progress import BarColumn, Progress
from rich.padding import Padding

class DisplayHelpers:
    def __init__(self):
        self.console = Console()

    def display_main(self, tasks_summary, input_prompt=""):
        # Setting up the layout for display sections with added separation
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="spacer1", size=1),
            Layout(name="main", ratio=1),
            Layout(name="spacer2", size=1),
            Layout(name="footer", size=4),
        )

        # Header display
        header = Panel("📅 Today's Task Manager", style="bold white on blue")
        layout["header"].update(header)

        # Table for task details with updated colors for columns
        tasks_table = Table(title="Today's Tasks", expand=True, show_header=True, header_style="bold magenta")
        tasks_table.add_column("Task", justify="center", style="cyan")
        tasks_table.add_column("Target", justify="center", style="yellow")
        tasks_table.add_column("Progress", justify="center", style="green")
        tasks_table.add_column("Completion", justify="center", style="red")

        # Populating the table with tasks
        for task_name, details in tasks_summary.items():
            target = str(details["target"])
            progress_amount = str(details["progress"])
            status = "Completed" if details["progress"] >= details["target"] else "Incomplete"

            # Progress bar for the task
            progress_bar = Progress(
                "[progress.percentage]{task.percentage:>3.0f}%",
                BarColumn(bar_width=None),
            )
            task = progress_bar.add_task("", total=details["target"], completed=details["progress"])
            progress_renderable = progress_bar.render(task)

            tasks_table.add_row(task_name, target, progress_amount, status)

        # Main panel for tasks overview with padding for separation
        main_panel = Padding(Panel(tasks_table, title="Task Progress Overview", border_style="bright_blue", padding=(1, 2)), (1, 0))
        layout["main"].update(main_panel)

        # Footer message with more space between sections
        footer_message = "Instructions: Manage tasks (add, update, check, modify, remove, exit).\n" + input_prompt
        footer = Panel(
            footer_message,
            border_style="green",
            padding=(2, 2),
            style="bold white on black",
        )
        layout["footer"].update(footer)

        # Render the layout with added separation
        self.console.print(layout)

    def display_message(self, message, style="bold green"):
        self.console.print(message, style=style)


    
