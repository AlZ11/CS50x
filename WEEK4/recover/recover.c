#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>
#define BLOCK_SIZE 512
#define FILE_NAME_SIZE 8
typedef uint8_t BYTE;
bool new_jpeg(BYTE buffer[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 1;
    }
    FILE* ptfile = fopen(argv[1], "r");
    if (ptfile == NULL)
    {
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    bool jpg_found = false;
    int file_idx = 0;
    FILE* out_file;
    while (fread(buffer, BLOCK_SIZE, 1, ptfile))
    {
        if (new_jpeg(buffer))
        {
            if (jpg_found == false)
            {
                jpg_found = true;
            }
            else
            {
                fclose(out_file);
            }
            char filename[FILE_NAME_SIZE];
            sprintf(filename, "%03i.jpg", file_idx++);
            out_file = fopen(filename, "w");
            if (out_file == NULL)
            {
                return 1;
            }
            fwrite(buffer, BLOCK_SIZE, 1, out_file);

    }
    else if (jpg_found == true)
    {
        fwrite(buffer, BLOCK_SIZE, 1, out_file);
    }
    }
    fclose(out_file);
    fclose(ptfile);
}

bool new_jpeg(BYTE buffer[])
    {
    return buffer[0] == 0xFF && buffer[1] == 0xd8 && buffer[2] == 0xFF && (buffer[3] & 0xF0) == 0xE0;
    }
