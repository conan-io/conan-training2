#include <iostream>
#include "hello.h"
#include <fmt/color.h>

void hello() {
    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, 
                "hello/1.0: Hello World! (with color!)\n");
}
