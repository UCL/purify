if(Sopt_ARGUMENTS)
    cmake_parse_arguments(Sopt "" "GIT_REPOSITORY;GIT_TAG" "" 
        ${Sopt_ARGUMENTS})
endif()
if(NOT Sopt_GIT_REPOSITORY)
    set(Sopt_GIT_REPOSITORY https://github.com/UCL/sopt.git)
endif()
if(NOT Sopt_GIT_TAG)
    set(Sopt_GIT_TAG features/cmake)
endif()
ExternalProject_Add(
    Sopt
    PREFIX ${EXTERNAL_ROOT}
    GIT_REPOSITORY ${Sopt_GIT_REPOSITORY}
    GIT_TAG ${Sopt_GIT_TAG}
    CMAKE_ARGS
      -DBUILD_SHARED_LIBS=OFF
      -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
      -DCMAKE_C_FLAGS=${CMAKE_C_FLAGS}
      -DCMAKE_C_FLAGS_DEBUG=${CMAKE_C_FLAGS_DEBUG}
      -DCMAKE_C_FLAGS_RELWITHDEBINFO=${CMAKE_C_FLAGS_RELWITHDEBINFO}
      -DCMAKE_C_FLAGS_RELEASE=${CMAKE_C_FLAGS_RELEASE}
      -DCMAKE_C_FLAGS_MINSIZEREL=${CMAKE_C_FLAGS_MINSIZEREL}
      -DCMAKE_BUILD_TYPE=Release
      -DCMAKE_INSTALL_PREFIX=${EXTERNAL_ROOT}
      -DNOEXPORT=TRUE
    INSTALL_DIR ${EXTERNAL_ROOT}
    LOG_DOWNLOAD ON
    LOG_CONFIGURE ON
    LOG_BUILD ON
)
add_recursive_cmake_step(Sopt Sopt_FOUND DEPENDEES install)
ExternalProject_Get_Property(Sopt install_dir)
# unset(Sopt_INCLUDE_DIRS CACHE)
# set(Sopt_INCLUDE_DIRS ${install_dir}/include
#     CACHE PATH "Path to external project include")
set(Sopt_INCLUDE_DIRS Dummy)
set(Sopt_LIBRARIES dummy)