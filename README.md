# Chess Game

This is a simple chess game implemented in Python using the Pygame library.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [AI Functionality](#ai-functionality)
- [Customization](#customization)
- [Contributing](#contributing)

## Introduction

This chess game provides a simple yet interactive way to play chess either against a friend or against an AI opponent. It features a graphical user interface built using Pygame, allowing users to make moves by clicking on the pieces and squares.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the Pygame library by running the following command:
   `pip install pygame`
3. Clone this repository to your local machine:
   `git clone https://github.com/EmanuelJrc/Chess-python.git`

## Usage

### Playing against a Friend

To play against a friend, run the `ChessNormal.py` file:
`python ChessNormal.py`

This will launch the game interface, allowing you to make moves by clicking on the pieces and squares.

### Playing against the AI

To play against the AI, run the `ChessAIMain.py` file:
`python ChessAIMain.py`

You can customize the AI's difficulty by adjusting the depth parameter in the `SmartMoveFinder.py` file.

## AI Functionality

The AI functionality is implemented in the `SmartMoveFinder.py` file. It uses a minimax algorithm with alpha-beta pruning to search for the best move based on a given depth level. The AI evaluates the board state using a combination of piece values, piece square tables, and other heuristics.

## Customization

You can customize various aspects of the game, including the AI's difficulty level and the graphical interface. Feel free to explore the codebase and make modifications according to your preferences.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.
