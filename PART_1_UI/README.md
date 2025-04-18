# PART 1 - Creating the app UI

## App skeleton

The Python Shiny app UI design process is highly similar to R. The basic app
skeleton looks like this:

```python
from shiny import App, ui, reactive, render

app_ui = ui.page_fluid(
)

def server(input, output, session):
    pass

app = App(app_ui, server)
```

_Note that the UI variable is called `app_ui` and not `ui` as this is an
imported Shiny object we need to access UI objects_

## What you can directly transfer from R Shiny

### Main layout elements

The following UI elements have a direct Python Shiny equivalent

| UI element       | R code            | Python Code             |
| ---------------- | ----------------- | ----------------------- |
| Fluid Page       | `fluidPage()`     | `ui.page_fluid()`       |
| Row              | `fluidRow()`      | `ui.row()`              |
| Column           | `column()`        | `ui.column()`           |
| Tabset           | `tabsetPanel()`   | `ui.navset_tab()`       |
| - tab panel      | `tabPanel()`      | `ui.nav_panel()`        |
| Side bar         | `sidebarLayout()` | `ui.layout_sidebar()`\* |
| - side bar panel | `sidebarPanel()`  | `ui.sidebar()`          |
| - main panel     | `mainPanel()`     | _not needed_            |

\* note that you can also use `ui.page_sidebar` if this is the main layout

_There are many more UI elements available, all under the `ui` object_

### Inputs

All default Shiny inputs in Python are organised under `ui.input_<name>`. The
names are identical to those used in R, only with the _input_ part first and
separated by underscores instead of using camel case.

| Input    | R code            | Python code                |
| -------- | ----------------- | -------------------------- |
| Slider   | `sliderInput()`   | `ui.input_slider()`        |
| Button   | `actionButton()`  | `ui.input_action_button()` |
| Number   | `numericInput()`  | `ui.input_numeric()`       |
| Text     | `textInput()`     | `ui.input_text()`          |
| Checkbox | `checkboxInput()` | `ui.input_checkbox()`      |
| ...      | ...               | ...                        |

The **arguments** inside the input functions are **identical to R** (e.g.
inputId, label, etc)

_NOTE: similar to R, every `ui.input_<element>` has a corresponding
`ui.update_<element>` function to dynamically update the input*

### Outputs

All outputs are organised under `ui.output_<name>`

| Output | R code          | Python Code         |
| ------ | --------------- | ------------------- |
| Text   | `textOutput()`  | `ui.output_text()`  |
| Table  | `tableOutput()` | `ui.output_table()` |
| Plot   | `plotOutput`    | `ui.output_plot()`  |
| UI     | `uiOutput()`    | `ui.output_ui()`    |

### HTML Tags

HTML tags allow you to insert any type of static UI available in HTML, examples
are headers, images, links, or custom divs

- In R shiny you can access HTML tags via `tags$<tag>` e.g. `tags$h1()`
- In Python they are all under `ui.<tag>` e.g. `ui.h1()`

### Sourcing local images

- In R shiny, all images need to reside in the `www` sub-folder of your app.
- In python, you need to define the subfolder which contains the static assets.
  Assuming you would also create a `www` folder you would designate it using

```python
from shiny import ui, App
from pathlib import Path

app_ui = ui.page_fluid(
  ui.tags.img(src = "image.png", alt = "An image")
)

def server(input, output, session):
  return

app = App(app_ui, server, static_assets=Path(__file__).parent / "www")
```

_Note that similarly to R, you do not put the static assets folder name in the
path name when sourcing in data_

## References

- [Layouts](https://shiny.posit.co/py/layouts/)
- [Inputs, outputs and other components](https://shiny.posit.co/py/components/)
