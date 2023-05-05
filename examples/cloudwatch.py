from typing import List, Iterator, Optional
import boto3
import re
from dataclasses import dataclass
from enum import Enum


class AlarmState(Enum):
    OK = "OK"
    ALARM = "ALARM"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


@dataclass
class CloudWatchAlarm:
    name: str
    arn: str
    state: str

    @property
    def ok(self):
        return AlarmState[self.state] == AlarmState.OK

    @property
    def alarm(self):
        return AlarmState[self.state] == AlarmState.ALARM

    @property
    def insufficient_data(self):
        return AlarmState[self.state] == AlarmState.INSUFFICIENT_DATA

    @property
    def account_id(self) -> str:
        return re.search(r"arn:aws:cloudwatch:.*:([0-9]{12}):alarm:.*", self.arn).group(
            1
        )

    @property
    def region(self) -> str:
        return re.search(r"arn:aws:cloudwatch:(.*):[0-9]{12}:alarm:.*", self.arn).group(
            1
        )

    def __str__(self) -> str:
        return f"{self.arn} is in a {self.state} state"


class CloudWatch:
    __alarms: List[dict]

    def __init__(self):
        self.__alarms = []

    @staticmethod
    def __parse_response(response: Iterator, key: str) -> List[dict]:
        def flatten(input_: List[List[dict]]) -> List[dict]:
            return [item for sublist in input_ for item in sublist]

        def read_iteration(response_: dict) -> Optional[str]:
            return response_.get(key)

        return flatten(map(read_iteration, response))  # type: ignore

    def get_alarms(self, session: boto3.session.Session, region: str) -> None:
        client = session.client("cloudwatch", region_name=region)
        paginator = client.get_paginator("describe_alarms")
        response_iterator = paginator.paginate(PaginationConfig={"PageSize": 100})

        self.__alarms.extend(self.__parse_response(response_iterator, "MetricAlarms"))

    @property
    def alarms(self) -> List[CloudWatchAlarm]:
        def resolve(alarm: dict) -> CloudWatchAlarm:
            return CloudWatchAlarm(
                name=alarm.get("AlarmName", ""),
                arn=alarm.get("AlarmArn", ""),
                state=alarm.get("StateValue", ""),
            )

        return list(map(resolve, self.__alarms))
