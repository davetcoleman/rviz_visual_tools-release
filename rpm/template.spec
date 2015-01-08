Name:           ros-indigo-rviz-visual-tools
Version:        1.5.0
Release:        0%{?dist}
Summary:        ROS rviz_visual_tools package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/davetcoleman/rviz_visual_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-graph-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-graph-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
Helper functions for displaying and debugging data in Rviz via published markers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jan 07 2015 Dave Coleman <davetcoleman@gmail.com> - 1.5.0-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Dave Coleman <davetcoleman@gmail.com> - 1.4.0-0
- Autogenerated by Bloom

* Mon Oct 27 2014 Dave Coleman <davetcoleman@gmail.com> - 1.3.1-0
- Autogenerated by Bloom

