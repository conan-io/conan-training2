cmake_minimum_required(VERSION 3.15)
project(mylib CXX)

add_library(mylib src/mylib.cpp)
target_include_directories(mylib PUBLIC include)

set_target_properties(mylib PROPERTIES PUBLIC_HEADER "include/mylib.h")
install(TARGETS mylib)
