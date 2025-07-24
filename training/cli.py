import curses
from storage import load_data, save_data
from spaced_repetition_service import get_due_cards, mark_review

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    cards = load_data()
    due_cards = get_due_cards(cards)

    if not due_cards:
        stdscr.addstr(0, 0, "🎉 No cards due for review today!")
        stdscr.refresh()
        stdscr.getch()
        return

    current_selection = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "🧠 Cards due today (Use ↑ ↓ to navigate, Enter to select, q to quit):")
        
        # Add a guard condition to avoid index error with screen height
        max_height, max_width = stdscr.getmaxyx()

        for idx, card in enumerate(due_cards):
            if idx == current_selection:
                stdscr.attron(curses.A_REVERSE)
            
            if idx + 2 < max_height:  # Ensure we don't go out of bounds
                stdscr.addstr(idx + 2, 2, f"{card.title[:max_width - 2]}")
            else:
                stdscr.addstr(max_height - 1, 0, "More cards available, scroll to see them.")
                break
            if idx == current_selection:
                stdscr.attroff(curses.A_REVERSE)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_selection > 0:
            current_selection -= 1
        elif key == curses.KEY_DOWN and current_selection < len(due_cards) - 1:
            current_selection += 1
        elif key in (10, 13):  # Enter
            selected = due_cards[current_selection]
            review_card(stdscr, selected)
            result = prompt_success(stdscr, selected)
            
            if result is None:
                continue  # user chose to quit
            mark_review(selected, result)
            save_data(cards)
            due_cards = get_due_cards(cards)  # refresh list
            if not due_cards:
                stdscr.clear()
                stdscr.addstr(0, 0, "✅ All cards reviewed for today.")
                stdscr.refresh()
                stdscr.getch()
                break
            current_selection = min(current_selection, len(due_cards) - 1)
        elif key == ord('q'):
            break

def review_card(stdscr, card):
    stdscr.clear()
    stdscr.addstr(0, 0, f"📚 {card.title}")
    stdscr.addstr(2, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def prompt_success(stdscr, card):
    stdscr.clear()
    stdscr.addstr(0, 0, f"🤔 Did you recall \"{card.title}\" correctly?")
    stdscr.addstr(2, 0, "y = Yes | n = No | q = Abort")

    while True:
        key = stdscr.getch()
        if key in (ord('y'), ord('Y')):
            return True
        elif key in (ord('n'), ord('N')):
            return False
        elif key in (ord('q'), ord('Q')):
            return None  # exit gracefully

if __name__ == "__main__":
    curses.wrapper(main)
