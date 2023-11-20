# Connect 4

#### Video Demo:  https://youtu.be/kkN-I-TNANs

#### Description:
Connect 4 is a two player game where players take turns dropping their counter into one of 7 columns. The game board consists of 6 rows and 7 columns, and the aim of the game is to line 4 of your pieces up either vertically, horizontally or diagonally before your opponent.

History:
The strategic depth of Connect 4 lies in the players' attempts to create a winning combination while simultaneously blocking their opponent's progress. As the game progresses, the board fills up, and players must carefully consider each move to both advance their own position and hinder their adversary's chances of victory.

Connect 4 is not only a game of skill but also one of anticipation and prediction. Players must foresee potential combinations and counteract their opponent's strategies. The game encourages critical thinking, spatial awareness, and pattern recognition.

The simplicity of the rules makes Connect 4 accessible to players of all ages, yet the strategic complexity ensures that it remains engaging for seasoned players. Its quick setup and relatively short playing time make it an ideal choice for a casual game night or a quick brain-teasing session.

Connect 4 has transcended its original physical board game form and found a digital presence, with online versions and apps allowing players to enjoy the game across distances. Its enduring popularity attests to the timeless appeal of its straightforward yet challenging gameplay, making it a classic in the world of abstract strategy games.

#### Implementation:

This is a simple connect 4 game with 2 games modes run completely in the command line that is built using vanilla python.

This project was built with the implementation of several functions that contributed to the overall game.

validate_input - Repeatedly prompts the user for input until they enter an input within a set of valid options.

create_board - Generates a list of lists to represent the game board for Connect4.

print_board - Prints a visual representation of the game board to console.

drop_piece - Simulates a player dropping their piece into a column of the game board.

execute_player_turn - Prompts the user for a legal move given the game board.

end_of_game - Checks the current state of the game board to see whether the game has ended or not.

local_2_player_game - Runs a regular game of Connect4 against local user

cpu_player_easy - Represents the computer player using a simple strategy to play its turn during a game

cpu_player_medium - Represents the computer player using a slightly more advanced strategy to play its turn during a game.

cpu_player_hard - Represents the computer player using an even more advanced strategy.

game_against_cpu - Runs a regular game of Connect4 against the CPU.


There is 2 possible game modes: CPU and PVP 2 player
IN CPU MODE: You can choose to play against the CPU in difficulty: easy, medium or hard
Easy mode: CPU plays random moves
Medium: CPU will block next move if win for opponent is possible and will play move if win is possible for CPU
Hard: Implemented so that the CPU will consistently achieve >= 90% win rate against CPU medium

IN PVP mode: You can play a local 2 player game against another user, where each player will take turns in placing pieces onto the board.

This was my CS50X!

