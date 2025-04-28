# AlphaQuoridor

AlphaQuoridor is a project that combines game design with deep learning and Monte Carlo Tree Search (MCTS) to create an AI-driven board game experience. The system supports self-play for data collection, network training, parameter evaluation, and includes a user interface for human players to challenge the AI.

## Key Components

- **game.py:** Implements the game design and core rules.
- **dual_network.py:** Provides a deep learning implementation using a ResNet architecture.
- **pv_mcts.py:** Implements Monte Carlo Tree Search (MCTS) for decision making.
- **self_play.py:** Collects game data through self-play.
- **train_network.py:** Updates the parameters of the ResNet based on the training data.
- **evaluate_network.py:** Compares and updates the best network parameters.
- **evaluate_best_player.py:** Evaluates the performance of the best AI player.
- **train_cycle.py:** Runs the entire training cycle end-to-end.
- **human_play.py:** Implements a game UI for playing against the AI.

## Getting Started

### Requirements

- Python 3.x
- Libraries specified in `requirements.txt` (e.g., TensorFlow or PyTorch, NumPy, etc.)

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/dorakingx/AlphaQuoridor.git
cd AlphaQuoridor
pip install -r requirements.txt
```

### Usage

#### Training the AI

To run the complete training cycle, execute:

```bash
python train_cycle.py
```
This script will handle data collection through self-play, update the network parameters, and evaluate model improvements.

#### Playing Against the AI
To play a game against the trained AI, run:

```
python human_play.py
```
This launches the game UI, allowing you to challenge the AI directly.

### References
English -> https://doraking.medium.com/theory-and-implementation-of-alphaquoridor-cb9192f139a8 \\
Japanese -> https://note.com/dorakingx/n/n09cd88da9029
