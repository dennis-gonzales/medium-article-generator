# About the project

Medium Article Generator Built with Langchain and LLM's (ChatGPT, GPT-4, etc)

## Activate

```bash
# use `conda info --envs` to list all your envs
conda activate /PATH_TO_PROJ/env
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

### Run Jupyter Notebook in VSCode

Open the Jupyter Notebook file and make sure that the correct [kernel](#selecting-the-correct-kernel) is selected.

### Run Streamlit (WebUI)

```bash
streamlit run app.py
```

## Deactivate

```bash
conda deactivate
```

## Commands Used for Setting up the Project

```bash
conda create --prefix ./env jupyter
pip install python-dotenv streamlit langchain openai wikipedia chromadb tiktoken
```

## Troubleshooting

### Selecting The Correct Kernel

Make sure you've selected the **correct environment** to run on.

e.g. `python <python-version> (conda) .\env\python.exe`

### Installing ChromaDB

If you received an error `ERROR: Could not build wheels for chroma-hnswlib, which is required to install pyproject.toml-based projects` check [HERE](https://github.com/chroma-core/chroma/issues/189#issuecomment-1454418844).
