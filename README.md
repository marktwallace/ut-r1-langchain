# A simple streamlit based UI for R1 with langchain

This is bases on https://github.com/krishnaik06/Gen-AI-With-Deep-Seek-R1/blob/main/app.py (YouTube: https://www.youtube.com/watch?v=zC6B490i-IY)

I fixed a couple of things and it now streams the output to the browser, which feels snappier.

## Building and running

### conda

You will need Conda. To install conda safely on a Mac:

`brew install conda`

And then probably:

`conda init zsh`

This makes it so conda does not override you system python, and it will affect python only when activated as venv:

`conda config --set auto_activate_base false`

To avoid weird conda stuff, only create virtual environments with the -p option, e.g.

`conda create -p venv python=3.10`

### The python project

Pull this repo with `git clone`

Create a venv in the project (it will be .gitignore'd).

```
cd ut-r1-langchain
conda create -p venv python=3.10
conda activate ./venv
pip install -r requirements.txt
```

Notice you HAVE to use `./venv` with the new conda!

A few months from now, based on Python package "drift" you may have to do this instead:

`pip install -r requirements_version.txt`

I did this as insurance in Feb '25: `pip freeze > requirements_version.txt`

### Running the streamlit

streamlit run app.py

The streamlit looks pretty good! It is just riffing on the now traditional OpenAI style web UI.

Next I should add some history.

(fib.py is just some code that R1 generated on my laptop with the 1.5B model.)
