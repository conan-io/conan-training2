cmake_minimum_required(VERSION 3.15)
project(hello CXX)

enable_testing()

add_library(hello src/hello.cpp)
target_include_directories(hello PUBLIC include)

set_target_properties(hello PROPERTIES PUBLIC_HEADER "include/hello.h")
install(TARGETS hello)

if (NOT BUILD_TESTING STREQUAL OFF)
    add_subdirectory(tests)
    add_test(NAME test_hello COMMAND test_hello)
endif()
