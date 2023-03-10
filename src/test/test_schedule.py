import pytest
from crown_schedule.schedule import (
    schedule, generate_require_employees,
    schedule_day, BuildingType, EmployeeType)
import faker

Faker = faker.Faker()

# define a series of test fixtures
@pytest.fixture
def employees_fixture():
    return [
        {"name": Faker.name(), "type": EmployeeType.Certified_Installer},
        {"name": Faker.name(), "type": EmployeeType.Installer_Pending_Certification},
        {"name": Faker.name(), "type": EmployeeType.Laborer},
    ]

@pytest.fixture
def buildings_fixture():
    return [
        {"name": "Foo Court", "type": BuildingType.Single_Tenant},
        {"name": "Bar Park", "type": BuildingType.Multi_Tenant},
        {"name": "Baz Tower", "type": BuildingType.Commercial},
    ]

def test_schedule_returns_dict(employees_fixture, buildings_fixture):
    """Test that the schedule function returns a dictionary."""
    buildings = buildings_fixture
    employees = employees_fixture

    result = schedule(buildings, employees)
    assert isinstance(result, list)


def test_generate_required_employees_single_tenant(employees_fixture):
    test_building = {"name": "Test Court", "type":BuildingType.Single_Tenant}
    res = generate_require_employees(test_building)
    assert res == [EmployeeType.Certified_Installer]

# TODO cover other employee types


def test_schedule_day_single_building(employees_fixture):
    test_buildings = [{"name": "Test Court", "type":BuildingType.Single_Tenant}]
    res = schedule_day(0, test_buildings, employees_fixture)
    assert isinstance()