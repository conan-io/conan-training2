cmake_minimum_required(VERSION 3.15)
project(formatter CXX)

find_package(fmt REQUIRED)

message(NOTICE "==> Building with CMake version: ${CMAKE_VERSION} <== ")

add_executable(formatter src/main.cpp)
target_link_libraries(formatter fmt::fmt)
