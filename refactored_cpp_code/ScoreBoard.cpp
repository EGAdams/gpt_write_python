#include "ScoreBoard.h"
#include "FontLoader.h"
#include "CanvasCreator.h"
#include "TextDrawer.h"

void ScoreBoard::update(GameState* gameState, RGBMatrix::Options matrix_options, rgb_matrix::RuntimeOptions runtime_opt)  { 
    printf( "Updating ScoreBoard...\n" ); 
    const char *bdf_font_file = "fonts/mspgothic_042623.bdf";
    rgb_matrix::Font font;
    FontLoader fontLoader(bdf_font_file);
    if (!fontLoader.LoadFont(font)) {
        exit(1);
    }
    bool with_outline = false;
    rgb_matrix::Font *outline_font = NULL;
    if (with_outline) {
        outline_font = font.CreateOutlineFont();
    }
    CanvasCreator canvasCreator(matrix_options, runtime_opt);
    RGBMatrix *canvas = canvasCreator.CreateCanvas();
    Color color(255, 255, 0);
    Color bg_color(0, 0, 0);
    Color flood_color(0, 0, 0);
    Color outline_color(0,0,0);
    const bool all_extreme_colors = (matrix_options.brightness == 100)
        && this->FullSaturation( color ) && this->FullSaturation( bg_color ) && this->FullSaturation( outline_color );
    if (all_extreme_colors) {
        canvas->SetPWMBits(1);
    }
    const int x = 0;
    int y = 0;

    canvas->Fill(flood_color.r, flood_color.g, flood_color.b);

    // Rest of the code...

    delete canvas;
}