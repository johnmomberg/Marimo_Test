# /// script
# requires-python = ">=3.15"
# dependencies = [
#     "marimo>=0.23.3",
#     "matplotlib>=3.11.2",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo 
    import matplotlib.pyplot as plt 


    return mo, plt


@app.cell
def _(mo):
    slider = mo.ui.slider(
        start=0,
        stop=100,
        step=1,
        value=50,
        label="Select a value",
    )

    slider



    return (slider,)


@app.cell
def _(plt, slider):
    plt.figure(figsize=(5,5))
    plt.xlim((0, slider.value))
    plt.show() 
    return


if __name__ == "__main__":
    app.run()
