#include "minesweeper.h"

// Main function to play Minesweeper
void minesweeper(string input, string output)
{
	char board[SIZE][SIZE];  // Game board initialized from file
	bool touchedBoard[SIZE][SIZE];  // Tracks touched cells on the board
	bool gameOver = false; // Indicateds whether the game has ended
	int findBlank = 0;  // Counter for the number of blank cless found (if findBlank==54, wins the game)
	
	// Opne input file to read commands and input file unitl the end of the file
	ifstream commandFile(input);  
	ofstream outFile(output); 
	while (!commandFile.eof()) {  
		string line;  // Stores a line of command from the input file
		getline(commandFile, line);  // Stores a line of command from the input line
		
		// If the command starts with LOAD
		if (line.find(LOAD) == 0) {  
			outFile << "Command: " << line << endl;  
			string boardFile = line.substr(LOAD.length(), line.length() - LOAD.length());  
			initBoard(board, boardFile); 
			initTouched(touchedBoard); 
		}

		// If the command starts with DISPLAY
		else if (line.find(DISPLAY) == 0) {  
			outFile << "Command: " << line << endl; 
			displayBoard(outFile, board, touchedBoard, gameOver);  
		}

		// If the command starts with TOUCH
		else if (line.find(TOUCH) == 0) { 
			outFile << "Command: " << line << endl; 
			
			// Extract x and y coordinates from the command
			line = line.substr(TOUCH.length());  
			int x = stoi(line.substr(0, line.find(" ")));  
			line = line.substr(line.find(" ") + 1);  
			int y = stoi(line);  

			// Touch (x,y) in board
			touchBoard(touchedBoard, x, y);  
			if ((x >= 1 && x <= SIZE) && (y >= 1 && y <= SIZE)) { 
				if (board[x - 1][y - 1] == '*') {  // If touched cell is bomb
					gameOver = true;  // End the game
					displayBoard(outFile, board, touchedBoard, gameOver);  // Display the final board
					break;  
				}
				else if (++findBlank == BLACK_COUNT) { // If all blank spaces are found
					gameOver = true;  // End the game
					displayBoard(outFile, board, touchedBoard, gameOver);  
					break;
				}
			}
		}
	}

	if (!gameOver) { 
		gameOver = true;  
		displayBoard(outFile, board, touchedBoard, gameOver);  
	}
}

// Function to initialize the game board from the given file
void initBoard(char board[][SIZE], string file) 
{
	ifstream inputFile(file); 
	for (int i = 0; i < SIZE; i++) {  
		for (int j = 0; j < SIZE; j++) {  
			inputFile >> board[i][j];  // Read char from inputFile and save it to board[i][j]
		}
	}
}

// Function to display the current state of the board
void displayBoard(ostream& out, char board[][SIZE], bool touchedBoard[][SIZE], bool gameOver)
{
	if (gameOver) { 
		out << "Game Over" << endl;
		out << "~~~~~~~~~" << endl;
		out << "Final Board" << endl;
	}
	int spaceTouched = 0;  // Counter for touched spaces
	for (int i = 0; i < SIZE; i++) {  
		for (int j = 0; j < SIZE; j++) {  
			if (!touchedBoard[i][j] && board[i][j] == '.') {  
				out << ".";  // . meas empty space
			}
			else if (!touchedBoard[i][j] && board[i][j] == '*') {  
				if (gameOver) {  
					out << "@";  // @ means hidden bomb
				}
				else {  
					out << ".";  
				}
			}
			else if (touchedBoard[i][j] && board[i][j] == '.') {  
				int bombCount = 0;  // Counter for neighboring bombs
				if ((i - 1 >= 0 && i - 1 < SIZE) && (j - 1 >= 0 && j - 1 < SIZE) && board[i - 1][j - 1] == '*') {  	bombCount++;  
				}
				if ((i - 1 >= 0 && i - 1 < SIZE) && (j >= 0 && j < SIZE) && board[i - 1][j] == '*') { 
					bombCount++;  
				}
				if ((i - 1 >= 0 && i - 1 < SIZE) && (j + 1 >= 0 && j + 1 < SIZE) && board[i - 1][j + 1] == '*') { 
					bombCount++;  
				}
				if ((i >= 0 && i < SIZE) && (j - 1 >= 0 && j - 1 < SIZE) && board[i][j - 1] == '*') {  
					bombCount++; 
				}
				if ((i >= 0 && i < SIZE) && (j + 1 >= 0 && j + 1 < SIZE) && board[i][j + 1] == '*') {  
					bombCount++;  
				}
				if ((i + 1 >= 0 && i + 1 < SIZE) && (j - 1 >= 0 && j - 1 < SIZE) && board[i + 1][j - 1] == '*') { 
					bombCount++;  
				}
				if ((i + 1 >= 0 && i + 1 < SIZE) && (j >= 0 && j < SIZE) && board[i + 1][j] == '*') {  
					bombCount++; 
				}
				if ((i + 1 >= 0 && i + 1 < SIZE) && (j + 1 >= 0 && j + 1 < SIZE) && board[i + 1][j + 1] == '*') { 
					bombCount++;  
				}
				spaceTouched++;  
				out << bombCount; 
			}
			else if (touchedBoard[i][j] && board[i][j] == '*') {  
				out << "*";  // * means revealed bomb
				spaceTouched++;  
			}
		}
		out << endl;  
	}
	out << endl;
	if (gameOver) { 
		out << "Spaces touched: " << spaceTouched << endl;  
	}
}

// Initialize touchBoard to all false
void initTouched(bool touchedBoard[][SIZE])  
{
	for (int i = 0; i < SIZE; i++) {  
		for (int j = 0; j < SIZE; j++) {  
			touchedBoard[i][j] = false;  // Set all cells to untouched
		}
	}
}

// Function to mark a cell as touched
void touchBoard(bool board[][SIZE], int x, int y)  
	if ((x >= 1 && x <= SIZE) && (y >= 1 && y <= SIZE)) {  
		board[x - 1][y - 1] = true; // Convert to 0-based index ans mark as touched
	}
}

int main() {
	cout << "Testing minesweeper" << endl;
	minesweeper(".\\test1commands.txt", "test1_output_mine.txt");
	minesweeper(".\\test2commands.txt", "test2_output_mine.txt");
	minesweeper(".\\test3commands.txt", "test3_output_mine.txt");
	minesweeper(".\\test4commands.txt", "test4_output_mine.txt");
	minesweeper(".\\test5commands.txt", "test5_output_mine.txt");
	minesweeper(".\\test6commands.txt", "test6_output_mine.txt");
	minesweeper(".\\test7commands.txt", "test7_output_mine.txt");
	minesweeper(".\\test8commands.txt", "test8_output_mine.txt");
	minesweeper(".\\test9commands.txt", "test9_output_mine.txt");
	minesweeper(".\\test10commands.txt", "test10_output_mine.txt");

	return 0;
}