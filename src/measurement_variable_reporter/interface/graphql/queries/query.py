from abc import ABC, abstractmethod
from collections import namedtuple
from injector import inject
from graphene import ObjectType, InputObjectType, ID, Float, Field

from src.measurement_variable_reporter.application.services.testService import (
    TestService,
)

LastSampleOutputValueObject = namedtuple("LastSampleOutput", ["id", "last_sample"])

# Input Models
class SensorInput(InputObjectType):
    id = ID()


# Output Models
class LastSampleOutput(ObjectType):
    id = ID()
    last_sample = Float()


# Queries
class SampleQuery(ObjectType):

    get_last_sample = Field(LastSampleOutput, sensor=SensorInput())
    get_samples_by_date_range = Field(LastSampleOutput, sensor=SensorInput())

    def resolve_get_last_sample(root, info, sensor):
        test_servicer = info.context["dependency_container"].get(TestService)
        test_servicer.create("Mike")
        return LastSampleOutputValueObject(id="1", last_sample=1234.0)

    def resolve_get_samples_by_date_range(root, info, sensor):
        return LastSampleOutputValueObject(id="1", last_sample=1234.0)
