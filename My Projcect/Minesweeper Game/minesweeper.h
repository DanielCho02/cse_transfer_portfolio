#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cctype>
#include <cassert>

using std::endl;
using std::cout;
using std::ifstream;
using std::ofstream;
using std::setw;
using std::setfill;
using std::string;
using std::ostream;

const int SIZE = 8;
const int BLACK_COUNT = 54;
const string LOAD = "load ";
const string DISPLAY = "display";
const string TOUCH = "touch ";

void minesweeper(string input, string output);

void initBoard(char board[][SIZE], string file);
/******************************************************************************
 * This method will read the file that is loaded and store the locations of the
 * bombs as well as figure out the values for the numbers on the board.
 *
 * board[][] - this is the 2d array that is the board.
 * file - the name of the file that contains the locations of the bombs
 ******************************************************************************/

void displayBoard(ostream& out, char board[][SIZE], bool touchedBoard[][SIZE], bool gameOver = false);
/******************************************************************************
 * This function will read a board from the given file
 *
 * out - the ostream to display the board on.
 * board[][] - the board that is to be displayed
 * touchedBoard[][] - this is a board of bools that indicates if the game board
 * has been touched at a given spot.
 * gameOver - use this to indicate whether to reveal the hidden bombs
 ******************************************************************************/

void initTouched(bool touchedBoard[][SIZE]);
/******************************************************************************
 * This function will initialize a board to have a false value for every element
 *
 * touchedBoard[][] - this is a board of bools that indicates if the game board
 * has been touched at a given spot.
 ******************************************************************************/

void touchBoard(bool board[][SIZE], int x, int y);
/******************************************************************************
 * This will go to the given board and indicate that it's been touched at the
 * given location.
 * The board that is given is not the board with the bombs and numbers but
 * rather a bool board that indicates if the spots been touched or not and
 * it is needed for the displaying
 * board - this is the boolean touched board
 * x - this is the x coordinate in 1 based terms.  Must be checked for
 * validity and decremented.  If invalid nothing is touched
 * y - this is the y coordinate in 1 based terms.  Must be checked for
 * validity and decremented.  If invalid nothing is touched
 ******************************************************************************/