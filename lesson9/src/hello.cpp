#include <iostream>
#include "hello.h"
#include <fmt/color.h>

void hello(){
    #ifdef NDEBUG
    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, "hello/1.0: Hello World Release!\n");
    #else
    fmt::print(fg(fmt::color::crimson) | fmt::emphasis::bold, "hello/1.0: Hello World Debug!\n");
    #endif

    // ARCHITECTURES
    #ifdef _M_X64
    fmt::print(fg(fmt::color::medium_orchid), "  hello/1.0: _M_X64 defined\n");
    #endif

    #ifdef _M_IX86
    fmt::print(fg(fmt::color::medium_orchid), "  hello/1.0: _M_IX86 defined\n");
    #endif

    #if __i386__
    fmt::print(fg(fmt::color::medium_orchid), "  hello/1.0: __i386__ defined\n");
    #endif

    #if __x86_64__
    fmt::print(fg(fmt::color::medium_orchid), "  hello/1.0: __x86_64__ defined\n");
    #endif

    // Libstdc++
    #if defined _GLIBCXX_USE_CXX11_ABI
    fmt::print(fg(fmt::color::crimson), "  hello/1.0: _GLIBCXX_USE_CXX11_ABI {}\n", _GLIBCXX_USE_CXX11_ABI);
    #endif

    // COMPILER VERSIONS
    #if _MSC_VER
    fmt::print(fg(fmt::color::papaya_whip), "  hello/1.0: _MSC_VER {}\n", _MSC_VER);
    #endif

    #if _MSVC_LANG
    fmt::print(fg(fmt::color::papaya_whip), "  hello/1.0: _MSVC_LANG {}\n", _MSVC_LANG);
    #endif

    #if __cplusplus
    fmt::print(fg(fmt::color::papaya_whip), "  hello/1.0: __cplusplus {}\n", __cplusplus);
    #endif

    #if __INTEL_COMPILER
    fmt::print(fg(fmt::color::papaya_whip), "  hello/1.0: __INTEL_COMPILER {}\n", __INTEL_COMPILER);
    #endif

    #if __GNUC__
    fmt::print(fg(fmt::color::violet), "  hello/1.0: __GNUC__ {}\n", __GNUC__);
    #endif

    #if __GNUC_MINOR__
    fmt::print(fg(fmt::color::papaya_whip), "  hello/1.0: __GNUC_MINOR__ {}\n", __GNUC_MINOR__);
    #endif

    #if __clang_major__
    fmt::print(fg(fmt::color::yellow_green), "  hello/1.0: __clang_major__ {}\n", __clang_major__);
    #endif

    #if __clang_minor__
    fmt::print(fg(fmt::color::thistle), "  hello/1.0: __clang_minor__ {}\n", __clang_minor__);
    #endif

    #if __apple_build_version__
    fmt::print(fg(fmt::color::sandy_brown), "  hello/1.0: __apple_build_version__ {}\n", __apple_build_version__);
    #endif

    // SUBSYSTEMS

    #if __MSYS__
    fmt::print(fg(fmt::color::spring_green), "  hello/1.0: __MSYS__ {}\n", __MSYS__);
    #endif

    #if __MINGW32__
    fmt::print(fg(fmt::color::spring_green), "  hello/1.0: __MINGW32__ {}\n", __MINGW32__);
    #endif

    #if __MINGW64__
    fmt::print(fg(fmt::color::spring_green), "  hello/1.0: __MINGW64__ {}\n", __MINGW64__);
    #endif

    #if __CYGWIN__
    fmt::print(fg(fmt::color::spring_green), "  hello/1.0: __CYGWIN__ {}\n", __CYGWIN__);
    #endif
}