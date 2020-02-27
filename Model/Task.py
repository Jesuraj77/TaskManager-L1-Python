class Task:
    def __init__(self):
        self.taskId
	    self.taskName
	    self.taskStartDate
	    self.taskPriority
	    self.taskEndDate

        def get_taskId(self):
        return self._taskId

        def get_taskName(self):
        return self._taskName

        def get_taskStartDate(self):
        return self._taskStartDate

        def get_taskPriority(self):
        return self._taskPriority

        def get_taskEndDate(self):
        return self._taskEndDate

        def set_taskId(self,taskId):
            self.taskId=taskId
        
        def set_taskName(self,taskName):
            self.taskName=taskName

        def set_taskStartDate(self,taskStartDate):
            self.taskStartDate=taskStartDate

        def set_taskPriority(self,taskPriority):
            self.taskPriority=taskPriority

        def set_taskEndDate(self,taskEndDate):
            self.taskEndDate=taskEndDate
        