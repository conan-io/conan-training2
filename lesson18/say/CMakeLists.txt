cmake_minimum_required(VERSION 3.15)
project(say CXX)

add_executable(say src/say.cpp)

find_package(hello REQUIRED CONFIG)
target_link_libraries(say hello::hello)

install(TARGETS say)
