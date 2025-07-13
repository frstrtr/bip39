cmake_minimum_required(VERSION 3.10)
project(tron_xpub_demo)

set(CMAKE_CXX_STANDARD 17)

find_package(CryptoPP REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(LIBBITCOIN_SYSTEM libbitcoin-system)

include_directories(${CRYPTOPP_INCLUDE_DIRS} ${LIBBITCOIN_SYSTEM_INCLUDE_DIRS})

add_executable(tron_xPUB tron_xPUB.cpp)
target_link_libraries(tron_xPUB ${CRYPTOPP_LIBRARIES} ${LIBBITCOIN_SYSTEM_LIBRARIES})