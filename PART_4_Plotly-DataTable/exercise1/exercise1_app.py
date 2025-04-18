# PART 4 - Exercise 1
# ///////////////////

from shiny import App, ui, reactive, render, req
import pandas as pd
from datetime import datetime

app_ui = ui.page_fluid(
    ui.card(
        ui.card_header("Create Task"),
        ui.input_text("task", "Description", width="auto"),
        ui.input_action_button("add", "Add task", width="150px"),
    ),
    ui.card(
        ui.card_header("ToDo list"),
        ui.input_action_button(
            "completed", "Mark selected task as complete", width="300px"
        ),
    ),
)


def server(input, output, session):
    #  Start with empty data frame
    todos = reactive.value(pd.DataFrame())

    # Add a new todo
    @reactive.effect
    @reactive.event(input.add)
    def _():
        req(input.task().strip())
        newTask = pd.DataFrame(
            {
                "created": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "task": [input.task()],
                "completed": [None],
            }
        )
        todos.set(pd.concat([todos(), newTask], ignore_index=True))
        ui.update_text("task", value="")


app = App(app_ui, server)
