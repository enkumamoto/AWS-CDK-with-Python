from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_cloudwatch,
    aws_cloudwatch_actions as cw_actions,
    Duration,
)

from constructs import Construct

class MonitoringStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        web_hook_lambda = _lambda.Function(
            self,
            "WebHookLambda",
            runtime = _lambda.Runtime.PYTHON_3_11,
            code = _lambda.Code.from_asset("services"),
            handler = "hook.handler",
        )

        alarm_topic = sns.Topic(
            self, "AlarmTopic", display_name = "AlarmTopic", topic_name = "AlarmTopic",
        )

        alarm_topic.add_subscription(
            subscriptions.LambdaSubscription(web_hook_lambda)
        )

        alarm = aws_cloudwatch.Alarm(
            self,
            "ApiAlarm",
            metric=aws_cloudwatch.Metric(
                metric_name="custom-error",
                namespace="Custom",
                period=Duration.minutes(1),
                statistic="Sum",
            ),
            evaluation_periods=1,
            threshold=100,
        )
    
        topic_action = cw_actions.SnsAction(alarm_topic)
        alarm.add_alarm_action(topic_action)
        alarm.add_ok_action(topic_action)