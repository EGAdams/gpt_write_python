#pragma once

#include "Player.h"
#include "Color.h"
#include <led-matrix.h>

class ScoreBoard {
public:
    ScoreBoard(Player* player1, Player* player2);
    ~ScoreBoard();

    bool FullSaturation(const Color &c);
    void update(rgb_matrix::RGBMatrix::Options matrix_options, rgb_matrix::RuntimeOptions runtime_opt);

private:
    Player* _player1;
    Player* _player2;
};