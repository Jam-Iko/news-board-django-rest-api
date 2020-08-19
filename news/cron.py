from django_cron import CronJobBase, Schedule
from news.models import Post


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ["00:00"]

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "news.my_cron_job"

    def do(self):
        Post.objects.all().update(upvotes=0)
