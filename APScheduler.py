from apscheduler.scheduler import Scheduler

class APScheduler(object):
    scheduler = None
    @classmethod
    def get_scheduler(self):
        if self.scheduler is None:
            sched = Scheduler()
            sched.start()
            self.scheduler = sched
        return self.scheduler
		
# every hour execute the "some_function_job".
# for loop to check execution_expirer is to put any active cronjob to rest, and re-evaluate if enabled.	

def update_execution_expirer_cronjob(enabled):
    scheduler = APScheduler.get_scheduler()
    for job in scheduler.get_jobs():
        if job.name == 'execution_expirer':
            scheduler.unschedule_job(job)
    if enabled:
        scheduler.add_interval_job(some_function_job, hours=1)
    scheduler.print_jobs()