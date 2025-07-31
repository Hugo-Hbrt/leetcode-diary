from datetime import date, timedelta
from typing import Dict, List
from models import Card

MAX_REVIEW_INTERVAL = 60

def sort_by_oldest_next_review_date(cards: List[Card]):
    cards.sort(key=lambda x: x.next_review)

def get_due_cards(cards: Dict[str, Card]) -> List[Card]:
    today = date.today()
    cards_list = [card for card in cards.values() if card.next_review <= today]
    sort_by_oldest_next_review_date(cards_list)
    return cards_list

def refresh_due_cards(due_cards: List[Card], reviewed_card: Card) -> List[Card]:    
    if reviewed_card.next_review <= date.today():
        return due_cards  # No change needed
    
    return [card for card in due_cards if card != reviewed_card]
    
def mark_review(card: Card, success: bool) -> None:
    today = date.today()
    card.last_reviewed = today

    if success:
        card.success_streak += 1
        card.interval = min(card.interval * 2, MAX_REVIEW_INTERVAL) if card.interval > 0 else 1
    else:
        card.success_streak = 0
        card.interval = 1

    card.next_review = today + timedelta(days=card.interval)
