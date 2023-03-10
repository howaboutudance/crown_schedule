from enum import Enum
import faker
from typing import List, Dict, Any
Faker = faker.Faker()

class BuildingType(Enum):
  Single_Tenant = 1
  Multi_Tenant = 2
  Commercial = 3

class EmployeeType(Enum):
    Certified_Installer = 1
    Installer_Pending_Certification = 2
    Laborer = 3


# Did not get a complete implementations
# looking to the work, I should have spent more time on requirements, I started witth odd assumption
# that the schedule should be by day and building
#
# for instance, each day of the week would be given a day of the week
# inside that would be a list of buildings and each building would have the assigned employee
#
# I got stuck on the implemtation of `schedule_day`
# I would assume I would build a function to assign buildings visited in a single day and then expand
# into the week for `schedule()`

# limitations of the current implementation:
# - only assumes Monday-Friday work week with no dates
def schedule(buildings: List[Dict], employees: List[Dict]) -> List[Dict]:
    """Schedule employees to buildings.

    Args:
        buildings (dict): A dictionary of buildings to be scheduled.
        employees (dict): A dictionary of employees to be scheduled.

    Returns:
        dict: A dictionary of employees scheduled to buildings.
    """
    # Schedule Schema
    # [{ day: 0, building: "building_name", employees: ["employee_name", "employee_name"] }]
    schedule_list = []
    return schedule_list

def generate_require_employees(building: Dict) -> List:
    """Generate a list of employees required for a building.

    Args:
        building (dict): A dictionary of a building.

    Returns:
        list: A list of employees required for a building.
    """
    if building["type"] == BuildingType.Single_Tenant:
        return [EmployeeType.Certified_Installer]
    elif building["type"] == BuildingType.Multi_Tenant:
        return [EmployeeType.Certified_Installer] + [[EmployeeType.Installer_Pending_Certification, EmployeeType.Laborer]]
    elif building["type"] == BuildingType.Commercial:
        return [[EmployeeType.Certified_Installer]]* 2 + [[EmployeeType.Installer_Pending_Certification]] * 2 + [[EmployeeType.Certified_Installer, EmployeeType.Installer_Pending_Certification, EmployeeType.Laborer]] * 4

def schedule_employees(building: Dict, required_employees: List, employees: List[Dict]) -> Dict:
    building["employees"] = []
    for employee in employees:
        print(employee)
        if employee["type"] in required_employees:
            building["employees"].append(employee["name"])
            employees.remove(employee)
    return (building, employees)

def schedule_day(day_num: int, buildings: List[Dict], employees: List[Dict]) -> Dict:
    # expected schema {"day": 0, "buildings": [{"name": "example building", "employees": []}]}
    scheduled_day = {"day": 0}
    
    availibility = employees
    for building in buildings:
        required_employees = generate_require_employees(building)
        (scheduled, availibility) = schedule_employees(building, required_employees, availibility)
        scheduled_day["buildings"] = scheduled
        if len(availibility) == 0:
            break
    
    return schedule_day