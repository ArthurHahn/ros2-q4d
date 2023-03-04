# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_eng10026_publisher_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED eng10026_publisher_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(eng10026_publisher_FOUND FALSE)
  elseif(NOT eng10026_publisher_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(eng10026_publisher_FOUND FALSE)
  endif()
  return()
endif()
set(_eng10026_publisher_CONFIG_INCLUDED TRUE)

# output package information
if(NOT eng10026_publisher_FIND_QUIETLY)
  message(STATUS "Found eng10026_publisher: 2.1.0 (${eng10026_publisher_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'eng10026_publisher' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${eng10026_publisher_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(eng10026_publisher_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${eng10026_publisher_DIR}/${_extra}")
endforeach()
