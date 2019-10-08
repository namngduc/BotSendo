import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.test import run_evaluation


def train_nlu(data_path, configs, model_path):
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, project_name='current', fixed_model_name='nlu')
    run_evaluation(data_path, model_directory)


def run_nlu(nlu_path):
    interpreter = Interpreter.load(nlu_path)
    pprint.pprint(interpreter.parse("Một số sản phẩm áo khoác "))
    pprint.pprint(interpreter.parse("Tìm các sảm phẩm điện thoại cho tôi"))
    pprint.pprint(interpreter.parse("Sản phẩm đồ chơi"))
    pprint.pprint(interpreter.parse("Tìm kiếm Id 20906002"))


if __name__ == '__main__':
    train_nlu('./data/nlu-vi.md', 'nlu_config.yml', './models')
    run_nlu('./models/current/nlu')
