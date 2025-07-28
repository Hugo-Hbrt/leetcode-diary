import json
from pathlib import Path
from typing import Dict
from models import Card, dict_to_card, card_to_dict

DATA_FILE = Path("training/training_data.json")

def load_data() -> Dict[str, Card]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file {DATA_FILE} does not exist. Please ensure the file is created before loading data.")

    with open(DATA_FILE, "r") as f:
        raw_data = json.load(f)

    return {
        key: dict_to_card(key, value)
        for key, value in raw_data.items()
    }

def save_data(cards: Dict[str, Card]) -> None:
    data_to_save = {
        key: card_to_dict(card)
        for key, card in cards.items()
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data_to_save, f, indent=4)
