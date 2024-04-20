Based on this [YouTube tutorial](https://www.youtube.com/watch?v=2TJxpyO3ei4)

Requires [Ollama](https://ollama.com/download/linux) installation:
```
curl -fsSL https://ollama.com/install.sh | sh
```

Pull a model (e.g. Mistral):
```
ollama pull mistral
```


### How to use
1. Add your documents to a directory "data"
2. Launch the LLM server: `ollama serve`

Note: if you are getting an error stating that the port is already busy, run: `export OLLAMA_HOST=localhost:8888`

3. Run `python3 populate_database.py`
4. Provide a question as an argument to the query script:
```
python3 query_data.py "What is the goal of the paper?"
```

### Unit testing
```
pytest
```