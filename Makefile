

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-nlu"
	@echo "        Trains a new nlu model using the projects Rasa NLU config"
	@echo "    train-core"
	@echo "        Trains a new dialogue model using the story training data"
	@echo "    action"
	@echo "        Starts the server for custom action."
	@echo "    cmdline"
	@echo "       This will load the assistant in your terminal or host for you to chat."
	

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build
	
train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu-vi.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue -c policy.yml
	
action:
	python -m rasa_core_sdk.endpoint --actions actions
	
cmdline:
	python -m rasa_core.run -d models/dialogue -u models/current/nlu --port 5002 --connector slack --credentials slack_credentials.yml --endpoints endpoints.yml