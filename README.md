# About the project

Medium Article Generator Built with Langchain and LLM's (ChatGPT, GPT-4, etc)

## Getting Started

```bash
conda create --prefix ./env jupyter
```

```bash
pip install -r requirements.txt
```

### Commands Used for Setting up the Project

```bash
pip install python-dotenv streamlit langchain openai wikipedia chromadb tiktoken pipreqs
```

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

## Troubleshooting

### Selecting The Correct Kernel

Make sure you've selected the **correct environment** to run on.

e.g. `python <python-version> (conda) .\env\python.exe`

### Installing ChromaDB

If you received an error `ERROR: Could not build wheels for chroma-hnswlib, which is required to install pyproject.toml-based projects` check [HERE](https://github.com/chroma-core/chroma/issues/189#issuecomment-1454418844).

## Extra

### Agents

```bash
python agent.py
# When did the titanic sank? how many years has it been since then? how many people who survived? multiply these two values together.
```
