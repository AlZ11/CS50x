#include "helpers.h"
#include <math.h>

#define min(a, b) ((a < b) ? (a) : (b))

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            float red = pixel.rgbtRed;
            float blue = pixel.rgbtBlue;
            float green = pixel.rgbtGreen;
            int average = round((red + green + blue) / 3);
            image[i][j].rgbtBlue = image[i][j].rgbtRed = image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            int originalRed = pixel.rgbtRed;
            int originalBlue = pixel.rgbtBlue;
            int originalGreen = pixel.rgbtGreen;

            image[i][j].rgbtRed = min(round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue), 0xFF);
            image[i][j].rgbtGreen = min(round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue), 0xFF);
            image[i][j].rgbtBlue = min(round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue), 0xFF);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int left = 0;
        int right = width - 1;
        while (left < right)
        {
            RGBTRIPLE tmp = image[i][left];
            image[i][left] = image[i][right];
            image[i][right] = tmp;

            left++;
            right--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            tmp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int total_red, total_blue, total_green;
            total_red = total_blue = total_green = 0;
            float count = 0.0;
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int curX = i + x;
                    int curY = j + y;

                    if (curX < 0 || curX > (height - 1) || curY < 0 || curY > (width - 1))
                    {
                        continue;
                    }
                    total_red += image[curX][curY].rgbtRed;
                    total_green += image[curX][curY].rgbtGreen;
                    total_blue += image[curX][curY].rgbtBlue;

                    count++;
                }
                tmp[i][j].rgbtRed = round(total_red / count);
                tmp[i][j].rgbtBlue = round(total_blue / count);
                tmp[i][j].rgbtGreen = round(total_green / count);
            }
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tmp[i][j].rgbtRed;
            image[i][j].rgbtBlue = tmp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = tmp[i][j].rgbtGreen;
        }
    }
    return;
}
