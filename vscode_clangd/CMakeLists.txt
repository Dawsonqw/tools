# 版本
cmake_minimum_required(VERSION 3.20)
# 工程名
project(vscode_clangd)

# 设置C++标准
set(CMAKE_CXX_STANDARD 17)

# 设置编译器
set(CMAKE_CXX_COMPILER g++)
set(CMAKE_C_COMPILER gcc)

# 设置编译选项
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -g")

# Debug模式
set(CMAKE_BUILD_TYPE "Debug")

# 头文件路径 {SOURCE_PREFIX}/include
include_directories(include)

# 源文件路径 {SOURCE_PREFIX}/src
file(GLOB SOURCE_FILES src/*.cpp)

# 生成编译命令
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# 生成静态库
add_library(${PROJECT_NAME} STATIC ${SOURCE_FILES})
# 动态库
# add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})

# 安装路径
install(TARGETS ${PROJECT_NAME} DESTINATION lib)
install(DIRECTORY include/ DESTINATION include)

# 可执行文件
add_executable(${PROJECT_NAME}_test test/main.cpp)
target_link_libraries(${PROJECT_NAME}_test ${PROJECT_NAME})

