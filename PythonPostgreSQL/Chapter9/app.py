import matplotlib.pyplot as plt
import abc
import test
import databasebar

MENU_PROMPT = "Enter 'q' to quit or anything to chart a new poll."
POLL_PROMPT = "Select the poll id to create a pie chart of the vote percentages."


def prompt_select_poll(polls):
    for poll in polls:
        print(f"{poll[0]}: {poll[1]}")

    selected_poll = int(input(POLL_PROMPT))
    _chart_options_for_poll(selected_poll)


def _chart_options_for_poll(poll_id):
    options = test.get_options(poll_id)
    figure = abc.create_pie_chart(options)
    plt.show()


while (user_input := input(MENU_PROMPT)) != "q":
    polls = test.get_polls()
    prompt_select_poll(polls)