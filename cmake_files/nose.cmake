# Adds function to create nose tests
function(add_nose_test SOURCE)
    get_filename_component(testname ${SOURCE} NAME_WE)
    if(LOCAL_PYTHON_EXECUTABLE)
        set(exec "${LOCAL_PYTHON_EXECUTABLE}")
    elseif(PYTHON_EXECUTABLE)
        set(exec "${PYTHON_EXECUTABLE}")
    else()
        message(FATAL_ERROR "Python executable not  set")
    endif()
    add_test( NAME ${testname}
        COMMAND ${exec} -c "import nose; nose.run()"
            ${CMAKE_CURRENT_SOURCE_DIR}/${SOURCE}
    )
    set_tests_properties(${testname} PROPERTIES LABELS "nose;python")
endfunction()