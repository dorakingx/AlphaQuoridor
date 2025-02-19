# ====================
# Execution of Learning Cycle
# ====================

# Importing packages
from dual_network import dual_network
from self_play import self_play
from train_network import train_network
from evaluate_network import evaluate_network
from evaluate_best_player import evaluate_best_player

# Number of NUM_EPOCH
NUM_TRAIN_CYCLE = 3

# Main function
if __name__ == '__main__':
    # Creating the dual network
    dual_network()

    for i in range(NUM_TRAIN_CYCLE):
        print('Train', i, '====================')
        # self-play part
        self_play()

        # parameter update part
        train_network()

        # Evaluating new parameters
        update_best_player = evaluate_network()

        # Evaluating the best player
        if update_best_player:
            evaluate_best_player()
