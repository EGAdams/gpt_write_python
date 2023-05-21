#include "ScoreBoard.h"
#include "FontLoader.h"
#include "CanvasCreator.h"
#include "TextDrawer.h"

int main() {
    printf("Updating ScoreBoard...\n");

    RGBMatrix::Options matrix_options;
    rgb_matrix::RuntimeOptions runtime_opt;

    // Create Canvas
    CanvasCreator canvasCreator(matrix_options, runtime_opt);
    RGBMatrix* canvas = canvasCreator.CreateCanvas();

    // Load Fonts
    FontLoader fontLoader("fonts/mspgothic_042623.bdf");
    rgb_matrix::Font font;
    fontLoader.LoadFont(font);

    FontLoader bigNumberFontLoader("fonts/fgm_27_ee.bdf");
    rgb_matrix::Font bigNumberFont;
    bigNumberFontLoader.LoadFont(bigNumberFont);

    FontLoader littleNumberFontLoader("fonts/little_numbers.bdf");
    rgb_matrix::Font littleNumberFont;
    littleNumberFontLoader.LoadFont(littleNumberFont);

    // Draw Text
    Color color(255, 255, 0);
    Color bg_color(0, 0, 0);
    TextDrawer textDrawer(canvas, font, 0, 0, color, bg_color, "I", 0);
    textDrawer.DrawText();

    // Drawing the rest of the text
    TextDrawer bigNumberDrawer1(canvas, bigNumberFont, 16, bigNumberFont.baseline() - 1, color, bg_color, "8", 1);
    bigNumberDrawer1.DrawText();

    TextDrawer bigNumberDrawer2(canvas, bigNumberFont, 38, bigNumberFont.baseline() - 1, color, bg_color, "9", 1);
    bigNumberDrawer2.DrawText();

    TextDrawer littleNumberDrawer(canvas, littleNumberFont, 7, littleNumberFont.baseline(), color, bg_color, "1 2 3", 0);
    littleNumberDrawer.DrawText();

    delete canvas;

    return 0;
}