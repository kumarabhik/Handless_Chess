# Handless-Chess
# Chess Game with Pygame
This project is a graphical chess game developed using Python and Pygame. It includes functionalities such as piece movement, castling, pawn promotion, and capturing. The game can be played between two players on the same machine.

## Table of Contents
## Requirements
Installation
Running the Game
Game Features
Game Controls
Code Overview
TODO
Requirements
Python 3.x
Pygame library
## Installation
Clone the repository from your preferred source.
Install the Pygame library using pip.
Running the Game
To run the game, navigate to the project directory and execute the main script.

## Game Features
Piece Movement: Pieces move according to standard chess rules.
Castling: Special move involving the king and a rook.
Pawn Promotion: Promote a pawn to another piece when it reaches the last rank.
Capturing: Capture opponent's pieces.
Check and Checkmate Detection: The game highlights the king in check and detects game over conditions.
## Game Controls
Use mouse clicks to select and move pieces.
Click the "FORFEIT" text to forfeit the game.
Press the ENTER key to restart the game after it is over.
# Code Overview
## Main Functions
draw_board(): Draws the chessboard and additional UI elements like the status text and grid lines.
draw_pieces(): Renders the chess pieces on the board based on their positions.
check_options(pieces, locations, turn): Calculates all possible moves for each piece of the given color.
check_king(position, color): Determines the valid moves for the king, including castling options.
check_queen(position, color): Determines the valid moves for the queen by combining bishop and rook moves.
check_bishop(position, color): Determines the valid moves for the bishop.
check_rook(position, color): Determines the valid moves for the rook.
check_knight(position, color): Determines the valid moves for the knight.
check_pawn(position, color): Determines the valid moves for the pawn.
check_valid_moves(): Returns the valid moves for the currently selected piece.
draw_valid(moves): Draws the valid moves for the selected piece on the board.
draw_captured(): Displays the captured pieces.
draw_check(): Highlights the king if it is in check.
draw_game_over(): Displays the game over screen.
check_ep(old_coords, new_coords): Checks for en passant conditions for pawns.
check_castling(): Determines the castling moves available for the king.
draw_castling(moves): Draws the castling move options on the board.
check_promotion(): Checks if a pawn can be promoted.
draw_promotion(): Displays the promotion options for a pawn.
check_promo_select(): Handles the selection of a piece for pawn promotion.
## TODO
Improve the user interface and graphics.
Add AI for single-player mode.
Implement a timer for each player's moves.
Add sounds for moves and captures.
Improve check and checkmate detection logic.
Feel free to contribute to this project by submitting issues or pull requests. Enjoy playing the game!







