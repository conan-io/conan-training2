cmake_minimum_required(VERSION 3.15)
project(formatter CXX)

find_package(fmt REQUIRED)

# FIXME: this is here just to showcase 
# the use of the VirtualRunEnv
set(CMAKE_SKIP_RPATH TRUE)

add_executable(formatter src/main.cpp)
target_link_libraries(formatter fmt::fmt)
