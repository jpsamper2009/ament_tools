# Copyright 2015 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_package import package_exists_at
from ament_package import PACKAGE_MANIFEST_FILENAME
from ament_package import parse_package

__all__ = ('entry_point_data')

# meta information of the entry point
entry_point_data = dict(
    name='ament',
    description="A package containing a '%s' manifest file." % PACKAGE_MANIFEST_FILENAME,
    package_exists_at=package_exists_at,
    parse_package=lambda path:
      parse_package(path, package_name_warning_not_error=True),
    depends=[],
)
